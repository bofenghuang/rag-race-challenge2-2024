platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/sending-and-receiving/api-reference/new-event

## Event Object[¶](#event-object "Permalink to this headline")

|     |     |
| --- | --- |
| **type** (required) | The type of event you are posting. For Direct Messages, use `message_create` |
| **message\_create.target.recipient\_id** (required) | The ID of the user who should receive the direct message. |
| **message\_create.message\_data** (required) | The `Message Data Object` defining the content to deliver to the reciepient. |