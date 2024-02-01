platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/migration/us-ss-migration-guide

### Deprecated streaming message types 

|     |     |
| --- | --- |
| Blank lines | Blank lines will no longer be delivered in the Account Activity API as they were used as keep-alive messages in User Streams and Site Streams. |
| Limit notices | Limit notices will no longer be sent to a given webhook.  Instead, users can call the API to get current usage of available handles. This will be included in the developer portal at some time in the future. |
| Disconnect messages | Disconnect notices will no longer be necessary as webhooks do not rely on an active connection. |
| Stall warnings | Stall warnings will no longer be necessary as webhooks do not rely on an active connection being able to handle large numbers of incoming messages. |
| Friends list | Friends lists will no longer be sent proactively. There will now be a REST endpoint to get this information. |