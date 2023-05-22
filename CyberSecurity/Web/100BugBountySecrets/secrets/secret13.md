# Firing 8 Account Takeover Methods 🔥

### 1. Unicode Normalization Issue
- Victim account `victim@gmail.com`
- Create an account using Unicode
- Example: `vićtim@gmail.com`
- List of Unicode character: [https://en.wikipedia.org/wiki/List_of_Unicode_characters](https://en.wikipedia.org/wiki/List_of_Unicode_characters)
- Note: check where verification doesn’t require
<br>&nbsp;

### 2. Authorization Issue
- Change email of Account `A` and put email `B`
- Check confirmation mail in account `B`
- Open the confirmation mail from account `C`
- Taken over Account `C`
<br>&nbsp;

### 3. Reusing Reset Token
- If target allows you to reuse the reset link then hunt for more reset link via `gau`, `wayback` or `urlscan.io`
<br>&nbsp;

### 4. Pre Account Takeover
- Signup using normal signup form as a hacker but hacker has no verification link.
- Then if victim signs up using oauth .
- Verification bypass now attacker can login the victim account without verification link with the password he entered while registering.
<br>&nbsp;

### 5. CORS Misconfiguration to Account Takeover
- Check api , any endpoint has access access token/session/secret/fingerprint
- If yes check for CORS misconfiguration does it allow us to fetch data from target?
- Make a payload to fetch data and replace headers and boom
<br>&nbsp;

### 6. CSRF to Account Takeover
- If profile modification in cookie based authentication doesn’t generate any token
- Open Account `A` change&Put email that you own click save intercept the request and generate a csrf poc.
- If fully cookie based auth then you dont have to modify anything send the csrf file to victim.
- If it requires UUID/UserID or unique token it becomes hard to do that but that doesn't mean it is secure , just start playing with target
- hint: password reset page helps many times for UUID/GUID and UserID
<br>&nbsp;

### 7. Host Header Injection
- Well in this case there are 4 ways do that.
- Click reset password change `host` header.
- Or change proxy header ex: `X-Forwarded-For: attacker.com`
- Or change `host`, `referrer`, `origin` headers at once as `attacker.com`
- Click reset then click resend mail and do all 3 methods above
<br>&nbsp;

### 8. Response Manipulation
1. code manipulation * to `200 OK`
2. code and body manipulation
code * to `200 OK`
body * to `{"success":true}` or `{}`
it works when json is being used to transfer and receive data.
<br>&nbsp;

## Credit
Based on [0xMaruf](https://infosecwriteups.com/firing-8-account-takeover-methods-77e892099050)'s writeup.
<br>&nbsp;

## Support
You can Follow [me](https://twitter.com/MeAsHacker_HNA) on twitter or
<br><br><a href="https://www.buymeacoffee.com/NafisiAslH" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
