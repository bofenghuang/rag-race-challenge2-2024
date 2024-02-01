platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/conversation-id


###   
Retrieving conversation\_id as a tweet.fields parameter

To request the conversation\_id for all Tweets returned on a v2 endpoint, the tweet.fields=conversation\_id field can be added to the request parameters.  The conversation\_id field is always the Tweet ID of the original Tweet in the conversation reply thread.  All Tweets within the same reply thread, including reply threads that are created from earlier reply threads, will show the same conversation\_id.  
 

#### Request with conversation\_id parameter  
 

      `curl --request GET \   --url 'https://api.twitter.com/2/tweets?ids=1225917697675886593&tweet.fields=author_id,conversation_id,created_at,in_reply_to_user_id,referenced_tweets&expansions=author_id,in_reply_to_user_id,referenced_tweets.id&user.fields=name,username' \   --header 'Authorization: Bearer $ACCESS_TOKEN'` 
    

####   
Response  
 

      `{     "data": [         {             "id": "1225917697675886593",             "text": "@TwitterEng *ahem* https://t.co/aroJHt2zQ1",             "created_at": "2020-02-07T23:02:10.000Z",             "author_id": "2244994945",             "in_reply_to_user_id": "6844292",             "conversation_id": "1225912275971657728",             "referenced_tweets": [                 {                     "type": "quoted",                     "id": "1200517737669378053"                 },                 {                     "type": "replied_to",                     "id": "1225912275971657728"                 }             ]         }     ],     "includes": {         "users": [             {                 "username": "TwitterDev",                 "name": "Twitter Dev",                 "id": "2244994945"             },             {                 "username": "TwitterEng",                 "name": "Twitter Engineering",                 "id": "6844292"             }         ],         "tweets": [             {                 "id": "1200517737669378053",                 "text": "|￣￣￣￣￣￣￣￣￣￣￣|\n             don't push            \n             to prod on            \n               Fridays                  \n|＿＿＿＿＿＿＿＿＿＿＿| \n(\\__/)  ||\n(•ㅅ•) ||\n/ 　 づ",                 "created_at": "2019-11-29T20:51:47.000Z",                 "author_id": "2244994945",                 "conversation_id": "1200517737669378053"             },             {                 "id": "1225912275971657728",                 "text": "Note to self: Don't deploy on Fridays",                 "created_at": "2020-02-07T22:40:37.000Z",                 "author_id": "6844292",                 "conversation_id": "1225912275971657728"             }         ]     } }`