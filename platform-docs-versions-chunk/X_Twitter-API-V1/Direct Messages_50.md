platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/welcome-messages/api-reference/new-welcome-message

## Welcome Message Object[¶](#welcome-message-object "Permalink to this headline")

|     |     |
| --- | --- |
| **message\_data** (required) | The `Message Data Object` defining the content of the message template. See [POST direct\_messages/events/new (message\_create)](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/new-event) for Message Data object details. |
| **name** (optional) | A human readable name for the Welcome Message. This is not displayed to the user. Max length of 100 alpha numeric characters including hyphens, underscores, spaces, hashes and at signs. |

> **Note**
> 
> See [Attaching Media to Direct Messages](https://developer.twitter.com/en/docs/direct-messages/message-attachments/guides/attaching-media) for details on including an image, GIF or video in Direct Messages.