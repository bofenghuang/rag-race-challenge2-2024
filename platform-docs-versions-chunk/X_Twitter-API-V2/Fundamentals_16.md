platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/list


### Retrieving a user object

#### Sample Request

In the following request, we are requesting fields for the user on the [List lookup by ID](https://developer.twitter.com/en/docs/twitter-api/lists/list-lookup/introduction.html) endpoint. Be sure to replace `$BEARER_TOKEN` with your own generated [Bearer Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens).  
 

      `curl --request GET 'https://api.twitter.com/2/lists/1355797419175383040?list.fields=created_at,description,private,follower_count,member_count,owner_id&expansions=owner_id' --header 'Authorization: Bearer $BEARER_TOKEN'`
    

####   
Sample Response  
 

      `{   "data": {     "name": "Twitter Comms",     "member_count": 60,     "id": "1355797419175383040",     "private": false,     "description": "",     "follower_count": 198,     "owner_id": "257366942",     "created_at": "2021-01-31T08:37:48.000Z"   },   "includes": {     "users": [       {         "created_at": "2011-02-25T07:51:26.000Z",         "name": "Ashleigh Hay 🤸🏼‍♀️",         "id": "257366942",         "username": "shleighhay",         "verified": false       }     ]   } }`