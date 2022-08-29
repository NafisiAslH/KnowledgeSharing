# How to find Origin IP Automatically 🔭
&nbsp;


### 1. Censys
```
censys search hackerone.com
censys search hackerone.com | grep “ip” | egrep -v “description” | cut -d “:” -f2 | tr -d \”\, | httpx
```
![secret10-1.png](../images/secret10-1.png)
![secret10-2.png](../images/secret10-2.png)
&nbsp;

### 2. Shodan
```
shodan search Ssl.cert.subject.CN:”hackerone.com” 200 — fields ip_str | httpx
```
![secret10-3.png](../images/secret10-3.png)
&nbsp;

### 3. Uncover
- [uncover](https://github.com/projectdiscovery/uncover) is a go wrapper using APIs of well known search engines to quickly discover exposed hosts on the internet.
```
uncover -q “hackerone.com” -e censys,fofa,shodan,shodan-idb | httpx
```
![secret10-4.png](../images/secret10-4.png)
&nbsp;

### 4. Favicon Hashes
- Python script for generating the hash
```
import mmh3
import requests
import codecs

response = requests.get('https://<website>/<favicon path>')
favicon = codecs.encode(response.content, 'base64')
hash = mmh3.hash(favicon)
print(hash)
```
- Using [Fav-Up](https://github.com/pielco11/fav-up) tool you can look up for real IP<br>
![secret10-5.png](../images/secret10-5.png)<br>
- Using [LiLi](https://github.com/Dheerajmadhukar/Lilly/blob/main/README.md) tool you can look up for real IP<br>
![secret10-8.png](../images/secret10-8.png)<br>
&nbsp;

### 5. SecurityTrails
- You can explore complete current and historical data for any internet assets.
![secret10-6.png](../images/secret10-6.png)
&nbsp;

### 6. DNS Records
```
dig udemy.com A
dig udemy.com MX
```
![secret10-7.png](../images/secret10-7.png)
&nbsp;

## Credit
Based on [பூபதி S.](https://medium.com/@bobby.S/how-to-find-origin-ip-1f684f459942)'s writeup
Based on [HolyBugx](https://infosecwriteups.com/finding-the-origin-ip-behind-cdns-37cd18d5275)'s writeup
</br>&nbsp;

## Support
You can Follow [me](https://twitter.com/MeAsHacker_HNA) on twitter or
<br><br><a href="https://www.buymeacoffee.com/NafisiAslH" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
