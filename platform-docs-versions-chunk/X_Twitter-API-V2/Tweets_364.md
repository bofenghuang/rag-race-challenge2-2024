platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/retweets/api-reference/delete-users-id-retweets-tweet_id

### Example responses

* [Successful response](#tab0)

Successful response

      `{   "data": {     "retweeted": false   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `retweeted` | boolean | Indicates whether the user has removed the Retweet of the specified Tweet as a result of this request. The returned value is `false` for a successful unretweet request. |