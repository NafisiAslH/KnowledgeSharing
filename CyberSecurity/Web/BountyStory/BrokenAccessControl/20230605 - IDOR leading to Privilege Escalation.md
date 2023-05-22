# IDOR leading to Privilege Escalation! 🪰

1. I quickly went to the password reset section
2. After entering a new password in both input fields, I captured the request.
3. The parameters were not so interesting to me, also I check them for other bugs but no success :(
4. Anyways I saw a header named “uid” which had my current email.
5. I simply created another account and replaced my email inside the “uid” header with this victim mail.
6. BOOM!! We just changed the victim’s password!!


<br>&nbsp;
## Credit
Based on [Kapil Varma](https://k4pil.medium.com/idor-leading-to-privilege-escalation-c45f4a6380a1)'s writeup.
<br>&nbsp;

## Support
You can Follow [me](https://twitter.com/MeAsHacker_HNA) on twitter or
<br><br><a href="https://www.buymeacoffee.com/NafisiAslH" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
