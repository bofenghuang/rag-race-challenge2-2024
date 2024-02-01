platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/sending-and-receiving/guides/message-create-object

## Top level event object

|     |     |
| --- | --- |
| Property | Description |
| type | The type of event. For Direct Messages type will be message\_create. |
| id  | The ID of the direct message event. |
| created\_timestamp | Epoch timestamp of when the Direct Message event was created. |
| initiated\_via.tweet\_id | The ID of the Tweet with Direct Message Prompt the conversation was initiated from if one was used. |
| initiated\_via.welcome\_message\_id | The ID of the Welcome Message immediatley preceding the conversation if one was used. |