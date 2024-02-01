platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/sending-and-receiving/api-reference/new-event


## Message Data Object[¶](#message-data-object "Permalink to this headline")

|     |     |
| --- | --- |
| **text** (required) | The text of your Direct Message. URL encode as necessary. Max length of 10,000 characters. Max length of 9,990 characters if used as a [Welcome Message](https://developer.twitter.com/en/docs/direct-messages/welcome-messages/api-reference/new-welcome-message). |
| **quick\_reply.type** (optional) | The Quick Reply type to present to the user (example requests below):<br><br>* **options** - Array of `Options` objects (20 max). |
| **attachment.type** (optional) | The attachment type. Can be media or location. |
| **attachment.media.id** (optional) | A media id to associate with the message. A Direct Message may only reference a single media\_id. See [Uploading Media](https://developer.twitter.com/en/docs/direct-messages/message-attachments/guides/attaching-media) for further details on uploading media. |

**Note**

See [Attaching Media to Direct Messages](https://developer.twitter.com/en/docs/direct-messages/message-attachments/guides/attaching-media) for details on including an image, GIF or video in Direct Messages.