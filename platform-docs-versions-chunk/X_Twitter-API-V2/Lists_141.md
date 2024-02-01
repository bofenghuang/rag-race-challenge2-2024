platform: X
topic: Twitter-API-V2
subtopic: Lists
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Lists.md
url: https://developer.twitter.com/en/docs/twitter-api/lists/list-members/api-reference/get-users-id-list_memberships

### Example responses

* [Default fields](#tab0)
* [Optional fields](#tab1)

Default fields

Optional fields

      `{   "data": [     {       "id": "1451951974291689472",       "name": "Twitter"     },     {       "id": "1451812298184540161",       "name": "Updates"     },     {       "id": "1450519480132509697",       "name": "Twitter"     }   ],   "meta": {     "result_count": 3   } }`
    

      `{   "data": [     {       "follower_count": 5,       "id": "1451951974291689472",       "name": "Twitter",       "owner_id": "1227213680120479745"     }   ],   "includes": {     "users": [       {         "name": "구돆",         "created_at": "2020-02-11T12:52:11.000Z",         "id": "1227213680120479745",         "username": "Follow__Y0U"       }     ]   },   "meta": {     "result_count": 1   } }`