# Unauthorized access via Leaked Credentials ⚽️

1. After subdomains enumeration, I started fuzzing the directories and finally arrived at a specific path.
2. When I opened the desired path, a message was displayed requiring a username and password to access this path.
3. I started searching Google and the Wayback Machine and GitHub and all the indexes, but I couldn’t find anything that pointed directly to this particular path.
4. I opened the directory in the out-of-scope domains. for one of them, my [Wayback Machine Extension](https://chrome.google.com/webstore/detail/wayback-machine/fpnmgdkabkmnadcjpehmlllkndpkmiak) was activated and some archived paths were detected.
5. I opened the archived paths and found a few usernames, passwords, and specific endpoints.
6. I replaced them in the subdomain in scope and one of them worked correctly and I got access to the admin panel.
<br>Now I’m In.

<br>&nbsp;
## Credit
Based on [M7arm4nr](https://infosecwriteups.com/unauthorized-access-to-the-admin-panel-via-leaked-credentials-on-the-waybackmachine-55c3307141c6)'s writeup.
<br>&nbsp;

## Support
You can Follow [me](https://twitter.com/MeAsHacker_HNA) on twitter or
<br><br><a href="https://www.buymeacoffee.com/NafisiAslH" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
