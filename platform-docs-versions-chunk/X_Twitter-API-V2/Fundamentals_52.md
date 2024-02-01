platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/expansions


## Expanding the poll object

In the following request, we are requesting the following expansions to include alongside the default Tweet fields:

* `attachments.poll_ids`

**Sample Request**

      `curl 'https://api.twitter.com/2/tweets/1199786642791452673?expansions=attachments.poll_ids' --header 'Authorization: Bearer $ACCESS_TOKEN'`
    

**Sample Response**

      `{     "data": {         "attachments": {             "poll_ids": [                 "1199786642468413448"             ]         },         "id": "1199786642791452673",         "text": "C#"     },     "includes": {         "polls": [             {                 "id": "1199786642468413448",                 "options": [                     {                         "position": 1,                         "label": "“C Sharp”",                         "votes": 795                     },                     {                         "position": 2,                         "label": "“C Hashtag”",                         "votes": 156                     }                 ]             }         ]     } }`