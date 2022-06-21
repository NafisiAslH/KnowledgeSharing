# 7 Security Response Headers Every Security Tester Should Know ⚡️
&nbsp;

### 1. Content Security Policy
🔶 CSP response header prevent code injection or XSS attack.</br>
🔶 CSP header instruct the browser from which location and which type of resources are allowed to be loaded.</br>
🛡️ Best configuration practice:</br>
```Content-Security-Policy: script-src ‘self’```</br>
&nbsp;

### 2. X-XSS-Protection
🔶 X-XSS-Protection header is designed to protect application from XSS.</br>
🔶 Header will instruct browser to enable XSS filter which are built in modern web browsers like Chrome and Firefox.</br>
🛡️ Best configuration practice:</br>
```X-XSS-Protection: 1; mode=block```</br>
&nbsp;

### 3. X-Frame-Options
🔶 X-Frame-Options header is designed to protect the application from clickjacking or UI redressing.</br>
🔶 Header will instruct the browser not to embed web pages in iframe options.</br>
🛡️ Best configuration practice:</br>
```X-Frame-Options: DENY```</br>
&nbsp;

### 4. X-Content-Type-Options
🔶 X-Content-Type-Options header is designed to protect application against MIME sniffing attack.</br>
🔶 Header will instruct browser that content-type should not be changed and be followed.</br>
🛡️ Best configuration practice:</br>
```X-Content-Type-Options: nosniff```</br>
&nbsp;

### 5. Access-Control-Allow-Origin
🔶 Access-Control-Allow-Origin response header deals with resource sharing. Header will instruct the browser whether the response can be shared or not.</br>
🛡️ Best configuration practice:</br>
```Access-Control-Allow-Origin: http://www.origin.com```</br>
&nbsp;

### 6. Strict-Transport-Security
🔶 Prevent browser from accessing webs in stateless HTTP connections.</br>
🔶 Header will instruct browser to access pages using HTTPS, instead of using HTTP</br>
🛡️ Best configuration practice:</br>
```Strict-Transport-Security: max-age=31536000; includeSubDomains```</br>
&nbsp;

### 7. Public-Key-Pins
🔶 Public-Key-Pins header prevent web browser from MITM attacks using rogue and forged X.509 certificates.</br>
🔶 Header will instruct browser to associate/save a specific cert public key, which help browser which certificate to trust.</br>
&nbsp;

## Credit
Based on [Johne_Jacob](https://medium.com/@Johne_Jacob/7-security-response-headers-every-security-tester-should-know-77576ffdfc0f)'s writeup.
</br>&nbsp;

## Support
You can Follow [me](https://twitter.com/MeAsHacker_HNA) on twitter or buy me a [Coffee](https://buymeacoffee.com/NafisiAslH)
