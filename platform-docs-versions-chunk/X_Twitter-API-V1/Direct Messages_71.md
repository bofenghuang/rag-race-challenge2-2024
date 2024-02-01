platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/quick-replies/api-reference/options

## Example User Response[¶](#example-user-response "Permalink to this headline")

The `type` and `metadata` will be present in the `quick_reply_response` object. The `label` for the chosen option is sent as the message `text`.

    {
      "event": {
        "type": "message_create",
        "id": "1234858592",
        "created_timestamp": "1392078023603",
        "message_create": {
          "target": {
            "recipient_id": "1234858592"
          },
          "sender_id": "3805104374",
          "message_data": {
            "text": "Blue Bird",
            "entities": {
              "hashtags": [],
              "symbols": [],
              "urls": [],
              "user_mentions": []
            },
            "quick_reply_response": {
              "type": "options",
              "metadata": "external_id_2"
            }
          }
        }
      }
    }