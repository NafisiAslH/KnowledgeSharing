# From Django Debug Mode to PII Data Leak of 500 Employees
<br>&nbsp;

### Recon
1. I started with basic subdomain enumeration using tools such as Subfinder, Amass, Assetfinder and Alterx
```
$ subfinder -d redacted.com -o subfinder.txt
$ amass enum -d --passive redacted.com -o amass.txt
$ echo redacted.com | assetfinder --subs-only | tee assetfinder.txt
$ cat subfinder.txt amass.txt assetfinder.txt | sort -u | anew subdomains.txt
$ cat subdomains.txt | alterx | anew subd.txt
```

2. Now, its time to resolve the subdomains and check how many of them are alive or having status code 200. I used httpx and then saved the output in a file say live.txt.
```
$ cat subd.txt | httpx -mc 200 | tee live.txt
```

3. I have used naabu for port-scanning.
```
$ cat subd.txt | naabu -top-ports 1000 -o port-scan.txt
```

4. For the subdomain 3ntern1l.redacted.com, I found two open ports 8443 and 443.

<br>&nbsp;
### Working with the Subdomain
- On the port 8443, I found Django Debug mode Enabled by just adding a random string at the end of the URL
<img width="939" alt="Screenshot 2023-04-29 at 2 41 06 PM" src="https://user-images.githubusercontent.com/97911162/235299606-4c412d0a-2dbb-40b3-9784-0a95f1d9b206.png"><br>
- Using the Swagger endpoint, I was successfully able to access the Swagger UI Dashboard.
- I was not able to access the API endpoints as they require the authorization token
- I know that subdomain is also running on port 443. I navigated to port 443 and found a Login as well as Sign Up page. I immediately signed up and accessed the dashboard.
- I found that subdomain is using the same API endpoints of which Swagger UI Dashboard was available to me. In the burp-request, I also found the JWT Token.
- I immediately copied the JWT token and pasted on the Swagger UI Dashboard. I was successfully able to access the API endpoints available on the dashboard.
- I found 2–3 endpoints requires only an id input from the user. I start playing with those endpoints and found that with a change of id💥
<h3>The data exposed includes the PII data such as first name, last name, professional email address, phone number, etc of more than 500+ employees registered on the subdomain.<h3>

<br>&nbsp;
## Credit
Based on [Aayush Vishnoi](https://medium.com/@ar_hawk/from-django-debug-mode-to-pii-data-leak-of-more-than-500-employees-due-broken-access-control-and-a3eb602a4207)'s report.
<br>&nbsp;

## Support
You can Follow [me](https://twitter.com/MeAsHacker_HNA) on twitter or
<br><br><a href="https://www.buymeacoffee.com/NafisiAslH" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
