platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/message-attachments/guides/attaching-media

### 2\. Send Direct Message with media attachment

* Define an attachment object in the message\_data object in the Direct Message event json body.
* Set attachment type property to media.
* Set the media.id property to the media ID returned in the previous chunk upload process.  
     

#### Parameters

|     |     |
| --- | --- |
| **attachment.type  <br>**(required) | Must be set to media. |
| **attachment.media.id  <br>**(required) | A media ID to associate with the message. A Direct Message may only reference a single media id. |

See [POST direct\_messages/events/new](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/new-event.html) documentation for all parameters and full details.