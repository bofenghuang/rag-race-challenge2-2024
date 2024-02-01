platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/sending-and-receiving/guides/direct-message-migration


### Summary of changes

If you are still using the following DM endpoints, you will have to migrate to the newer endpoints. 

| Deprecated endpoint | New migration alternative |
| --- | --- |
| [POST direct\_messages/new](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/new-message) | [POST direct\_messages/events/new](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/new-event) |
| [GET direct\_messages/show](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/get-message) | [GET direct\_messages/events/show](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/get-event) |
| [GET direct\_messages](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/get-messages) | [GET direct\_messages/events/list](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/list-events) |
| [GET direct\_messages/sent](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/get-sent-message) | [GET direct\_messages/events/list](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/list-events) |
| [POST direct\_messages/destroy](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/delete-message) | [DELETE direct\_messages/events/destroy](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/delete-message-event "GET direct_messages/events/list") |