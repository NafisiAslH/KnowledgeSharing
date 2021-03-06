# 7 Security Response Headers Every Security Tester Should Know โก๏ธ
&nbsp;

### 1. Content Security Policy
๐ถ CSP response header prevent code injection or XSS attack.</br>
๐ถ CSP header instruct the browser from which location and which type of resources are allowed to be loaded.</br>
๐ก๏ธ Best configuration practice:</br>
```Content-Security-Policy: script-src โselfโ```</br>
&nbsp;

### 2. X-XSS-Protection
๐ถ X-XSS-Protection header is designed to protect application from XSS.</br>
๐ถ Header will instruct browser to enable XSS filter which are built in modern web browsers like Chrome and Firefox.</br>
๐ก๏ธ Best configuration practice:</br>
```X-XSS-Protection: 1; mode=block```</br>
&nbsp;

### 3. X-Frame-Options
๐ถ X-Frame-Options header is designed to protect the application from clickjacking or UI redressing.</br>
๐ถ Header will instruct the browser not to embed web pages in iframe options.</br>
๐ก๏ธ Best configuration practice:</br>
```X-Frame-Options: DENY```</br>
&nbsp;

### 4. X-Content-Type-Options
๐ถ X-Content-Type-Options header is designed to protect application against MIME sniffing attack.</br>
๐ถ Header will instruct browser that content-type should not be changed and be followed.</br>
๐ก๏ธ Best configuration practice:</br>
```X-Content-Type-Options: nosniff```</br>
&nbsp;

### 5. Access-Control-Allow-Origin
๐ถ Access-Control-Allow-Origin response header deals with resource sharing. Header will instruct the browser whether the response can be shared or not.</br>
๐ก๏ธ Best configuration practice:</br>
```Access-Control-Allow-Origin: http://www.origin.com```</br>
&nbsp;

### 6. Strict-Transport-Security
๐ถ Prevent browser from accessing webs in stateless HTTP connections.</br>
๐ถ Header will instruct browser to access pages using HTTPS, instead of using HTTP</br>
๐ก๏ธ Best configuration practice:</br>
```Strict-Transport-Security: max-age=31536000; includeSubDomains```</br>
&nbsp;

### 7. Public-Key-Pins
๐ถ Public-Key-Pins header prevent web browser from MITM attacks using rogue and forged X.509 certificates.</br>
๐ถ Header will instruct browser to associate/save a specific cert public key, which help browser which certificate to trust.</br>
&nbsp;

## Credit
Based on [Johne_Jacob](https://medium.com/@Johne_Jacob/7-security-response-headers-every-security-tester-should-know-77576ffdfc0f)'s writeup.
</br>&nbsp;

## Support
You can Follow [me](https://twitter.com/MeAsHacker_HNA) on twitter or buy me a [Coffee](https://buymeacoffee.com/NafisiAslH)
