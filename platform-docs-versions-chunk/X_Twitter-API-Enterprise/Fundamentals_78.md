platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/activity

###   
Additional Tweet attributes

| Attribute | Type | Description |
| --- | --- | --- |
| twitter\_lang | string |     |
| favoritesCount | int | _Nullable._ Indicates approximately how many times this Tweet has been liked by Twitter users.  <br>  <br>"favoritesCount":298 |
| retweetCount | int | Number of times this Tweet has been retweeted. Example:<br><br>"retweetCount":153 |

### Deprecated Attributes

|     |     |     |
| --- | --- | --- |
| Field | Type | Description |
| geo | object | Point location where the Tweet was created. |
| twitter\_filter\_level | string | Deprecated field left in for non breaking change |