platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/migration/us-ss-migration-guide

### Summary of changes

The Account Activity API will deliver you events for authenticated and subscribed accounts via webhooks as opposed to a streaming connection like with User Streams and Site Streams.

#### Deprecated APIs

GET user  
  
GET site  (including control streams: GET site/c/:stream\_id,  GET site/c/:stream\_id/info.json,  GET site/c/:stream\_id/friends/ids.json,  POST site/c/:stream\_id/add\_user.json,  POST /site/c/:stream\_id/remove\_user.json)

#### Replacement APIs

[Enterprise Account Activity API - All Activities](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise)

[Premium Account Activity API - All Activities](https://developer.twitter.com/en/docs/twitter-api/premium/account-activity-api/api-reference/aaa-premium)