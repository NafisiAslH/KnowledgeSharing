# IDOR a Highest Bounty 🍺

1. I used google dorks for recon the website.
```
site:*.example.com inurl:.aspx
```
2. In the result, the user data has been leaked and URL is like this
```
https://buy.example.com/protect/landing.aspx?base64encodeddata
```
3. This base64 encoded data is a user’s mobile number by which a user is validated.
4. I changed the mobile number to other user’s mobile number and BOOM!
5. this Vulnerability gives me 2000$ and the severity of this bug is P0 

## Credit
Based on [omdubey170](https://medium.com/@omdubey170/idor-a-highest-bounty-6dae1bb10b66)'s writeup.
<br>&nbsp;

## Support
You can Follow [me](https://twitter.com/MeAsHacker_HNA) on twitter or
<br><br><a href="https://www.buymeacoffee.com/NafisiAslH" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
