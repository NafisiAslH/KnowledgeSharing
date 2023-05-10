# Trick - Modify Token

### Description
details
</br>&nbsp;

## Sub Techniques
### 1. Use another user's Token
```
cookie: session=SESSION_A;
token = TOKEN_B
```
### 2. Reuse Token (Check token expiration)
```
First request:
token = TOKEN

Second request:
token = TOKEN
```
### 3. Remove parameter (name and value)
```
remove name and value
```
### 4. Send empty value
```
token = (empty)
```
### 7. Modify a few bits
```
origianl token: TOKEN_123456
forged token: TOKEN_123478
```
### 6. Send null/None value
```
token = None
token = null
```

<br>&nbsp;
## References:
[Reference](link)</br>

<br>&nbsp;
## Support
You can Follow [me](https://twitter.com/MeAsHacker_HNA) on twitter or
<br><br><a href="https://www.buymeacoffee.com/NafisiAslH" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
