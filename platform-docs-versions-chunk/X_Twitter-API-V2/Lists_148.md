platform: X
topic: Twitter-API-V2
subtopic: Lists
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Lists.md
url: https://developer.twitter.com/en/docs/twitter-api/lists/list-members/api-reference/get-lists-id-members


### Example responses

* [Default fields](#tab0)
* [Optional fields](#tab1)

Default fields

Optional fields

      `{   "data": [     {       "id": "1319036828964454402",       "name": "Birdwatch",       "username": "birdwatch"     },     {       "id": "1244731491088809984",       "name": "Twitter Thailand",       "username": "TwitterThailand"     },     {       "id": "1194267639100723200",       "name": "Twitter Retweets",       "username": "TwitterRetweets"     },     {       "id": "1168976680867762177",       "name": "Twitter Able",       "username": "TwitterAble"     },     {       "id": "1065249714214457345",       "name": "Spaces",       "username": "TwitterSpaces"     }   ],   "meta": {     "result_count": 5,     "next_token": "5676935732641845249"   } }`
    

      `{   "data": [     {       "name": "Birdwatch",       "id": "1319036828964454402",       "username": "birdwatch",       "pinned_tweet_id": "1353789891348475905"     },     {       "name": "Twitter Thailand",       "id": "1244731491088809984",       "username": "TwitterThailand"     },     {       "name": "Twitter Retweets",       "id": "1194267639100723200",       "username": "TwitterRetweets"     },     {       "name": "Twitter Able",       "id": "1168976680867762177",       "username": "TwitterAble"     },     {       "name": "Spaces",       "id": "1065249714214457345",       "username": "TwitterSpaces",       "pinned_tweet_id": "1451239134798942208"     }   ],   "includes": {     "tweets": [       {         "id": "1353789891348475905",         "text": "Want to help build a new community-driven approach to tackling misleading information? Join us — sign up for Birdwatch! nnhttps://t.co/FSsqNznPy1"       },       {         "id": "1451239134798942208",         "text": "the time has arrived -- we’re now rolling out the ability for everyone on iOS and Android to host a Spacennif this is your first time hosting, welcome! here’s a refresher on how https://t.co/cLH8z0bocy"       }     ]   },   "meta": {     "result_count": 5,     "next_token": "5676935732641845249"   } }`