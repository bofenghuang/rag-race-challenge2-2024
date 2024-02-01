platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/message-attachments/guides/attaching-location

## Example message with shared place attachment

      `{   "event": {     "type": "message_create",       "message_create": {         "target": {           "recipient_id": "844385345234"         },         "message_data": {           "text": "Here's my location",           "attachment": {             "type": "location",             "location": {               "type": "shared_place",               "shared_place": {                 "place": {                   "id": "123456"                 }               }             }           }         }       }     }   } }`
    

**Note:** Not all place IDs are discoverable with [GET geo/search](https://developer.twitter.com/en/docs/geo/places-near-location/api-reference/get-geo-search.html). To retrieve all available details for a place ID you may also use [GET geo/id/:place\_id](https://developer.twitter.com/en/docs/twitter-api/v1/geo/place-information/api-reference/get-geo-id-place_id).