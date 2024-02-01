platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/sending-and-receiving/overview

## 

To send a new Direct Message use [POST direct\_messages/events/new (message\_create)](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/new-event). Optionally, you may also attach [Quick Replies](https://developer.twitter.com/en/docs/direct-messages/quick-replies) or [media](https://developer.twitter.com/en/docs/direct-messages/message-attachments/guides/attaching-media) (image, GIF or video).

## Receiving messages events

* You can retrieve Direct Messages from up to the past 30 days with [GET direct\_messages/events/list](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/list-events).
* Consuming Direct Messages in real-time can be accomplished via webhooks with the [Account Activity API](https://developer.twitter.com/en/docs/accounts-and-users/subscribe-account-activity/overview).