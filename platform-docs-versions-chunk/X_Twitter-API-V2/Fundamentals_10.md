platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user


### Retrieving a user object

#### Sample Request

In the following request, we are requesting fields for the user on the [users lookup](https://developer.twitter.com/en/docs/twitter-api/users/lookup/introduction.html) endpoint. Be sure to replace `$BEARER_TOKEN` with your own generated [Bearer Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens).  
 

      `curl --request GET 'https://api.twitter.com/2/users?ids=2244994945&user.fields=created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,url,username,verified,withheld&expansions=pinned_tweet_id' --header 'Authorization: Bearer $BEARER_TOKEN'`
    

####   
Sample Response  
 

      `{     "data": [         {             "id": "2244994945",             "name": "Twitter Dev",             "username": "TwitterDev",             "location": "127.0.0.1",             "entities": {                 "url": {                     "urls": [                         {                             "start": 0,                             "end": 23,                             "url": "https://t.co/3ZX3TNiZCY",                             "expanded_url": "/content/developer-twitter/en/community",                             "display_url": "developer.twitter.com/en/community"                         }                     ]                 },                 "description": {                     "hashtags": [                         {                             "start": 23,                             "end": 30,                             "tag": "DevRel"                         },                         {                             "start": 113,                             "end": 130,                             "tag": "BlackLivesMatter"                         }                     ]                 }             },             "verified": true,             "description": "The voice of Twitter's #DevRel team, and your official source for updates, news, & events about Twitter's API. \n\n#BlackLivesMatter",             "url": "https://t.co/3ZX3TNiZCY",             "profile_image_url": "https://pbs.twimg.com/profile_images/1267175364003901441/tBZNFAgA_normal.jpg",             "protected": false,             "pinned_tweet_id": "1255542774432063488",             "created_at": "2013-12-14T04:35:55.000Z"         }     ],     "includes": {         "tweets": [             {                 "id": "1255542774432063488",                 "text": "During these unprecedented times, what’s happening on Twitter can help the world better understand &amp; respond to the pandemic. \n\nWe're launching a free COVID-19 stream endpoint so qualified devs &amp; researchers can study the public conversation in real-time. https://t.co/BPqMcQzhId"             }         ]     } }`