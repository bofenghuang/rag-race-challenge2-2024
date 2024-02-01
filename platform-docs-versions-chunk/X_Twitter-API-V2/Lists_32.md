platform: X
topic: Twitter-API-V2
subtopic: Lists
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Lists.md
url: https://developer.twitter.com/en/docs/twitter-api/lists/list-lookup/api-reference/get-users-id-owned_lists

### Example responses

* [Default fields](#tab0)
* [Optional fields](#tab1)

Default fields

Optional fields

      `{   "data": [     {       "id": "1451305624956858369",       "name": "Test List"     }   ],   "meta": {     "result_count": 1   } }`
    

      `{   "data": [     {       "follower_count": 0,       "id": "1451305624956858369",       "name": "Test List",       "owner_id": "2244994945"     }   ],   "includes": {     "users": [       {         "username": "TwitterDev",         "id": "2244994945",         "created_at": "2013-12-14T04:35:55.000Z",         "name": "Twitter Dev"       }     ]   },   "meta": {     "result_count": 1   } }`