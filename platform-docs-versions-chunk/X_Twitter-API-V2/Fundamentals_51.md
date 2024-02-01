platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/expansions


## Expanding the media, Tweet, and user objects

#### In the following request, we are requesting the following expansions to include alongside the default Tweet fields.  Be sure to replace `$ACCESS_TOKEN` with your own generated [App-only Token](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/app-only).

* `attachments.media_keys`
* `referenced_tweets.id`
* `author_id`

**Sample Request**

      `curl 'https://api.twitter.com/2/tweets/1212092628029698048?expansions=attachments.media_keys,referenced_tweets.id,author_id' --header 'Authorization: Bearer $ACCESS_TOKEN'`
    

**Sample Response**

      `{     "data": {         "attachments": {             "media_keys": [                 "16_1211797899316740096"             ]         },         "author_id": "2244994945",         "id": "1212092628029698048",         "referenced_tweets": [             {                 "type": "replied_to",                 "id": "1212092627178287104"             }         ],         "text": "We believe the best future version of our API will come from building it with YOU. Here’s to another great year with everyone who builds on the Twitter platform. We can’t wait to continue working with you in the new year. https://t.co/yvxdK6aOo2"     },     "includes": {         "media": [             {                 "media_key": "16_1211797899316740096",                 "type": "animated_gif"             }         ],         "users": [             {                 "id": "2244994945",                 "name": "Twitter Dev",                 "username": "TwitterDev"             }         ],         "tweets": [             {                 "author_id": "2244994945",                 "id": "1212092627178287104",                 "referenced_tweets": [                     {                         "type": "replied_to",                         "id": "1212092626247110657"                     }                 ],                 "text": "These launches would not be possible without the feedback you provided along the way, so THANK YOU to everyone who has contributed your time and ideas. Have more feedback? Let us know ⬇️ https://t.co/Vxp4UKnuJ9"             }         ]     } }`