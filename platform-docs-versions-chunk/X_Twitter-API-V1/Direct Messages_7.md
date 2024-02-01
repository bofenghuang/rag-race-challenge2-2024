platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/sending-and-receiving/guides/message-create-object

## message\_create object

|     |     |
| --- | --- |
| message\_create.target.recipient\_id | The ID of the user receiving the message. |
| message\_create.sender\_id | The ID of the user sending the message. |
| message\_create.source\_app\_id | The ID of the application used to create the event. App details are available in the apps object in JSON payloads containing message\_create events. |
| message\_create.message\_data | A message\_data object. |

message\_data object  
## 

|     |     |
| --- | --- |
| message\_data.text | The Direct Message text. |
| message\_data.entities | A Twitter [entities](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object) object. |
| message\_data.quick\_reply\_response | A [Quick Reply](https://developer.twitter.com/en/docs/direct-messages/quick-replies/overview) response object. |
| message\_data.attachment | An [attachment](https://developer.twitter.com/en/docs/direct-messages/message-attachments/overview) object (media) |