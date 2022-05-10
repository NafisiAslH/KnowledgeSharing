# Most Known Vendors Default Credentials
One place for all the default credentials to assist the pentesters during an engagement, this document has a several products default credentials that are gathered from several sources.
</br>&nbsp;

## Motivation
- One document for the most known vendors default credentials
- Assist pentesters during a pentest/red teaming engagement
- **Helping the Red/Blue teamers to secure the company infrastructure by discovering this security flaw in order to mitigate it**. See 
[WSTG-ATHN-02](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/02-Testing_for_Default_Credentials "OWASP Guide")
</br>&nbsp;

## Sources
- [Changeme](https://github.com/ztgrace/changeme "Changeme project")
- [Routersploit]( https://github.com/threat9/routersploit "Routersploit project")
- [betterdefaultpasslist]( https://github.com/govolution/betterdefaultpasslist "betterdefaultpasslist")
- [Seclists]( https://github.com/danielmiessler/SecLists/tree/master/Passwords/Default-Credentials "Seclist project")
- [ics-default-passwords](https://github.com/arnaudsoullie/ics-default-passwords) (thanks to @noraj)
- Vendors documentations/blogs
</br>&nbsp;

## Creds script

You can turn the cheat sheet into a cli command and perform search queries for a specific product.

```bash
# Usage
➤ python3 creds.py search tomcat                                                                                                      
+----------------------------------+------------+------------+
| Product                          |  username  |  password  |
+----------------------------------+------------+------------+
| apache tomcat (web)              |   tomcat   |   tomcat   |
| apache tomcat (web)              |   admin    |   admin    |
...
+----------------------------------+------------+------------+
```
</br>&nbsp;

## Credit
Based on [ihebski](https://github.com/ihebski/DefaultCreds-cheat-sheet)'s github page.</br>
