platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/sending-and-receiving/guides/direct-message-migration


### Differences & migration considerations

The new API endpoints behave very differently from their previous counterparts. Simply updating the endpoint URLs will result in errors in your application. Consider the following when updating your application for the migration.

#### New Direct Message object

The first thing you are likely to notice is the new object structure of Direct Messages. This new Message Create object structure has been introduced to support new capabilities like [Quick Replies](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/quick-replies) and [Attachments](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/message-attachments). The new object also contains a smaller condensed user object. Your application will need to be updated to account for this new object structure when parsing and potentially in data models or storage. For descriptions of each property see the [full documentation on the Message Create Object](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/guides/message-create-object).  

**Example message create object**  

    {
      "type": "message_create",
      "id": "1234858592",
      "created_timestamp": "1392078023603",
      "initiated_via": {
        "tweet_id": "123456",
        "welcome_message_id": "456789"
      },
      "message_create": {
        "target": {
          "recipient_id": "1234858592"
        },
        "sender_id": "3805104374",
        "source_app_id": "268278",
        "message_data": {
          "text": "Blue Bird",
          "entities": {
            "hashtags": [],
            "symbols": [],
            "urls": [],
            "user_mentions": [],
          },
          "quick_reply_response": {
            "type": "options",
            "metadata": "external_id_2"
          },
          "attachment": {
            "type": "media",
            "media": {
             ...
            }
          }
        }
      }

#### Summary

* Entirely new Direct Message object structure.
* Condensed user object.
* New information provided (quick reply responses, attachments, etc).