platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/conversation-management/guides/initiated-via

## Example Direct Message Event

The following Direct Message event was preceded by a Direct Message prompt from a Tweet or a Welcome Message was presented to the user.  

      `{   "type": "message_create",   "id": "1234858592",   "created_timestamp": "1392078023603",   "initiated_via": {     "tweet_id": "123456",     "welcome_message_id": "456789"   },   "message_create": {     "target": {       "recipient_id": "1234858592"     },     "sender_id": "3805104374",     "source_app_id": "268278",     "message_data": {       "text": "Blue Bird",       "entities": {         "hashtags": [],         "symbols": [],         "urls": [],         "user_mentions": [],       },       "quick_reply_response": {         "type": "options",         "metadata": "external_id_2"       },       "attachment": {         "type": "media",         "media": {          ...         }       }     }   } }`