# Trick - Change Request Method

### Description
details
</br>&nbsp;

## Sub Techniques
### 1. Change in http protocol.
- You can use burp suite.
### 2. Method Override Functionality
```
Use a POST method and send:
https://target.com/some/endpoint/num?_method=PUT
```
### 3. Use Header:
```
X-HTTP-Method: PUT
X-HTTP-Method-Override: PUT
X-Method-Override: PUT
```

## Refrences:
[REF](https://book.hacktricks.xyz/pentesting-web/csrf-cross-site-request-forgery)</br>
