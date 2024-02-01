platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise

### Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response Format | JSON |
| Requires Authentication | Yes (user context - all consumer and access tokens) |
| Rate Limited | Yes |
| Requests / 15-min window (user auth) | 15  |
| Support for Tweet edits | All Tweet objects will include Tweet edit metadata describing the Tweet's edit history. See the ["Tweet edits" fundamentals](https://developer.twitter.com/en/docs/twitter-api/enterprise/tweet-edits) page for more details. |

### Parameters[¶](#parameters "Permalink to this headline")

|     |     |
| --- | --- |
| url (required) | Encoded URL for the callback endpoint. |