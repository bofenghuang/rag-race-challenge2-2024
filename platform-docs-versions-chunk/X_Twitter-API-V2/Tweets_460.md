platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/bookmarks/api-reference/delete-users-id-bookmarks-tweet_id

### Example responses

* [Successful response](#tab0)

Successful response

      `{   "data": {     "bookmarked": false   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `bookmarks` | boolean | Indicates whether the user has removed the Bookmark of the specified Tweet. specified Tweet as a result of this request. The returned value is `false` for a successful request. |