platform: X
topic: Twitter-API-Enterprise
subtopic: Compliance Firehose API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Compliance Firehose API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/compliance-firehose-api/guides/honoring-user-intent

### Status

| Action | Description |
| --- | --- |
| Delete Status | A Twitter user can delete a status at any point in time. Deleted statuses cannot be reversed and are permanently deleted. |
| Withhold Status | Twitter retains the right to reactively withhold access to certain content in a specific country from time to time. A withheld status can only be made unwithheld by Twitter.   <br>For more information, see [Country Withheld Content](https://support.twitter.com/articles/20169222-country-withheld-content). |

### Keeping Track of User and Status Changes

The state of a User or Status can change at any time due to one of the actions above, and this impacts how consumers of Twitter data are expected to treat the availability and privacy of all associated content. When these actions happen, a corresponding compliance message is sent that indicates that the state of a Status or User has changed.