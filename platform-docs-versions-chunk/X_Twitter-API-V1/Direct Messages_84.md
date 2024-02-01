platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/typing-indicator-and-read-receipts/api-reference/new-typing-indicator

## Webhook Event[¶](#webhook-event "Permalink to this headline")

**Coming Soon:** If using the [Account Activity API](https://developer.twitter.com/en/docs/accounts-and-users/subscribe-account-activity/overview), the following JSON payload will be sent to your webhook for all subscribed users.

    {
      "direct_message_indicate_typing_events": [
        {
          "created_timestamp":"1288834974657",
          "sender_id":"2244994945",
          "target":{
            "recipient_id":"3805104374"
          }
        }
      ],
      "users": {
        // hydrated user objects
      }
    }