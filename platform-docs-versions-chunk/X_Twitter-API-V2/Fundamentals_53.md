platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/expansions

## Expanding the place object

In the following request, we are requesting the following expansions to include alongside the default Tweet fields:

* `geo.place_id`

**Sample Request**

      `curl 'https://api.twitter.com/2/tweets/:ID?expansions=geo.place_id’ --header 'Authorization: Bearer $ACCESS_TOKEN'`
    

**Sample Response**

      `{     "data": {         "geo": {             "place_id": "01a9a39529b27f36"         },         "id": "ID",         "text": "Test"     },     "includes": {         "places": [             {                 "full_name": "Manhattan, NY",                 "id": "01a9a39529b27f36"             }         ]     } }`