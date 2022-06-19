# Mass Account Takeovers using HTTP Request Smuggling 👻

### 1. Find Vulnerability🔍 
slackb.com was vulnerable to HTTP Request Smuggling.</br>
You can use [smuggler](https://github.com/defparam/smuggler) to find this vulnerability.</br>
![img](./../images/20220620-1.png)
</br>&nbsp;

### 2. Prepare Hook 🪝
Attacker exploited HTTP Request Smuggling bug to perform hijack onto neighboring user requests.</br>
Attacker send following request:
![img](./../images/20220620-2.png)
</br>&nbsp;

### 3. Victim Comes in 🚶🏻
Suppose victim send following request:
![img](./../images/20220620-3.png)
</br>&nbsp;

### 4. Weird Deal 🪄
victim's request will be appended to attacker's request and will turn into following request.</br>
This hijack forward victim onto attacker's server with slack domain cookies.
![img](./../images/20220620-4.png)
</br>&nbsp;

### 5. Attacker Becomes King 👑
User' secret session will be sent to attacker.</br>
With this attacker will be able to prove session takeover against arbitrary users.</br>
Slack reward $6500 for this bug.
![img](./../images/20220620-5.png)
</br>&nbsp;

### 6. Whole Attack Scenario 👁️
![img](./../images/20220620-6.png)
</br>&nbsp;

## Credit
Based on [defparam](https://hackerone.com/reports/737140)'s report.
</br>&nbsp;

## Support
You can Follow [me](https://twitter.com/MeAsHacker_HNA) on twitter or buy me a [Coffee](https://buymeacoffee.com/NafisiAslH)
