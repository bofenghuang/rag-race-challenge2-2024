platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/message-attachments/guides/attaching-location

Attaching location

# Attaching location

Locations can be attached to Direct Messages created with [POST direct\_messages/events/new](https://dev.twitter.com/rest/reference/post/direct_messages/events/new). The location is defined as an attachement object with longitue and latitude coordinates or a Twitter place.  

## Example message with shared coordinate attachment

      `{   "event": {     "type": "message_create",     "message_create": {       "target": {         "recipient_id": "844385345234"       },       "message_data": {         "text": "Here's my location",         "attachment": {           "type": "location",           "location": {             "type": "shared_coordinate",             "shared_coordinate": {               "coordinates": {                 "type": "Point",                 "coordinates": [-122.443893, 37.771718]               }             }           }         }       }     }   } }`