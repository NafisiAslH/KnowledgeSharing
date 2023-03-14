# Remote Command Execution in a Bank Server 👽

### Discovery 🔍
1. There was a functionality that user could download a PDF file<br>
2. Observe the filename and folder parameters in the request<br>
3. It was straightforward, send passwd  and /etc<br>
It's WORKED 🥳<br>
![20230317-1.png](../images/20230317-1.png)<br>
<br>&nbsp;

### Deep Dive 🔬
1. The app does not allow us to pass directory traversal payloads (‘../’, ‘%2e%2e%2f’)<br>
2. tried to get some default internal OS configuration files, but most of the files give an error.<br>
3. Looked at the passwd file again and saw an interesting 'grcdm' user.<br>
![20230317-2.png](../images/20230317-2.png)<br>
<br>&nbsp;

### Further exploration 🔦
1. I tried with ~/.bash_history payload (/home/grcdm and .bash_history)
2. I got the complete command history of user 'grcdm'
3. After analyzing all the commands, I found the web host’s root path.
![20230317-3.png](../images/20230317-3.png)<br>
<br>&nbsp;

### Analysis 🧩
1. I copied the names of all JSP pages using the Target Analyzer of the Burp Suite (Engagement Tools)
2. Configured the intruder and set the attack point to the filename parameter.
3. I found a Directory Listing. vulnerability in cr_master_invoice.jsp.
![20230317-4.png](../images/20230317-4.png)<br>
<br>&nbsp;

### Analysis 🧩
1. I passed ../../../../../../etc and saw that it listed all contents of etc directory.
2. Crawled all folders with the help of internal directory listing.
3. I saw an unlinked JSP file that was vulnerable to Unrestricted File Upload.
![20230317-5.png](../images/20230317-5.png)<br>
<br>&nbsp;

### Exploitation 💣
1. I quickly created an HTML file upload page and specified a vulnerable endpoint in the action attribute of the form tag.
2. Opened the created HTML page in the browser and selected the JSP web shell to upload.
![20230317-6.png](../images/20230317-6.png)<br>
<br>&nbsp;

## Credit
Based on [Bipin Jitiya](https://medium.com/@win3zz/remote-command-execution-in-a-bank-server-b213f9f42afe)'s writeup.
<br>&nbsp;

## Support
You can Follow [me](https://twitter.com/MeAsHacker_HNA) on twitter or
<br><br><a href="https://www.buymeacoffee.com/NafisiAslH" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
