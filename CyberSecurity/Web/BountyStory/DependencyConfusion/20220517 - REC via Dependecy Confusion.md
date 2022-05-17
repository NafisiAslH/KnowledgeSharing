# How I get RCE via Dependency Confusion 💎

### 1. Introduction
Team gave mobile app and website.</br>
We didn’t waste of time on mobile app and decided to work on website.</br>
We just tried to find Admin Panel because main domain was just a single page to download the app.
</br>&nbsp;

### 2. Recon 🔦
I started with some Shodan recon and I found a IP that belongs to TARGET.</br>
Using directory brute forcing tools like [Dirsearch](https://github.com/maurosoria/dirsearch) and [FFUF](https://github.com/ffuf/ffuf), I found a package.json file contained all the packages which was installed in the server.</br>
URL: /ui/package.json
![img](./../images/20220517-1.png)
![img](./../images/20220517-2.png)
</br>&nbsp;

### 3. Dependency Confusion 💡
Using tool called Confused, I found that “spr-svg-loaders” package was not in npm public repository.</br>
You can verify the same by going to npm website and searching for the package name.
![img](./../images/20220517-3.png)
![img](./../images/20220517-4.png)
</br>&nbsp;

### 4. I am Evil 😈
Create a malicious package with the package name and upload it to public npm repository.</br>
After publishing the package we can verify it with npm repository.</br>
The full procedure for uploading the package can be found in this [blog](https://dhiyaneshgeek.github.io/web/security/2021/09/04/dependency-confusion/).</br>
![img](./../images/20220517-5.png)
</br>&nbsp;

### 5. Bounty Time 💵
Within few hours of uploading the packages, I received ping-back with few data like hostname, directory, ipaddress, username to my interact.sh server.
</br>&nbsp;

## Credit
Based on [Sm4rty](https://systemweakness.com/rce-via-dependency-confusion-e0ed2a127013)'s write-up.
