# IDOR - General Identification

### Description
details
</br>&nbsp;

## Sub Techniques
### 1. Easy Change
```
user_id=other_user_id
```
</br>&nbsp;

### 2. Parameter Pollution
- See [Trick - Parameter Pollution](https://github.com/NafisiAslH/WebPenTestMethodology/blob/main/Resources/Trick%20-%20Parameter%20Pollution.md)</br>
</br>&nbsp;

### 3. Change Request Method
- See [Trick - Parameter Pollution](https://github.com/NafisiAslH/WebPenTestMethodology/blob/main/Resources/Trick%20-%20Change%20Request%20Method.md)</br>
</br>&nbsp;

### 4. No ID, No Worry 
```
/ngprofile/aggregate/self/fullProfile → /ngprofile/aggregate/31337/fullProfile 
/ngprofile/aggregate/self/fullProfile → /ngprofile/aggregate/self/../31337/fullProfile 
```
</br>&nbsp;

### 5. Don’t Ignore Encoded & Hashed IDs 
```
try creating a few accounts to analyze how these IDs are created 
```
</br>&nbsp;

### 6. IDOR in GraphQL 
```
details
```
</br>&nbsp;

## References:
[Reference](https://www.aon.com/cyber-solutions/aon_cyber_labs/finding-more-idors-tips-and-tricks/)</br>
[Reference](https://16521092.medium.com/some-ways-to-find-more-idor-da16c93954e5 )</br>


<br>&nbsp;
## Support
You can Follow [me](https://twitter.com/MeAsHacker_HNA) on twitter or
<br><br><a href="https://www.buymeacoffee.com/NafisiAslH" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
