platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/retweets/api-reference/delete-users-id-retweets-tweet_id

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`tweet.write`<br><br>`users.read` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Required | string | The user ID who you are removing a the Retweet of a Tweet on behalf of. It must match your own user ID or that of an authenticating user, meaning that you must pass the [Access Tokens](https://developer.twitter.com/en/docs/authentication/oauth-2-0/user-access-token) associated with the user ID when authenticating your request. |
| `source_tweet_id`  <br> Required | string | The ID of the Tweet that you would like the `id` to remove the Retweet of. |