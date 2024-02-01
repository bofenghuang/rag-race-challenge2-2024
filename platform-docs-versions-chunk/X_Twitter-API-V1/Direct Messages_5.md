platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/sending-and-receiving/guides/message-create-object


# Message Create Object

Direct Message Event objects are returned by [GET direct\_messages/events/list](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/list-events), [GET direct\_messages/events/show](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/get-event) and can be consumed in real-time using the [Account Activity API](https://developer.twitter.com/en/docs/accounts-and-users/subscribe-account-activity/overview). Direct Messages have the type of message\_create.

      `{   "type": "message_create",   "id": "1234858592",   "created_timestamp": "1392078023603",   "initiated_via": {     "tweet_id": "123456",     "welcome_message_id": "456789"   },   "message_create": {     "target": {       "recipient_id": "1234858592"     },     "sender_id": "3805104374",     "source_app_id": "268278",     "message_data": {       "text": "Blue Bird",       "entities": {         "hashtags": [],         "symbols": [],         "urls": [],         "user_mentions": [],       },       "quick_reply_response": {         "type": "options",         "metadata": "external_id_2"       },       "attachment": {         "type": "media",         "media": {          ...         }       }     }   } }`