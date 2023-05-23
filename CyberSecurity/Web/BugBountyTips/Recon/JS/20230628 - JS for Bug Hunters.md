# JS for Bug Hunters 🛹

### Items You Should Be Searching For:
1. New Endpoints:
2. New Parameters
3. Hidden Features
4. API Keys
5. Developer Comments
```
cat *js | grep -r -E "aws_access_key|aws_secret_key|api key|passwd|pwd|heroku|slack|firebase|swagger|aws_secret_key|aws key|password|ftp password|jdbc|db|sql|secret jet|config|admin|pwd|json|gcp|htaccess|.env|ssh key|.git|access key|secret token|oauth_token|oauth_token_secret" /path/to/directory/*.js
```

### How to Extract JS File:
1. Discover subdomains 
2. Find live subdomains
3. Retrieves historical URLs
4. Filter URLs that contain ".js" 
```
subfinder -d domain.com | httpx -mc 200 | tee subdomains.txt && cat subdomains.txt | waybackurls | httpx -mc 200 | grep .js | tee js.txt
```

### Use Nuclei Exposures Tag
```
nuclei -l js.txt -t ~/nuclei-templates/exposures/ -o js_exposures_results.txt
```

<br>&nbsp;
## Credit
Based on [Shrirang Diwakar](https://shrirangdiwakar.medium.com/bypassing-403s-like-a-pro-2-100-broken-access-control-66beef4afa8c)'s writeup.
<br>&nbsp;

## Support
You can Follow [me](https://twitter.com/MeAsHacker_HNA) on twitter or
<br><br><a href="https://www.buymeacoffee.com/NafisiAslH" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
