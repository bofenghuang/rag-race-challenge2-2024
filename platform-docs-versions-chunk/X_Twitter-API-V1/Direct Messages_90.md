platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/conversation-management/guides/source-app

## source\_app object

|     |     |
| --- | --- |
| id  | The ID of the Twitter app used by the authenticating user to send the DM. |
| name | The name of the Twitter app used by the authenticating user to send the DM. |
| url | The URL of the Twitter app used by the authenticating user to send the DM. |

## Example for GET direct\_messages/events/list

      `{   "event": {     "type": "message_create",     "id": "854103000570187779",     "created_timestamp": "1492468998459",     "message_create": {       "target": {         "recipient_id": "3340250004"       },       "sender_id": "51378538",       "source_app_id": "268278",       "message_data": {         "text": "Hello",         "entities": {           "hashtags": [],           "symbols": [],           "user_mentions": [],           "urls": []         }       }     }   }   "apps": {     "268278": {       "id": "268278",       "name": "Twitter Web Client",       "url": "http://twitter.com"     }   } }`