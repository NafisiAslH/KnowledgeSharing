# Account Takeover in ChatGPT

1. We could access `https://chat.openai.com/api/auth/session` and the API will return our account data, such as name, email, ID, and the most critical one: our access token.

2. Now if we go to `https://chat.openai.com/api/auth/session/victim.css`, we will find the same content as `/api/auth/session`, regardless of whether the victim.css file exists on the server.

3. This way, the server’s web cache will see the “.css” extension and victim.css will be cached by the server with the victim’s session content

4. Now the hacker could simply go to `https://chat.openai.com/api/auth/session/victim.css` and retrieve all of the victim’s authentication data.
<br>&nbsp;

## Credit
Based on [Diego Tellaroli](https://medium.com/@diegotellaroli05/account-takeover-in-chatgpt-e134ed11654d)'s writeup.
<br>&nbsp;

## Support
You can Follow [me](https://twitter.com/MeAsHacker_HNA) on twitter or
<br><br><a href="https://www.buymeacoffee.com/NafisiAslH" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
