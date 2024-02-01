platform: X
topic: Twitter-API-V2
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-by


### Example responses

* [Default fields](#tab0)
* [Optional fields](#tab1)

Default fields

Optional fields

      `{   "data": [     {       "id": "2244994945",       "username": "TwitterDev",       "name": "Twitter Dev"     },     {       "id": "783214",       "username": "Twitter",       "name": "Twitter"     }   ] }`
    

      `{   "data": [     {       "created_at": "2013-12-14T04:35:55.000Z",       "username": "TwitterDev",       "pinned_tweet_id": "1255542774432063488",       "id": "2244994945",       "name": "Twitter Dev"     },     {       "created_at": "2007-02-20T14:35:54.000Z",       "username": "Twitter",       "pinned_tweet_id": "1274087687469715457",       "id": "783214",       "name": "Twitter"     }   ],   "includes": {     "tweets": [       {         "created_at": "2020-04-29T17:01:38.000Z",         "text": "During these unprecedented times, what’s happening on Twitter can help the world better understand &amp; respond to the pandemic. nnWe're launching a free COVID-19 stream endpoint so qualified devs &amp; researchers can study the public conversation in real-time. https://t.co/BPqMcQzhId",         "id": "1255542774432063488"       },       {         "created_at": "2020-06-19T21:12:30.000Z",         "text": "📍 Minneapolisn🗣️ @FredTJoseph https://t.co/lNTOkyguG1",         "id": "1274087687469715457"       }     ]   } }`