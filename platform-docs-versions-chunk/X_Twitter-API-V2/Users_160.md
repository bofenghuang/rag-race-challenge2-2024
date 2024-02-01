platform: X
topic: Twitter-API-V2
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/users/mutes/api-reference/get-users-muting

### Example responses

* [Default fields](#tab0)
* [Optional fields](#tab1)

Default fields

Optional fields

      `{   "data": [     {       "id": "2244994945",       "name": "Twitter Dev",       "username": "TwitterDev"     }   ],   "meta": {     "result_count": 1   } }`
    

      `{   "data": [     {       "username": "TwitterDev",       "created_at": "2013-12-14T04:35:55.000Z",       "id": "2244994945",       "name": "Twitter Dev",       "pinned_tweet_id": "1430984356139470849"     }   ],   "includes": {     "tweets": [       {         "created_at": "2021-08-26T20:03:51.000Z",         "id": "1430984356139470849",         "text": "Help us build a better Twitter Developer Platform!n nTake the annual developer survey &gt;&gt;&gt; https://t.co/9yTbEKlJHH https://t.co/fYIwKPzqua"       }     ]   },   "meta": {     "result_count": 1   } }`