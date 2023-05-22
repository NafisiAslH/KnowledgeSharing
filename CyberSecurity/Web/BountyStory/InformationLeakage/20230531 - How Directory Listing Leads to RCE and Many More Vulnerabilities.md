# How Recon Leads to RCE and Many More Vulnerabilities 🩻

1. I started with basic subdomain enumeration using tools
```
$ subfinder -d redacted.com -o subfinder.txt
$ amass enum -d --passive redacted.com -o amass.txt
$ echo redacted.com | assetfinder --subs-only | tee assetfinder.txt
$ cat subfinder.txt amass.txt assetfinder.txt | sort -u | anew subdomains.txt
$ cat subdomains.txt | alterx | anew subd.txt
```
2. Now, its time to resolve the subdomains and check how many of them are alive or having status code 200.
```
$ cat subd.txt | httpx -mc 200 | tee live.txt
```
3. I found that subdomain’s endpoint /teamlevelis hosting the information of all its employees in a hierarchy format. 
4. I found that the subdomain itself leaking the PII data of its employees.
5. I started fuzzing the subdomain and found an interesting endpoint /hrms which is asking for the employee’s email address to login/authorize.
6. I entered an email ID and without any password or OTP, I logged into their dashboard and was allowed to change the data available on it.
7. I started playing with input boxes and first thing I tried inputting a XSS payload <img src=x onerror=prompt()>in all froms and submit it. and BOOM
8. I logged into the dashboard and found file upload functionality. I have tried to upload a php file and BOOM

<br>&nbsp;
## Credit
Based on [Shrirang Diwakar](https://shrirangdiwakar.medium.com/bypassing-403s-like-a-pro-2-100-broken-access-control-66beef4afa8c)'s writeup.
<br>&nbsp;

## Support
You can Follow [me](https://twitter.com/MeAsHacker_HNA) on twitter or
<br><br><a href="https://www.buymeacoffee.com/NafisiAslH" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
