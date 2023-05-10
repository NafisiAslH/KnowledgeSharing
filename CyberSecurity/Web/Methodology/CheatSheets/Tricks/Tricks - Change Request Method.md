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

<br>&nbsp;
## Refrences:
[REF](https://book.hacktricks.xyz/pentesting-web/csrf-cross-site-request-forgery)</br>

<br>&nbsp;
## Support
You can Follow [me](https://twitter.com/MeAsHacker_HNA) on twitter or
<br><br><a href="https://www.buymeacoffee.com/NafisiAslH" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
