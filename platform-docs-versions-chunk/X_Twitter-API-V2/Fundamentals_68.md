platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/metrics


### Public metrics

In the following request, we are requesting public metrics on the Tweet and on the attached video with the following fields and expansion. Be sure to replace `$BEARER_TOKEN` with your own generated bearer token.

* tweet.fields=public\_metrics
* expansions=attachments.media\_keys&media.fields=public\_metrics

#### Sample Request

      `curl 'https://api.twitter.com/2/tweets?ids=1204084171334832128&tweet.fields=public_metrics&expansions=attachments.media_keys&media.fields=public_metrics' --header 'Authorization: Bearer $BEARER_TOKEN'`
    

**Sample Response**

      `{     "data": [         {             "id": "1204084171334832128",             "text": "Tired of reading? We’ve got you covered. Learn about the capabilities of the Account Activity API in this video walkthrough with @tonyv00 from our DevRel team. 🍿 ⬇️ https://t.co/LdHy4aLu0i",             "public_metrics": {                 "retweet_count": 9,                 "reply_count": 2,                 "like_count": 49,                 "quote_count": 1             },             "attachments": {                 "media_keys": [                     "13_1204080851740315648"                 ]             }         }     ],     "includes": {         "media": [             {                 "media_key": "13_1204080851740315648",                 "public_metrics": {                     "view_count": 1808                 },                 "type": "video"             }         ]     } }`