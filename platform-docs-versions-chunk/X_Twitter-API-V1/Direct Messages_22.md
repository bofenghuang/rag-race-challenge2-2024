platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/sending-and-receiving/api-reference/new-event

## Example Response[¶](#example-response "Permalink to this headline")

    {
    "event": {
      "type": "message_create",
      "message_create": {
        "target": {
          "recipient_id": "RECIPIENT_USER_ID"
        },
        "message_data": {
          "text": "Hello World!",
        }
      }
    }
    }

**Note**

See [media/entity](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object1) documentation for details on returned media object properties.