platform: X
topic: Twitter-API-V1
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/geo

## Coordinates object data dictionary

|     |     |     |
| --- | --- | --- |
| Field | Type | Description |
| coordinates | Collection of Float | The longitude and latitude of the Tweet’s location, as a collection in the form **\[longitude, latitude\]**. Example:<br><br>"coordinates":\[-97.51087576,35.46500176\] |
| type | String | The type of data encoded in the coordinates property. This will be “Point” for Tweet coordinates fields. Example:<br><br>"type": "Point" |

## JSON examples for geo-referenced Tweets