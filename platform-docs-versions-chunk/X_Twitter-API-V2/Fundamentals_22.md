platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/poll


### Retrieving a poll object

#### Sample Request

In the following request, we are requesting fields for the poll object attached to the Tweet on the [Tweets lookup](https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/introduction.html) endpoint. Since poll is a child object of a Tweet, the `attachments.poll_id` expansion is required. Be sure to replace `$BEARER_TOKEN` with your own generated [Bearer Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens).  
 

      `curl --request GET 'https://api.twitter.com/2/tweets?ids=1199786642791452673&expansions=attachments.poll_ids&poll.fields=duration_minutes,end_datetime,id,options,voting_status' --header 'Authorization: Bearer $BEARER_TOKEN'`
    

####   
Sample Response  
 

      `{     "data": [         {             "text": "C#",             "id": "1199786642791452673",             "attachments": {                 "poll_ids": [                     "1199786642468413448"                 ]             }         }     ],     "includes": {         "polls": [             {                 "id": "1199786642468413448",                 "voting_status": "closed",                 "duration_minutes": 1440,                 "options": [                     {                         "position": 1,                         "label": "“C Sharp”",                         "votes": 795                     },                     {                         "position": 2,                         "label": "“C Hashtag”",                         "votes": 156                     }                 ],                 "end_datetime": "2019-11-28T20:26:41.000Z"             }         ]     } }`