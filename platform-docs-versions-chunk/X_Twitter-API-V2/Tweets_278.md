platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/post-tweets-search-stream-rules

### Example responses

* [Create rules](#tab0)
* [Success](#tab1)

Create rules

Success

      `{   "data": [     {       "value": "meme",       "tag": "funny things",       "id": "1166895166390583299"     },     {       "value": "cats has:media -grumpy",       "tag": "happy cats with media",       "id": "1166895166390583296"     },     {       "value": "cat has:media",       "tag": "cats with media",       "id": "1166895166390583297"     },     {       "value": "meme has:images",       "id": "1166895166390583298"     }   ],   "meta": {     "sent": "2019-08-29T02:07:42.205Z",     "summary": {       "created": 4,       "not_created": 0     }   } }`
    

      `{   "meta": {     "sent": "2019-08-29T01:48:54.633Z",     "summary": {       "deleted": 1,       "not_deleted": 0     }   } }`