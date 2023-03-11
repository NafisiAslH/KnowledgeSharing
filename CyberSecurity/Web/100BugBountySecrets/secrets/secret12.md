# Subdomain Enumeration Techniques 🔮

### 1. Certificate Transparency
- Certificate transparency logs all the entries of the issued certificates in an inventory. This includes domain names, sub-domain names, and email addresses. This is publicly available to everyone.
- CT logs search engines:<br>
[https://crt.sh/](https://crt.sh/)<br>
[https://censys.io/](https://censys.io/)<br>
[https://developers.facebook.com/tools/ct/](https://developers.facebook.com/tools/ct/)<br>
[https://google.com/transparencyreport/https/ct/](https://google.com/transparencyreport/https/ct/)<br>
[https://sslmate.com/certspotter/](https://sslmate.com/certspotter/)<br>
<br>&nbsp;

### 2. Search Engines
The “Site:” operator which was used to search domain and subdomains was working in the below-mentioned search engines:
- Google
- Bing
- Yahoo
- Yandex
- Duckduckgo
- Aol
<br>&nbsp;

### 3. Online DNS Tools
I found 9 sub-domain enumeration services:
- [https://decoder.link/](https://decoder.link/)
- [https://searchdns.netcraft.com/](https://searchdns.netcraft.com/)
- [https://dnsdumpster.com/](https://dnsdumpster.com/)
- [https://www.virustotal.com/gui/home/search](https://www.virustotal.com/gui/home/search)
- [https://pentest-tools.com/information-gathering/find-subdomains-of-domain#](https://pentest-tools.com/information-gathering/find-subdomains-of-domain#)
- [https://findsubdomains.com/](https://findsubdomains.com/)
- [https://hackertarget.com/find-dns-host-records/](https://hackertarget.com/find-dns-host-records/)
- [https://www.pkey.in/tools-i/search-subdomains](https://www.pkey.in/tools-i/search-subdomains)
- [https://spyse.com/](https://spyse.com/)
<br>&nbsp;

### 4. ASN (Autonomous System Number)
- An autonomous system number is a unique number that is given to an Autonomous system and which is assigned by IANA (Internet Assigned Numbers Authority).
- Online tools to find ASN number:<br>
[https://www.radb.net/query?](https://www.radb.net/query?)<br>
[https://bgp.he.net/](https://bgp.he.net/)<br>
[https://mxtoolbox.com/asn.aspx](https://mxtoolbox.com/asn.aspx)<br>
[https://hackertarget.com/as-ip-lookup/](https://hackertarget.com/as-ip-lookup/)<br>
[http://whois.domaintools.com/](http://whois.domaintools.com/)<br>
[https://who.is/](https://who.is/)<br>
[https://asn.cymru.com/cgi-bin/whois.cgi](https://asn.cymru.com/cgi-bin/whois.cgi)<br>
- Online tools to find IP pool from ASN number:<br>
[https://bgp.he.net/](https://bgp.he.net/)<br>
[https://mxtoolbox.com/asn.aspx](https://mxtoolbox.com/asn.aspx)<br>
[https://hackertarget.com/as-ip-lookup/](https://hackertarget.com/as-ip-lookup/)<br>
<br>&nbsp;

### 5. Subject Alternate Name (SAN)
- The multi-domain SSL certificate secures up to 250 unique domain names or subdomains and that domain/subdomains names mentioned in the Subject Alternative Names (SAN) field in the certificate.
- Tools to extract domain names from SAN:
OpenSSL<br>
[Python Script](https://github.com/appsecco/the-art-of-subdomain-enumeration/blob/master/san_subdomain_enum.py)<br>
<br>&nbsp;

### 6. Public Dataset (Rapid7)
- Rapid7 performs Internet scanning to collect Internet-wide scan data and then publish the results publicly for free and some data is paid.
- Rapid7 Datasets Link: [https://opendata.rapid7.com/](https://opendata.rapid7.com/)
<br>&nbsp;

### 7. Brute force or Dictionary Attacks
Tools:
- Aquatone
- Bluto-Old
- DNS-Discovery
- Dnssearch
- Knock
- Fierce
- Subbrute
- Amass
- Dnsrecon

### 8. Zone Transfer
- DNS zone transfer is the process of replication DNS database or DNS records from the primary name server to the secondary name server.
- The DNS zone transfer functionality used by an adversary only when the primary name server is configured to replicate the zone information to any server. An adversary acts as a slave and asks the master for a copy of the zone records.



## Credit
Based on [Lazy Hacker](https://lazyhacker.medium.com/subdomain-enumeration-tec-276da39d7e69)'s writeup.
<br>&nbsp;

## Support
You can Follow [me](https://twitter.com/MeAsHacker_HNA) on twitter or
<br><br><a href="https://www.buymeacoffee.com/NafisiAslH" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
