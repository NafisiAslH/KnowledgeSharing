#!python3

import ssl
import sys
import base64
import re
import binascii
try:
    from http.client import HTTPConnection, HTTPSConnection, ResponseNotReady
except ImportError:
    from httplib import HTTPConnection, HTTPSConnection, ResponseNotReady
from impacket import ntlm


AddressList = []

def ewsManage(host, port, mode, domain, user, data,command):

    if command == "getfolderofinbox":
        POST_BODY = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
               xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" 
               xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" 
               xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <m:GetFolder>
      <m:FolderShape>
        <t:BaseShape>Default</t:BaseShape>
      </m:FolderShape>
      <m:FolderIds>
        <t:DistinguishedFolderId Id="inbox"/>
      </m:FolderIds>
    </m:GetFolder>
  </soap:Body>
</soap:Envelope>
'''


    elif command =='getfolderofsentitems': 
        POST_BODY = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
               xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" 
               xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" 
               xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <m:GetFolder>
      <m:FolderShape>
        <t:BaseShape>Default</t:BaseShape>
      </m:FolderShape>
      <m:FolderIds>
        <t:DistinguishedFolderId Id="sentitems"/>
      </m:FolderIds>
    </m:GetFolder>
  </soap:Body>
</soap:Envelope>
'''


    elif command =='listmailofinbox':    
        POST_BODY = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <t:RequestServerVersion Version="Exchange2013_SP1" />
  </soap:Header>
  <soap:Body>
    <m:FindItem Traversal="Shallow">
      <m:ItemShape>
        <t:BaseShape>AllProperties</t:BaseShape>
        <t:BodyType>Text</t:BodyType>
      </m:ItemShape>
      <m:IndexedPageItemView MaxEntriesReturned="2147483647" Offset="0" BasePoint="Beginning" />
      <m:ParentFolderIds>
        <t:DistinguishedFolderId Id="inbox" />
      </m:ParentFolderIds>
    </m:FindItem>
  </soap:Body>
</soap:Envelope>
'''


    elif command =='listmailofsentitems':    
        POST_BODY = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <t:RequestServerVersion Version="Exchange2013_SP1" />
  </soap:Header>
  <soap:Body>
    <m:FindItem Traversal="Shallow">
      <m:ItemShape>
        <t:BaseShape>AllProperties</t:BaseShape>
        <t:BodyType>Text</t:BodyType>
      </m:ItemShape>
      <m:IndexedPageItemView MaxEntriesReturned="2147483647" Offset="0" BasePoint="Beginning" />
      <m:ParentFolderIds>
        <t:DistinguishedFolderId Id="sentitems" />
      </m:ParentFolderIds>
    </m:FindItem>
  </soap:Body>
</soap:Envelope>
'''

    
    elif command =='listmailoffolder':          
        POST_BODY = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <t:RequestServerVersion Version="Exchange2013_SP1" />
  </soap:Header>
  <soap:Body>
    <m:FindItem Traversal="Shallow">
      <m:ItemShape>
        <t:BaseShape>AllProperties</t:BaseShape>
        <t:BodyType>Text</t:BodyType>
      </m:ItemShape>
      <m:IndexedPageItemView MaxEntriesReturned="2147483647" Offset="0" BasePoint="Beginning" />
      <m:ParentFolderIds>
        <t:FolderId Id="{id}" />
      </m:ParentFolderIds>
    </m:FindItem>
  </soap:Body>
</soap:Envelope>
'''
        Id = input("Input the Id of the Folder:")
        POST_BODY = POST_BODY.format(id=Id)


    elif command =='getmail':    
        POST_BODY = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <t:RequestServerVersion Version="Exchange2013_SP1" />
  </soap:Header>
  <soap:Body>
    <m:GetItem>
      <m:ItemShape>
        <t:BaseShape>AllProperties</t:BaseShape>
        <t:BodyType>Text</t:BodyType>
      </m:ItemShape>
      <m:ItemIds>
        <t:ItemId Id="{id}" ChangeKey="{key}" />
      </m:ItemIds>
    </m:GetItem>
  </soap:Body>
</soap:Envelope>
'''
        Id = input("Input the ItemId of the Message:")
        Key = input("Input the ChangeKey of the Message:")
        POST_BODY = POST_BODY.format(id=Id, key=Key)


    elif command =='deletemail':    
        POST_BODY = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <t:RequestServerVersion Version="Exchange2013_SP1" />
  </soap:Header>
  <soap:Body>
    <m:DeleteItem DeleteType="HardDelete" xmlns="https://schemas.microsoft.com/exchange/services/2006/messages">
      <m:ItemIds>
        <t:ItemId Id="{id}"/>
      </m:ItemIds>
    </m:DeleteItem>
  </soap:Body>
</soap:Envelope>
'''
        Id = input("Input the ItemId of the Message:")
        POST_BODY = POST_BODY.format(id=Id)


    elif command =='deletefolder':    
        POST_BODY = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <t:RequestServerVersion Version="Exchange2013_SP1" />
  </soap:Header>
  <soap:Body>
    <m:DeleteFolder DeleteType="HardDelete" xmlns="https://schemas.microsoft.com/exchange/services/2006/messages">
      <m:FolderIds>
        <t:FolderId Id="{id}"/>
      </m:FolderIds>
    </m:DeleteFolder>
  </soap:Body>
</soap:Envelope>
'''
        Id = input("Input the Id of the Folder:")
        POST_BODY = POST_BODY.format(id=Id)


    elif command =='getattachment':    
        POST_BODY = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <t:RequestServerVersion Version="Exchange2013_SP1" />
  </soap:Header>
  <soap:Body>
    <m:GetItem>
      <m:ItemShape>
        <t:BaseShape>IdOnly</t:BaseShape>
        <t:AdditionalProperties>
          <t:FieldURI FieldURI="item:Attachments" />
        </t:AdditionalProperties>
      </m:ItemShape>
      <m:ItemIds>
        <t:ItemId Id="{id}" />
      </m:ItemIds>
    </m:GetItem>
  </soap:Body>
</soap:Envelope>
'''
        Id = input("Input the ItemId of the Message who has Attachments:")
        POST_BODY = POST_BODY.format(id=Id)


    elif command =='saveattachment':          
        POST_BODY = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <t:RequestServerVersion Version="Exchange2013_SP1" />
  </soap:Header>
  <soap:Body>
    <m:GetAttachment>
      <m:AttachmentIds>
        <t:AttachmentId Id="{id}" />
      </m:AttachmentIds>
    </m:GetAttachment>
  </soap:Body>
</soap:Envelope>
'''
        Id = input("Input the Id of the attachment:")
        POST_BODY = POST_BODY.format(id=Id)


    elif command =='deleteattachment':          
        POST_BODY = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <t:RequestServerVersion Version="Exchange2013_SP1" />
  </soap:Header>
  <soap:Body>
    <m:DeleteAttachment>
      <m:AttachmentIds>
        <t:AttachmentId Id="{id}" />
      </m:AttachmentIds>
    </m:DeleteAttachment>
  </soap:Body>
</soap:Envelope>
'''
        Id = input("Input the Id of the attachment:")
        POST_BODY = POST_BODY.format(id=Id)


    elif command =='createattachment':    
        POST_BODY = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <t:RequestServerVersion Version="Exchange2013_SP1" />
  </soap:Header>
  <soap:Body>
    <m:CreateAttachment>
      <m:ParentItemId Id="{id}" ChangeKey="{key}"/>
      <m:Attachments>
        <t:FileAttachment>
          <t:Name>{name}</t:Name>
          <t:Content>{data}</t:Content>
        </t:FileAttachment>
      </m:Attachments>
    </m:CreateAttachment>
  </soap:Body>
</soap:Envelope>
'''
        Id = input("Input the ItemId of the Message:")
        Key = input("Input the ChangeKey of the Message:")
        Name = input("Input the name of the attachment file:")
        Path = input("Input the path of the attachment file:")
        Type = input("Input the type of the attachment file:(text or raw)")
        if Type == 'text':
          with open(Path, 'r') as file_obj:
            content = file_obj.read()
          content = content.encode("utf-8")
        elif Type =='raw':
          with open(Path, 'rb') as file_obj:
            content = file_obj.read()         
        else:
                print('[!]Wrong parameter')
                return False  
       
        base64content = base64.b64encode(content)
        Data = str((base64content),'utf-8')
        POST_BODY = POST_BODY.format(id=Id, key=Key, name=Name, data=Data)


    elif command =='createfolderofinbox':          
        POST_BODY = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <t:RequestServerVersion Version="Exchange2013_SP1" />
  </soap:Header>
  <soap:Body>
    <m:CreateFolder>
      <m:ParentFolderId>
        <t:DistinguishedFolderId Id="inbox" />
      </m:ParentFolderId>
      <m:Folders>
        <t:Folder>
          <t:DisplayName>{name}</t:DisplayName>
        </t:Folder>
      </m:Folders>
    </m:CreateFolder>
  </soap:Body>
</soap:Envelope>
'''
        Name = input("Input the name of the new folder:")
        POST_BODY = POST_BODY.format(name=Name)


    elif command =='SetHiddenPropertyType':          
        POST_BODY = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <t:RequestServerVersion Version="Exchange2013_SP1" />
  </soap:Header>
  <soap:Body>
    <m:GetFolder>
      <m:FolderShape>
        <t:BaseShape>IdOnly</t:BaseShape>
        <t:AdditionalProperties>
          <t:ExtendedFieldURI PropertyTag="4340" PropertyType="Boolean" />
        </t:AdditionalProperties>
      </m:FolderShape>
      <m:FolderIds>
        <t:FolderId Id="{id}" ChangeKey="{key}" />
      </m:FolderIds>
    </m:GetFolder>
  </soap:Body>
</soap:Envelope>
'''
        Id = input("Input the Id of the Folder:")
        Key = input("Input the ChangeKey of the Folder:")
        POST_BODY = POST_BODY.format(id=Id, key=Key)


    elif command =='UpdateHiddenPropertyType':          
        POST_BODY = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <t:RequestServerVersion Version="Exchange2013_SP1" />
  </soap:Header>
  <soap:Body>
    <m:UpdateFolder>
      <m:FolderChanges>
        <t:FolderChange>
          <t:FolderId Id="{id}" ChangeKey="{key}" />
          <t:Updates>
            <t:SetFolderField>
              <t:ExtendedFieldURI PropertyTag="4340" PropertyType="Boolean" />
              <t:Folder>
                <t:ExtendedProperty>
                  <t:ExtendedFieldURI PropertyTag="4340" PropertyType="Boolean" />
                  <t:Value>true</t:Value>
                </t:ExtendedProperty>
              </t:Folder>
            </t:SetFolderField>
          </t:Updates>
        </t:FolderChange>
      </m:FolderChanges>
    </m:UpdateFolder>
  </soap:Body>
</soap:Envelope>
'''
        Id = input("Input the Id of the Folder:")
        Key = input("Input the ChangeKey of the Folder:")
        POST_BODY = POST_BODY.format(id=Id, key=Key)


    elif command =='listhiddenfolderofinbox':          
        POST_BODY = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <t:RequestServerVersion Version="Exchange2013_SP1" />
  </soap:Header>
  <soap:Body>
   <m:FindFolder Traversal="Deep">
      <m:FolderShape>
        <t:BaseShape>IdOnly</t:BaseShape>
        <t:AdditionalProperties>
          <t:ExtendedFieldURI PropertyTag="4340" PropertyType="Boolean" />
          <t:FieldURI FieldURI="folder:DisplayName" />
        </t:AdditionalProperties>
      </m:FolderShape>
      <m:IndexedPageFolderView MaxEntriesReturned="100" Offset="0" BasePoint="Beginning" />
      <m:Restriction>
        <t:IsEqualTo>
          <t:ExtendedFieldURI PropertyTag="4340" PropertyType="Boolean" />
          <t:FieldURIOrConstant>
            <t:Constant Value="true" />
          </t:FieldURIOrConstant>
        </t:IsEqualTo>
      </m:Restriction>
      <m:ParentFolderIds>
        <t:DistinguishedFolderId Id="inbox" />
      </m:ParentFolderIds>
    </m:FindFolder>
  </soap:Body>
</soap:Envelope>
'''


    elif command =='createtestmail':          
        POST_BODY = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <t:RequestServerVersion Version="Exchange2013_SP1" />
  </soap:Header>
  <soap:Body>
    <m:CreateItem MessageDisposition="SaveOnly">
      <m:SavedItemFolderId>
        <t:FolderId Id="{id}" />
      </m:SavedItemFolderId>
      <m:Items>
        <t:Message>
          <t:Subject>test mail</t:Subject>
        </t:Message>
      </m:Items>
    </m:CreateItem>
  </soap:Body>
</soap:Envelope>
'''
        Id = input("Input the Id of the Folder:")
        POST_BODY = POST_BODY.format(id=Id)


    elif command =='getdelegateofinbox': 
        POST_BODY = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <t:RequestServerVersion Version="Exchange2013_SP1" />
  </soap:Header>
  <soap:Body>
    <m:GetDelegate IncludePermissions="true">
      <m:Mailbox>
        <t:EmailAddress>{mail}</t:EmailAddress>
      </m:Mailbox>
    </m:GetDelegate>
  </soap:Body>
</soap:Envelope>
'''
        EmailAddress = input("Input the EmailAddress of current user:")
        POST_BODY = POST_BODY.format(mail=EmailAddress)


    elif command =='adddelegateofinbox':          
        POST_BODY = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <t:RequestServerVersion Version="Exchange2013_SP1" />
  </soap:Header>
  <soap:Body>
    <m:AddDelegate>
      <m:Mailbox>
        <t:EmailAddress>{mail1}</t:EmailAddress>
      </m:Mailbox>
      <m:DelegateUsers>
      <t:DelegateUser>
        <t:UserId>
          <t:PrimarySmtpAddress>{mail2}</t:PrimarySmtpAddress>
        </t:UserId>
        <t:DelegatePermissions>
          <t:InboxFolderPermissionLevel>Editor</t:InboxFolderPermissionLevel>
        </t:DelegatePermissions>
        <t:ReceiveCopiesOfMeetingMessages>false</t:ReceiveCopiesOfMeetingMessages>
        <t:ViewPrivateItems>false</t:ViewPrivateItems>
      </t:DelegateUser>
    </m:DelegateUsers>
      <m:DeliverMeetingRequests>DelegatesAndMe</m:DeliverMeetingRequests>
    </m:AddDelegate>
  </soap:Body>
</soap:Envelope>
'''
        EmailAddress1 = input("Input the EmailAddress of current user:")
        EmailAddress2 = input("Input the EmailAddress of target user:")
        POST_BODY = POST_BODY.format(mail1=EmailAddress1, mail2=EmailAddress2)


    elif command =='updatedelegateofinbox':          
        POST_BODY = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <t:RequestServerVersion Version="Exchange2013_SP1" />
  </soap:Header>
  <soap:Body>
    <m:UpdateDelegate>
      <m:Mailbox>
        <t:EmailAddress>{mail1}</t:EmailAddress>
      </m:Mailbox>
      <m:DelegateUsers>
      <t:DelegateUser>
        <t:UserId>
          <t:PrimarySmtpAddress>{mail2}</t:PrimarySmtpAddress>
        </t:UserId>
        <t:DelegatePermissions>
          <t:InboxFolderPermissionLevel>Editor</t:InboxFolderPermissionLevel>
        </t:DelegatePermissions>
        <t:ReceiveCopiesOfMeetingMessages>false</t:ReceiveCopiesOfMeetingMessages>
        <t:ViewPrivateItems>true</t:ViewPrivateItems>
      </t:DelegateUser>
    </m:DelegateUsers>
      <m:DeliverMeetingRequests>DelegatesAndMe</m:DeliverMeetingRequests>
    </m:UpdateDelegate>
  </soap:Body>
</soap:Envelope>
'''
        EmailAddress1 = input("Input the EmailAddress of current user:")
        EmailAddress2 = input("Input the EmailAddress of target user:")
        POST_BODY = POST_BODY.format(mail1=EmailAddress1, mail2=EmailAddress2)


    elif command =='removedelegateofinbox':          
        POST_BODY = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <t:RequestServerVersion Version="Exchange2013_SP1" />
  </soap:Header>
  <soap:Body>
    <m:RemoveDelegate>
      <m:Mailbox>
        <t:EmailAddress>{mail1}</t:EmailAddress>
      </m:Mailbox>
      <m:UserIds>
        <t:UserId>
          <t:PrimarySmtpAddress>{mail2}</t:PrimarySmtpAddress>
        </t:UserId>
    </m:UserIds>
    </m:RemoveDelegate>
  </soap:Body>
</soap:Envelope>
'''
        EmailAddress1 = input("Input the EmailAddress of current user:")
        EmailAddress2 = input("Input the EmailAddress of target user:")
        POST_BODY = POST_BODY.format(mail1=EmailAddress1, mail2=EmailAddress2)


#https://docs.microsoft.com/en-us/exchange/client-developer/exchange-web-services/how-to-set-folder-permissions-for-another-user-by-using-ews-in-exchange
#Doesn't support sentitems
    elif command =='getdelegateofinbox2': 
        POST_BODY = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
               xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" 
               xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" 
               xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <t:RequestServerVersion Version="Exchange2013_SP1" />
  </soap:Header>
  <soap:Body>
    <m:GetFolder>
      <m:FolderShape>
        <t:BaseShape>IdOnly</t:BaseShape>
        <t:AdditionalProperties>
          <t:FieldURI FieldURI="folder:PermissionSet"/>
        </t:AdditionalProperties>
      </m:FolderShape>
      <m:FolderIds>
        <t:DistinguishedFolderId Id="inbox" />
      </m:FolderIds>
    </m:GetFolder>
  </soap:Body>
</soap:Envelope>
'''


    elif command =='adddelegateofinbox2': 
        POST_BODY = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
               xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" 
               xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" 
               xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <t:RequestServerVersion Version="Exchange2013_SP1" />
  </soap:Header>
  <soap:Body>
    <m:UpdateFolder>
      <m:FolderChanges>
        <t:FolderChange>
          <t:FolderId Id="{id}" ChangeKey="{key}" />
          <t:Updates>
            <t:SetFolderField>
              <t:FieldURI FieldURI="folder:PermissionSet" />
              <t:Folder>
                <t:PermissionSet>
                  <t:Permissions>
                    <t:Permission>
                      <t:UserId>
                        <t:DistinguishedUser>Default</t:DistinguishedUser>
                      </t:UserId>
                      <t:CanCreateItems>false</t:CanCreateItems>
                      <t:CanCreateSubFolders>false</t:CanCreateSubFolders>
                      <t:IsFolderOwner>false</t:IsFolderOwner>
                      <t:IsFolderVisible>false</t:IsFolderVisible>
                      <t:IsFolderContact>false</t:IsFolderContact>
                      <t:EditItems>None</t:EditItems>
                      <t:DeleteItems>None</t:DeleteItems>
                      <t:ReadItems>None</t:ReadItems>
                      <t:PermissionLevel>None</t:PermissionLevel>
                    </t:Permission>
                    <t:Permission>
                    <t:UserId>
                      <t:DistinguishedUser>Anonymous</t:DistinguishedUser>
                    </t:UserId>
                    <t:CanCreateItems>false</t:CanCreateItems>
                    <t:CanCreateSubFolders>false</t:CanCreateSubFolders>
                    <t:IsFolderOwner>false</t:IsFolderOwner>
                    <t:IsFolderVisible>false</t:IsFolderVisible>
                    <t:IsFolderContact>false</t:IsFolderContact>
                    <t:EditItems>None</t:EditItems>
                    <t:DeleteItems>None</t:DeleteItems>
                    <t:ReadItems>None</t:ReadItems>
                    <t:PermissionLevel>None</t:PermissionLevel>
                    </t:Permission>
                    <t:Permission>
                      <t:UserId>
                        <t:PrimarySmtpAddress>{mail}</t:PrimarySmtpAddress>
                      </t:UserId>
                      <t:PermissionLevel>Editor</t:PermissionLevel>
                    </t:Permission>
                  </t:Permissions>
                </t:PermissionSet>
              </t:Folder>
            </t:SetFolderField>
          </t:Updates>
        </t:FolderChange>
      </m:FolderChanges>
    </m:UpdateFolder>
  </soap:Body>
</soap:Envelope>
'''

        Id = input("Input the Id of Inbox:")
        Key = input("Input the ChangeKey of Inbox:")
        EmailAddress = input("Input the EmailAddress of target user:")
        POST_BODY = POST_BODY.format(id=Id, key=Key, mail=EmailAddress)


    elif command =='restoredelegateofinbox2': 
        POST_BODY = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
               xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" 
               xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" 
               xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <t:RequestServerVersion Version="Exchange2013_SP1" />
  </soap:Header>
  <soap:Body>
    <m:UpdateFolder>
      <m:FolderChanges>
        <t:FolderChange>
          <t:FolderId Id="{id}" ChangeKey="{key}" />
          <t:Updates>
            <t:SetFolderField>
              <t:FieldURI FieldURI="folder:PermissionSet" />
              <t:Folder>
                <t:PermissionSet>
                  <t:Permissions>
                    <t:Permission>
                      <t:UserId>
                        <t:DistinguishedUser>Default</t:DistinguishedUser>
                      </t:UserId>
                      <t:CanCreateItems>false</t:CanCreateItems>
                      <t:CanCreateSubFolders>false</t:CanCreateSubFolders>
                      <t:IsFolderOwner>false</t:IsFolderOwner>
                      <t:IsFolderVisible>false</t:IsFolderVisible>
                      <t:IsFolderContact>false</t:IsFolderContact>
                      <t:EditItems>None</t:EditItems>
                      <t:DeleteItems>None</t:DeleteItems>
                      <t:ReadItems>None</t:ReadItems>
                      <t:PermissionLevel>None</t:PermissionLevel>
                    </t:Permission>
                    <t:Permission>
                    <t:UserId>
                      <t:DistinguishedUser>Anonymous</t:DistinguishedUser>
                    </t:UserId>
                    <t:CanCreateItems>false</t:CanCreateItems>
                    <t:CanCreateSubFolders>false</t:CanCreateSubFolders>
                    <t:IsFolderOwner>false</t:IsFolderOwner>
                    <t:IsFolderVisible>false</t:IsFolderVisible>
                    <t:IsFolderContact>false</t:IsFolderContact>
                    <t:EditItems>None</t:EditItems>
                    <t:DeleteItems>None</t:DeleteItems>
                    <t:ReadItems>None</t:ReadItems>
                    <t:PermissionLevel>None</t:PermissionLevel>
                    </t:Permission>
                  </t:Permissions>
                </t:PermissionSet>
              </t:Folder>
            </t:SetFolderField>
          </t:Updates>
        </t:FolderChange>
      </m:FolderChanges>
    </m:UpdateFolder>
  </soap:Body>
</soap:Envelope>
'''

        Id = input("Input the Id of Inbox:")
        Key = input("Input the ChangeKey of Inbox:")
        POST_BODY = POST_BODY.format(id=Id, key=Key)


    elif command =='getinboxrules':         
        POST_BODY = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <t:RequestServerVersion Version="Exchange2013_SP1" />
  </soap:Header>
  <soap:Body>
    <m:GetInboxRules>
      <m:MailboxSmtpAddress>{mail1}</m:MailboxSmtpAddress>
    </m:GetInboxRules>
  </soap:Body>
</soap:Envelope>
'''
        EmailAddress1 = input("Input the EmailAddress of current user:")
        POST_BODY = POST_BODY.format(mail1=EmailAddress1)


    elif command =='updateinboxrules':         
        POST_BODY = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <t:RequestServerVersion Version="Exchange2013_SP1" />
  </soap:Header>
  <soap:Body>
    <m:UpdateInboxRules>
      <m:RemoveOutlookRuleBlob>true</m:RemoveOutlookRuleBlob>
      <m:Operations>
        <t:CreateRuleOperation>
          <t:Rule>
            <t:DisplayName>ForwardRule</t:DisplayName>
            <t:Priority>1</t:Priority>
            <t:IsEnabled>true</t:IsEnabled>
            <t:Conditions />
            <t:Exceptions />
            <t:Actions>
              <t:ForwardToRecipients>
                <t:Address>
                  <t:EmailAddress>{mail1}</t:EmailAddress>
                </t:Address>
              </t:ForwardToRecipients>
            </t:Actions>
          </t:Rule>
        </t:CreateRuleOperation>
      </m:Operations>
    </m:UpdateInboxRules>
  </soap:Body>
</soap:Envelope>
'''
        EmailAddress1 = input("Input the EmailAddress you want to forward to:")
        POST_BODY = POST_BODY.format(mail1=EmailAddress1)


    elif command =='removeinboxrules':  
        POST_BODY = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <t:RequestServerVersion Version="Exchange2013_SP1" />
  </soap:Header>
  <soap:Body>
    <m:UpdateInboxRules>
      <m:RemoveOutlookRuleBlob>true</m:RemoveOutlookRuleBlob>
        <m:Operations>
          <t:DeleteRuleOperation>
            <t:RuleId>{id}</t:RuleId>
          </t:DeleteRuleOperation>
        </m:Operations>
    </m:UpdateInboxRules>
  </soap:Body>
</soap:Envelope>
'''
        RuleId = input("Input the rule ID:")
        POST_BODY = POST_BODY.format(id=RuleId)


    elif command =='getcontact':    
        POST_BODY = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <t:RequestServerVersion Version="Exchange2013_SP1" />
  </soap:Header>
  <soap:Body>
      <m:FindPeople>
         <m:IndexedPageItemView BasePoint="Beginning" MaxEntriesReturned="1000" Offset="0"/>
         <m:ParentFolderId>
            <t:DistinguishedFolderId Id="contacts"/>
         </m:ParentFolderId>
      </m:FindPeople>
  </soap:Body>
</soap:Envelope>
'''


    elif command =='findpeople':   
        print('[*]This operation can only be used on Exchange Server 2013 or newer version') 
        POST_BODY = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <t:RequestServerVersion Version="Exchange2013_SP1" />
  </soap:Header>
  <soap:Body>
      <m:FindPeople>
         <m:IndexedPageItemView BasePoint="Beginning" MaxEntriesReturned="1000" Offset="0"/>
         <m:ParentFolderId>
            <t:DistinguishedFolderId Id="directory"/>
         </m:ParentFolderId>
         <m:QueryString>{string}</m:QueryString>
      </m:FindPeople>
  </soap:Body>
</soap:Envelope>
'''
        QueryString = input("Input the QueryString:")
        POST_BODY = POST_BODY.format(string=QueryString)


    elif command =='resolvename':
        POST_BODY = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <t:RequestServerVersion Version="Exchange2013_SP1" />
  </soap:Header>
  <soap:Body>
     <m:ResolveNames ReturnFullContactData="false" SearchScope="ContactsActiveDirectory">
      <m:UnresolvedEntry>{string}</m:UnresolvedEntry>
    </m:ResolveNames>
  </soap:Body>
</soap:Envelope>
'''
        QueryString = input("Input the resolved entry:")
        POST_BODY = POST_BODY.format(string=QueryString)


    else:    
        print('[!]Wrong parameter')
        return False

    ews_url = "/EWS/Exchange.asmx"

    if port ==443:
        try:
            uv_context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
            session = HTTPSConnection(host, port, context=uv_context)
        except AttributeError:
            session = HTTPSConnection(host, port)
    else:        
        session = HTTPConnection(host, port)

    # Use impacket for NTLM
    ntlm_nego = ntlm.getNTLMSSPType1(host, domain)

    #Negotiate auth
    negotiate = base64.b64encode(ntlm_nego.getData())
    # Headers
    headers = {
        "Authorization": 'NTLM %s' % negotiate.decode('utf-8'),
        "Content-type": "text/xml; charset=utf-8",
        "Accept": "text/xml",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
    }

    session.request("POST", ews_url, POST_BODY, headers)

    res = session.getresponse()
    res.read()

    if res.status != 401:
        print('Status code returned: %d. Authentication does not seem required for URL'%(res.status))
        return False
    try:
        if 'NTLM' not in res.getheader('WWW-Authenticate'):
            print('NTLM Auth not offered by URL, offered protocols: %s'%(res.getheader('WWW-Authenticate')))
            return False
    except (KeyError, TypeError):
        print('No authentication requested by the server for url %s'%(ews_url))
        return False

    print('[*] Got 401, performing NTLM authentication')
    # Get negotiate data
    try:
        ntlm_challenge_b64 = re.search('NTLM ([a-zA-Z0-9+/]+={0,2})', res.getheader('WWW-Authenticate')).group(1)
        ntlm_challenge = base64.b64decode(ntlm_challenge_b64)
    except (IndexError, KeyError, AttributeError):
        print('No NTLM challenge returned from server')
        return False


    if mode =='plaintext':
        password1 = data;
        nt_hash = ''

    elif mode =='ntlmhash':
        password1 = ''
        nt_hash = binascii.unhexlify(data)

    else:
        print('[!]Wrong parameter')
        return False

    lm_hash = ''    
    ntlm_auth, _ = ntlm.getNTLMSSPType3(ntlm_nego, ntlm_challenge, user, password1, domain, lm_hash, nt_hash)
    auth = base64.b64encode(ntlm_auth.getData())

    headers = {
        "Authorization": 'NTLM %s' % auth.decode('utf-8'),
        "Content-type": "text/xml; charset=utf-8",
        "Accept": "text/xml",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
    }

    session.request("POST", ews_url, POST_BODY, headers)
    res = session.getresponse()
    body = res.read()
    filename = command + ".xml"
    if res.status == 401:
        print('[!] Server returned HTTP status 401 - authentication failed')
        return False

    else:
        print('[+] Valid:%s %s'%(user,data))       
        #print(body)
        print('[+] Save response file to %s'%(filename))
        with open(filename, 'w+', encoding='utf-8') as file_object:
            file_object.write(bytes.decode(body))
        if res.status == 200:
            if command =='getattachment':
                responsecode_name = re.compile(r"<m:ResponseCode>(.*?)</m:ResponseCode>")
                responsecode = responsecode_name.findall(bytes.decode(body))
                if responsecode[0] =='NoError':
                    pattern_name = re.compile(r"<t:Name>(.*?)</t:Name>")
                    name = pattern_name.findall(bytes.decode(body))
                    for i in range(len(name)):       
                        print("[+] Attachment name: %s"%(name[i]))

            elif command =='saveattachment':
                responsecode_name = re.compile(r"<m:ResponseCode>(.*?)</m:ResponseCode>")
                responsecode = responsecode_name.findall(bytes.decode(body))
                if responsecode[0] =='NoError':
                    pattern_name = re.compile(r"<t:Name>(.*?)</t:Name>")
                    name = pattern_name.findall(bytes.decode(body))
                    print('[+] Save attachment to %s'%(name[0]))
                    pattern_data = re.compile(r"<t:Content>(.*?)</t:Content>")
                    attachmentdata = pattern_data.findall(bytes.decode(body))

                    pattern_type = re.compile(r"<t:ContentType>(.*?)</t:ContentType>")
                    contenttype = pattern_type.findall(bytes.decode(body))
                    if 'text' in contenttype:
                        truedata = base64.b64decode(attachmentdata[0])
                        with open(name[0], 'w+') as file_object:
                            file_object.write(truedata)
                    else:
                        truedata = base64.b64decode(attachmentdata[0])
                        with open(name[0], 'wb+') as file_object:
                            file_object.write(truedata)                   
                          
                else:
                    print('[!] %s'%(responsecode[0]))

            elif command =='findpeople':
                responsecode_name = re.compile(r"<ResponseCode>(.*?)</ResponseCode>")
                responsecode = responsecode_name.findall(bytes.decode(body))
                if responsecode[0] =='NoError':
                    pattern_name = re.compile(r"<Address>(.*?)</Address>")
                    name = pattern_name.findall(bytes.decode(body))
                    for i in range(len(name)): 
                        data = name[i]
                        x = data.find('<EmailAddress>')
                        y = data.find('</EmailAddress>')
                        data = data[x+14:y] 
                        print("[+] EmailAddress: %s"%(data))

            elif command =='resolvename':
                responsecode_name = re.compile(r"<m:ResponseCode>(.*?)</m:ResponseCode>")
                responsecode = responsecode_name.findall(bytes.decode(body))
                pattern_name = re.compile(r"<t:EmailAddress>(.*?)</t:EmailAddress>")
                name = pattern_name.findall(bytes.decode(body))
                x = bytes.decode(body).find('TotalItemsInView')
                y = bytes.decode(body).find('IncludesLastItemInRange')
                if y==-1:
                    print("[!] No results")
                    return True  
                size = bytes.decode(body)[x+18:y-2] 

                print("[+] Total results: %s\r\n"%(size))
                if size=='100':
                    print("[!] Search results may be incomplete, need to add search criteria.")
                    return True  

                for i in range(len(name)):       
                    print("[+] EmailAddress: %s"%(name[i]))

        return True

def ewsManage_findallpeople(host, port, mode, domain, user, data,QueryString):
    POST_BODY = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <t:RequestServerVersion Version="Exchange2013_SP1" />
  </soap:Header>
  <soap:Body>
      <m:FindPeople>
         <m:IndexedPageItemView BasePoint="Beginning" MaxEntriesReturned="1000" Offset="0"/>
         <m:ParentFolderId>
            <t:DistinguishedFolderId Id="directory"/>
         </m:ParentFolderId>
         <m:QueryString>{string}</m:QueryString>
      </m:FindPeople>
  </soap:Body>
</soap:Envelope>
'''
    POST_BODY = POST_BODY.format(string=QueryString)

    ews_url = "/EWS/Exchange.asmx"
    if port ==443:
        try:
            uv_context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
            session = HTTPSConnection(host, port, context=uv_context)
        except AttributeError:
            session = HTTPSConnection(host, port)
    else:        
        session = HTTPConnection(host, port)

    # Use impacket for NTLM
    ntlm_nego = ntlm.getNTLMSSPType1(host, domain)

    #Negotiate auth
    negotiate = base64.b64encode(ntlm_nego.getData())
    # Headers
    headers = {
        "Authorization": 'NTLM %s' % negotiate.decode('utf-8'),
        "Content-type": "text/xml; charset=utf-8",
        "Accept": "text/xml",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
    }

    session.request("POST", ews_url, POST_BODY, headers)
    res = session.getresponse()
    res.read()
    if res.status != 401:
        print('Status code returned: %d. Authentication does not seem required for URL'%(res.status))
        sys.exit(0)
    try:
        if 'NTLM' not in res.getheader('WWW-Authenticate'):
            print('NTLM Auth not offered by URL, offered protocols: %s'%(res.getheader('WWW-Authenticate')))
            sys.exit(0)
    except (KeyError, TypeError):
        print('No authentication requested by the server for url %s'%(ews_url))
        sys.exit(0)

    # Get negotiate data
    try:
        ntlm_challenge_b64 = re.search('NTLM ([a-zA-Z0-9+/]+={0,2})', res.getheader('WWW-Authenticate')).group(1)
        ntlm_challenge = base64.b64decode(ntlm_challenge_b64)
    except (IndexError, KeyError, AttributeError):
        print('No NTLM challenge returned from server')
        sys.exit(0)

    if mode =='plaintext':
        password1 = data;
        nt_hash = ''

    elif mode =='ntlmhash':
        password1 = ''
        nt_hash = binascii.unhexlify(data)

    else:
        print('[!]Wrong parameter')
        sys.exit(0)

    lm_hash = ''    
    ntlm_auth, _ = ntlm.getNTLMSSPType3(ntlm_nego, ntlm_challenge, user, password1, domain, lm_hash, nt_hash)
    auth = base64.b64encode(ntlm_auth.getData())

    headers = {
        "Authorization": 'NTLM %s' % auth.decode('utf-8'),
        "Content-type": "text/xml; charset=utf-8",
        "Accept": "text/xml",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
    }

    session.request("POST", ews_url, POST_BODY, headers)
    res = session.getresponse()
    body = res.read()

    if res.status == 401: 
        print('[!] Server returned HTTP status 401 - authentication failed')          
        sys.exit(0)

    else:       
        if res.status == 200: 
            responsecode_name = re.compile(r"<ResponseCode>(.*?)</ResponseCode>")
            responsecode = responsecode_name.findall(bytes.decode(body))
            if responsecode[0] =='NoError':
                pattern_name = re.compile(r"<Address>(.*?)</Address>")
                name = pattern_name.findall(bytes.decode(body))
                name = list(set(name))                
                for i in range(len(name)): 
                    data = name[i]
                    x = data.find('<EmailAddress>')
                    y = data.find('</EmailAddress>')
                    data = data[x+14:y]
                    AddressList.append(data)
        return True


def ewsManage_resolveallname(host, port, mode, domain, user, data,QueryString):
    POST_BODY = '''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <t:RequestServerVersion Version="Exchange2013_SP1" />
  </soap:Header>
  <soap:Body>
     <m:ResolveNames ReturnFullContactData="false" SearchScope="ContactsActiveDirectory">
      <m:UnresolvedEntry>{string}</m:UnresolvedEntry>
    </m:ResolveNames>
  </soap:Body>
</soap:Envelope>
'''

    POST_BODY = POST_BODY.format(string=QueryString)

    ews_url = "/EWS/Exchange.asmx"
    if port ==443:
        try:
            uv_context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
            session = HTTPSConnection(host, port, context=uv_context)
        except AttributeError:
            session = HTTPSConnection(host, port)
    else:        
        session = HTTPConnection(host, port)

    # Use impacket for NTLM
    ntlm_nego = ntlm.getNTLMSSPType1(host, domain)

    #Negotiate auth
    negotiate = base64.b64encode(ntlm_nego.getData())
    # Headers
    headers = {
        "Authorization": 'NTLM %s' % negotiate.decode('utf-8'),
        "Content-type": "text/xml; charset=utf-8",
        "Accept": "text/xml",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
    }

    session.request("POST", ews_url, POST_BODY, headers)
    res = session.getresponse()
    res.read()
    if res.status != 401:
        print('Status code returned: %d. Authentication does not seem required for URL'%(res.status))
        sys.exit(0)
    try:
        if 'NTLM' not in res.getheader('WWW-Authenticate'):
            print('NTLM Auth not offered by URL, offered protocols: %s'%(res.getheader('WWW-Authenticate')))
            sys.exit(0)
    except (KeyError, TypeError):
        print('No authentication requested by the server for url %s'%(ews_url))
        sys.exit(0)

    # Get negotiate data
    try:
        ntlm_challenge_b64 = re.search('NTLM ([a-zA-Z0-9+/]+={0,2})', res.getheader('WWW-Authenticate')).group(1)
        ntlm_challenge = base64.b64decode(ntlm_challenge_b64)
    except (IndexError, KeyError, AttributeError):
        print('No NTLM challenge returned from server')
        sys.exit(0)

    if mode =='plaintext':
        password1 = data;
        nt_hash = ''

    elif mode =='ntlmhash':
        password1 = ''
        nt_hash = binascii.unhexlify(data)

    else:
        print('[!]Wrong parameter')
        sys.exit(0)

    lm_hash = ''    
    ntlm_auth, _ = ntlm.getNTLMSSPType3(ntlm_nego, ntlm_challenge, user, password1, domain, lm_hash, nt_hash)
    auth = base64.b64encode(ntlm_auth.getData())

    headers = {
        "Authorization": 'NTLM %s' % auth.decode('utf-8'),
        "Content-type": "text/xml; charset=utf-8",
        "Accept": "text/xml",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
    }

    session.request("POST", ews_url, POST_BODY, headers)
    res = session.getresponse()
    body = res.read()

    if res.status == 401: 
        print('[!] Server returned HTTP status 401 - authentication failed')          
        sys.exit(0)

    else:       
        if res.status == 200: 
            if 'No results were found.' in bytes.decode(body):
                return False

            x = bytes.decode(body).find('TotalItemsInView')
            y = bytes.decode(body).find('IncludesLastItemInRange')
            if y==-1:
                return True  
            size = bytes.decode(body)[x+18:y-2] 
            if size=='100':
                print("[!] Search results may be incomplete, need to add search criteria.")

            responsecode_name = re.compile(r"<m:ResponseCode>(.*?)</m:ResponseCode>")
            responsecode = responsecode_name.findall(bytes.decode(body))
            pattern_name = re.compile(r"<t:EmailAddress>(.*?)</t:EmailAddress>")
            name = pattern_name.findall(bytes.decode(body))
            for i in range(len(name)):  
                AddressList.append(name[i]) 
        return True

if __name__ == '__main__':
    if len(sys.argv)!=8:
        print('[!]Wrong parameter')     
        print('ewsManage')       
        print('Use to access Exchange Web Service(Support plaintext and ntlmhash)')
        print('Author:3gstudent')      
        print('Reference:https://github.com/dirkjanm/PrivExchange/blob/master/privexchange.py')  
        print('Usage:')
        print('%s <host> <port> <mode> <domain> <user> <password> <command>'%(sys.argv[0]))
        print('<mode>:')
        print('- plaintext')   
        print('- ntlmhash')
        print('<command>:')
        print('- getfolderofinbox')
        print('- getfolderofsentitems')  
        print('- listmailofinbox')
        print('- listmailofsentitems')
        print('- listmailoffolder') 
        print('- getmail')
        print('- deletemail')
        print('- deletefolder')
        print('- getattachment')
        print('- saveattachment')
        print('- getdelegateofinbox')
        print('- adddelegateofinbox')
        print('- updatedelegateofinbox')
        print('- removedelegateofinbox')
        print('- getdelegateofinbox2')
        print('- updatedelegateofinbox2')
        print('- restoredelegateofinbox2')       
        print('- getinboxrules')
        print('- updateinboxrules')
        print('- removeinboxrules')
        print('- deleteattachment')
        print('- createattachment')
        print('- createfolderofinbox')
        print('- listhiddenfolderofinbox')
        print('- createtestmail')
        print('- SetHiddenPropertyType')               
        print('- UpdateHiddenPropertyType')
        print('- getcontact')
        print('- findpeople')
        print('- findallpeople') 
        print('- resolvename')
        print('- resolveallname') 
        print('Eg.')
        print('%s 192.168.1.1 443 plaintext test.com user1 password1 getfolderofinbox'%(sys.argv[0]))
        print('%s test.com 80 ntlmhash test.com user1 c5a237b7e9d8e708d8436b6148a25fa1 listmailofinbox'%(sys.argv[0]))
        sys.exit(0)
    else:
        if sys.argv[7] == "findallpeople":
            print('[*]This operation can only be used on Exchange Server 2013 or newer version')
            for i in range(97,123):
                ewsManage_findallpeople(sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], chr(i))
            print("[+] GlobalAddressList:")    
            AddressList = list(set(AddressList))
            for i in range(len(AddressList)):
                print("%s"%(AddressList[i]))

        elif sys.argv[7] == "resolveallname": 
            for i in range(97,123):
                for j in range(97,123):  
                    ewsManage_resolveallname(sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], chr(i)+chr(j))
            print("[+] GlobalAddressList:")    
            AddressList = list(set(AddressList))
            for i in range(len(AddressList)):
                print("%s"%(AddressList[i]))        

        else:  
            ewsManage(sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])
