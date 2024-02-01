platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/space


###   
Retrieving a Space object

#### Sample Request

In the following request, we are requesting fields for the Space on the [Spaces lookup](https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/introduction.html) endpoint. Be sure to replace `$BEARER_TOKEN` with your own generated [Bearer Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens).  
 

      `curl "https://api.twitter.com/2/spaces/1DXxyRYNejbKM?space.fields=created_at,creator_id,created_athost_ids,lang,is_ticketed,invited_user_ids,participant_count,scheduled_start,speaker_ids,started_at,state,title,updated_at&expansions=creator_id,host_ids,invited_user_ids,speaker_ids" --header "Authorization: Bearer $BEARER_TOKEN"`
    

**Sample Response** 

      `{     "data": {         "id": "1zqKVXPQhvZJB",         "state": "live",         "created_at": "2021-07-04T23:12:08.000Z",         "host_ids": [           "2244994945",           "6253282"         ],         "lang": "en",         "is_ticketed": false,         "invited_user_ids": [           "2244994945",           "6253282"         ],         "participant_count": 420,         "scheduled_start": "2021-07-14T08:00:00.000Z",         "speaker_ids": [           "2244994945",           "6253282"         ],                 "started_at": "2021-07-14T08:00:12.000Z",         "title": "Say hello to the Space data object!",         "updated_at": "2021-07-11T14:44:44.000Z"     },     "includes": {         "users": [             {                 "id": "2244994945",                 "name": "Twitter Dev",                 "username": "TwitterDev"            },            {             "id": "6253282",             "name": "Twitter API",             "username": "TwitterAPI"           }     ]     } }`