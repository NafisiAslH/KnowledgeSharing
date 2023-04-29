# How to use Burp Suite Like a PRO?
Burp Suite is a powerful tool for web application security testing and one of the most popular tools in the industry.<br>
By the end of this article, you will have a better understanding of how to leverage Burp Suite’s features to improve your web application security testing skills and find critical vulnerabilities that may have been overlooked.<br>
Let’s get started!
<br>&nbsp;

## 1. Perform Scans only to specific endpoints
- Capture the request and submit it to the Intruder tab to accomplish this.
- Manually pick the endpoints to be scanned, then, to customise the scan type, right-click and select ```Scan defined insertion points```.
- This boosts productivity while enabling you to scan a specific endpoint.
<img width="1065" alt="Screenshot 2023-04-29 at 12 53 04 PM" src="https://user-images.githubusercontent.com/97911162/235295341-df207f3e-d7ff-4c82-8e2b-346945497583.png">
<br>&nbsp;

## 2. Difference between Copy URLs and Copy links
- ```Copy URLs``` in this Host copy all the links found in the target, including links referencing third-party sites that are not in scope.
- ```Copy links``` in these URLs copy only the in-scope URLs.
<img width="571" alt="Screenshot 2023-04-29 at 12 58 14 PM" src="https://user-images.githubusercontent.com/97911162/235295581-81156bc4-309d-4c49-901a-68ac183be974.png">
<br>&nbsp;

## 3. Perform Directory fuzzing in Burp suite
- Select the target domain from the Target tab and right-click to access ```Engagement Tools > Discover Content```.
- You’ll now see a new popup with the directory fuzzing configuration. You can use your preferred wordlists.
<img width="1133" alt="Screenshot 2023-04-29 at 1 03 50 PM" src="https://user-images.githubusercontent.com/97911162/235295793-4585d322-f688-4050-bcfb-9c9b6e5952a8.png">
<img width="906" alt="Screenshot 2023-04-29 at 1 03 20 PM" src="https://user-images.githubusercontent.com/97911162/235295795-809cf00a-5b11-469a-b443-03168048a390.png">
<br>&nbsp;

## 4. Automatically Backup Burp projects
- Burp provides the option to save projects at predefined intervals.
- Go to ```User Options > Misc``` and look for the option ```Automatic Project Backup```.
<img width="1181" alt="Screenshot 2023-04-29 at 1 05 56 PM" src="https://user-images.githubusercontent.com/97911162/235295892-cd36a230-2d7f-4b09-92f4-e0bb0a831065.png">
<br>&nbsp;

## 5. Set Custom Burp Suite Keyboard Shortcuts
- Burp Suite offers a set of keyboard shortcuts that can be used to make it easier while testing.
- Navigate to ```User Options > Misc``` and select ```Hotkeys```.
<img width="1507" alt="Screenshot 2023-04-29 at 1 08 47 PM" src="https://user-images.githubusercontent.com/97911162/235296097-eebe0e9e-d89c-4dc3-90e9-e3a416cdc4d3.png">
<br>&nbsp;

## 6. Schedule Burp Suite Tasks
- Burp Suite provides users to schedule the task.
- Go to ```Project Options > Misc``` and look for the ```Scheduled Tasks``` option.
<img width="966" alt="Screenshot 2023-04-29 at 1 12 34 PM" src="https://user-images.githubusercontent.com/97911162/235296185-4d4aa29f-0441-4a1f-b6ea-80a85d2f10df.png">
- On the next screen, click Add and you’ll be given two options. To either pause or resume a task.
<img width="1380" alt="Screenshot 2023-04-29 at 1 13 30 PM" src="https://user-images.githubusercontent.com/97911162/235296231-12f124af-8672-4662-bac7-b8e074ce5eb1.png">
<br>&nbsp;

## 7. Issue Definitions
- Most of us browse the web for the vulnerability description, impact, and references for reporting the vulnerabilities.
- Burp Suite has this by default, and this can be found under ```Target > Issue Definitions```.
<img width="1505" alt="Screenshot 2023-04-29 at 2 07 40 PM" src="https://user-images.githubusercontent.com/97911162/235298385-3b27ecfe-f384-4cd4-af4b-ab6b71ec9e48.png">
<br>&nbsp;

## 8. Burp Configuration Library
- Burp Suite has a wide range of scan configurations, such as critical issues only, extensions only, and so on.
- Navigate to Burp > Configuration Library, and you’ll be presented with scan options on the next screen.
- Click the New button to begin creating scan configurations.
- By default, Burp Suite has plenty of default scan configurations. Select the configuration you need and create a scan profile.
<img width="697" alt="Screenshot 2023-04-29 at 1 20 56 PM" src="https://user-images.githubusercontent.com/97911162/235296534-0d1d9fa6-ffd2-4f30-8ab8-56bc4448e527.png">
- When the scan configuration is finished, give it a name and save it. Then, from the Dashboard, select New Scan to use the custom configuration.
- In the next popup screen, select the Select from library option, then locate and select the newly created scan configuration.
<img width="995" alt="Screenshot 2023-04-29 at 1 21 32 PM" src="https://user-images.githubusercontent.com/97911162/235296551-144b66f0-ca72-4eef-8861-9cc0276960e1.png">
<br>&nbsp;

## 9. Check if the default Collaborator server is working
- Burp Collaborator is a network service used by Burp Suite to assist in the discovery of vulnerabilities via an external service.
- To check this, go to ```Project Options > Misc``` and click the Run health check button.
<img width="835" alt="Screenshot 2023-04-29 at 2 00 30 PM" src="https://user-images.githubusercontent.com/97911162/235298128-a7cf5b10-9380-48b3-9eb1-5737ba2f6b63.png">
<br>&nbsp;

## 10. Simulate Manual Testing
- Navigate to the Target tab and select the domain for which you want to perform simulation testing.
- Then, under Engagement Tools, select ```Simulate Manual Testing```.
<img width="728" alt="Screenshot 2023-04-29 at 2 02 25 PM" src="https://user-images.githubusercontent.com/97911162/235298202-d451d0e3-c985-4ed7-bea6-dfe8ec11211a.png">
<br>&nbsp;

## Credit
Based on [N.I.M](https://medium.com/@nimmughal799/how-to-use-burp-suite-like-a-pro-20092412ed37)'s writeup.
<br>&nbsp;

## Support
You can Follow [me](https://twitter.com/MeAsHacker_HNA) on twitter or
<br><br><a href="https://www.buymeacoffee.com/NafisiAslH" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
