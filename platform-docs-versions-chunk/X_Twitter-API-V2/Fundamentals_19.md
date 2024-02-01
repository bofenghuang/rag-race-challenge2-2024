platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/media


### Retrieving a media object

#### Sample Request

In the following request, we are requesting fields for the media object attached to the Tweet on the [Tweet lookup](https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/introduction.html) endpoint. Since media is a child object of a Tweet, the `attachment.media_keys` expansion is required. Be sure to replace `$BEARER_TOKEN` with your own generated [Bearer Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens).  
 

      `curl --request GET 'https://api.twitter.com/2/tweets?ids=1263145271946551300&expansions=attachments.media_keys&media.fields=duration_ms,height,media_key,preview_image_url,public_metrics,type,url,width,alt_text' --header 'Authorization: Bearer $BEARER_TOKEN'`
    

**Sample Response** 

      `{     "data": [         {             "text": "Testing, testing...\n\nA new way to have a convo with exactly who you want. We’re starting with a small % globally, so keep your 👀 out to see it in action. https://t.co/pV53mvjAVT",             "id": "1263145271946551300",             "attachments": {                 "media_keys": [                     "13_1263145212760805376"                 ]             }         }     ],     "includes": {         "media": [             {                 "duration_ms": 46947,                 "type": "video",                 "height": 1080,                 "media_key": "13_1263145212760805376",                 "public_metrics": {                     "view_count": 6909260                 },                 "preview_image_url": "https://pbs.twimg.com/media/EYeX7akWsAIP1_1.jpg",                 "width": 1920             }         ]     } }`