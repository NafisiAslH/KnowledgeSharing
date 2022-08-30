# How I Account Takeover via XSS 💡

### 1. Found XSS
- found login page in /account/?jid=77877
- `jid` parameter has no validation
![20220830-1.png](../../images/20220830-1.png)
<br>&nbsp;

### 2. Escalate it to account takeover
![20220830-2.png](../../images/20220830-2.png)
<br>&nbsp;

### 3. Get user & pass
- Used Burb Collaborator
![20220830-3.png](../../images/20220830-3.png)
<br>&nbsp;

## Credit
Based on [Mohamed Tarek](https://medium.com/@mohamedtarekq/how-i-get-full-account-takeover-via-stealing-actions-login-form-xss-9e50068c2b2d)'s write-up.
</br>&nbsp;

## Support
You can Follow [me](https://twitter.com/MeAsHacker_HNA) on twitter or
<br><br><a href="https://www.buymeacoffee.com/NafisiAslH" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
