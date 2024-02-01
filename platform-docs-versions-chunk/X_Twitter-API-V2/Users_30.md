platform: X
topic: Twitter-API-V2
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-id

### Example responses

* [Default fields](#tab0)
* [Optional fields](#tab1)

Default fields

Optional fields

      `{   "data": {     "id": "2244994945",     "name": "Twitter Dev",     "username": "TwitterDev"   } }`
    

      `{   "data": {     "username": "TwitterDev",     "created_at": "2013-12-14T04:35:55.000Z",     "pinned_tweet_id": "1255542774432063488",     "id": "2244994945",     "name": "Twitter Dev"   },   "includes": {     "tweets": [       {         "text": "During these unprecedented times, what’s happening on Twitter can help the world better understand &amp; respond to the pandemic. nnWe're launching a free COVID-19 stream endpoint so qualified devs &amp; researchers can study the public conversation in real-time. https://t.co/BPqMcQzhId",         "created_at": "2020-04-29T17:01:38.000Z",         "id": "1255542774432063488"       }     ]   } }`