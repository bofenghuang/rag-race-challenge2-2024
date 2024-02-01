platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/data-dictionary/using-fields-and-expansions


### Requesting additional fields and objects.

First off, we will be requesting a [Tweet object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) using a Tweet ID and the [GET /tweets endpoint](https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/introduction.html).  

Request:

      `curl --request GET --url 'https://api.twitter.com/2/tweets?ids=1260294888811347969' \   --header 'Authorization: Bearer $BEARER_TOKEN'`
    

Response:

      `{     "data": [         {             "id": "1260294888811347969",             "text": "Don’t miss the Tweets about your Tweet. \n\nNow on iOS, you can see Retweets with comments all in one place. https://t.co/oanjZfzC6y"         }     ] }`
    

The following step-by-step guide will show you how to retrieve the additional data we can see in the screenshot.  

1. Identify the additional fields that you would like to request by using our [object model](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model.html), or by reviewing the list of fields in the endpoints’ API reference pages.  
      
    In this case, we will be requesting the following additional fields:  
    attachments, author\_id, created\_at, public\_metrics.  
      
    
2. Build the `tweet.fields` query parameter with the above fields as its value using a comma-separated list:  
    `?tweet.fields=attachments,author_id,created_at,public_metrics`
    
3. Add the query parameter to the GET /tweets request that you made earlier.

Request:

      `curl --request GET --url 'https://api.twitter.com/2/tweets?ids=1260294888811347969&tweet.fields=attachments,author_id,created_at,public_metrics' \   --header 'Authorization: Bearer $BEARER_TOKEN'`
    

  
Response:  
 

      `{     "data": [         {             "id": "1260294888811347969",             "text": "Don’t miss the Tweets about your Tweet. \n\nNow on iOS, you can see Retweets with comments all in one place. https://t.co/oanjZfzC6y",             "author_id": "783214",             "public_metrics": {                 "retweet_count": 5219,                 "reply_count": 1828,                 "like_count": 17141,                 "quote_count": 3255             },             "attachments": {                 "media_keys": [                     "13_1260294804770041858"                 ]             },             "created_at": "2020-05-12T19:44:51.000Z"         }     ] }`
    

  
4. Next, we are going to request fields related to the video that was included in the Tweet. To do so, we will use the `expansions` parameter with `attachments.media_keys` as the value, and add this to the request.

?expansions=attachments.media\_keys

Request:  
 

      `curl --request GET --url 'https://api.twitter.com/2/tweets?ids=1260294888811347969&tweet.fields=attachments,author_id,created_at,public_metrics&expansions=attachments.media_keys' \   --header 'Authorization: Bearer $BEARER_TOKEN'`
    

  
Response, with the media object represented in the includes object:  
 

      `{     "data": [         {             "id": "1260294888811347969",             "text": "Don’t miss the Tweets about your Tweet. \n\nNow on iOS, you can see Retweets with comments all in one place. https://t.co/oanjZfzC6y",             "public_metrics": {                 "retweet_count": 5219,                 "reply_count": 1828,                 "like_count": 17141,                 "quote_count": 3255             },             "created_at": "2020-05-12T19:44:51.000Z",             "attachments": {                 "media_keys": [                     "13_1260294804770041858"                 ]             },             "author_id": "783214"         }     ],     "includes": {         "media": [             {                 "media_key": "13_1260294804770041858",                 "type": "video"             }         ]     } }`
    

  
5. And finally, we are going to request the view count and duration of the video. These aren’t default fields so we have to specifically request them. Use the `media.fields` parameter with the comma-separated values, `public_metrics` and `duration_ms` in your request.

?media.fields=public\_metrics,duration\_ms

  
Request:  
 

      `curl --request GET --url 'https://api.twitter.com/2/tweets?ids=1260294888811347969&tweet.fields=attachments,author_id,created_at,public_metrics&expansions=attachments.media_keys&media.fields=duration_ms,public_metrics' --header 'Authorization: Bearer $BEARER_TOKEN'`
    

  
Response, which now includes all the data that can be seen in the Tweet screenshot:  
 

      `{     "data": [         {             "id": "1260294888811347969",             "text": "Don’t miss the Tweets about your Tweet. \n\nNow on iOS, you can see Retweets with comments all in one place. https://t.co/oanjZfzC6y",             "author_id": "783214",             "public_metrics": {                 "retweet_count": 5219,                 "reply_count": 1828,                 "like_count": 17141,                 "quote_count": 3255             },             "created_at": "2020-05-12T19:44:51.000Z",             "attachments": {                 "media_keys": [                     "13_1260294804770041858"                 ]             }         }     ],     "includes": {         "media": [             {                 "duration_ms": 36503,                 "media_key": "13_1260294804770041858",                 "public_metrics": {                     "view_count": 1534703                 },                 "type": "video"             }         ]     } }`
    

In total, we included the following parameters in this example:

* ids=1260294888811347969
* tweet.fields=attachments,author\_id,created\_at,public\_metrics
* expansions=attachments.media\_keys
* media.fields=public\_metrics,duration\_ms  
     

When tied together, here is what the full query string looks like:

?ids=1260294888811347969&tweet.fields=attachments,author\_id,created\_at,public\_metrics&expansions=attachments.media\_keys&media.fields=public\_metrics,duration\_ms