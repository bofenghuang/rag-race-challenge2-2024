platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/hide-replies/api-reference/put-tweets-id-hidden

### Example responses

* [Success (reply hidden)](#tab0)
* [Success (reply unhidden)](#tab1)

Success (reply hidden)

Success (reply unhidden)

      `{   "data": {     "hidden": true   } }`
    

      `{   "data": {     "hidden": false   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `hidden` | boolean | Indicates if the Tweet was successfully hidden or unhidden. |