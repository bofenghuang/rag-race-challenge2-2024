platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/likes/api-reference/delete-users-id-likes-tweet_id

### Example responses

* [Successful response](#tab0)

Successful response

      `{   "data": {     "liked": false   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `liked` | boolean | Indicates whether the user is unliking the specified Tweet as a result of this request. The returned value is `false` for a successful unlike request. |