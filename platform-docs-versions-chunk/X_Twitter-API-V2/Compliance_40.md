platform: X
topic: Twitter-API-V2
subtopic: Compliance
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Compliance.md
url: https://developer.twitter.com/en/docs/twitter-api/compliance/streams/integrate/honoring-user-intent

### Tweet

| Action | Description |
| --- | --- |
| Delete Tweet | A Twitter user can delete a Tweet at any point in time. Deleted Tweets cannot be reversed and are permanently deleted. |
| Withhold Tweet | Twitter retains the right to reactively withhold access to certain content in a specific country from time to time. A withheld Tweet can only be made unwithheld by Twitter.   <br>For more information, see [Country Withheld Content](https://support.twitter.com/articles/20169222-country-withheld-content). |

### Keeping Track of User and Tweet Changes

The state of a User or Tweet can change at any time due to one of the actions above, and this impacts how consumers of Twitter data are expected to treat the availability and privacy of all associated content. When these actions happen, a corresponding compliance message is sent that indicates that the state of a Tweet or User has changed.