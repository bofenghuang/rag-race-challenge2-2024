platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/likes/api-reference/delete-users-user_id-likes

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Required | string | The user ID who you are removing a Like of a Tweet on behalf of. It must match your own user ID or that of an authenticating user, meaning that you must pass the [Access Tokens](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens) associated with the user ID when authenticating your request. |
| `tweet_id`  <br> Required | string | The ID of the Tweet that you would like the `id` to unlike. |

  
  

### Example requests

* [cURL](#tab0)
* [twurl](#tab1)

cURL

twurl

      `curl -X DELETE https://api.twitter.com/2/users/2244994945/likes/1228393702244134912 -H "Authorization: OAuth $OAUTH_SIGNATURE"`
    

      `twurl -X DELETE /2/users/2244994945/likes/1228393702244134912`
    

### Example responses

* [Successful response](#tab0)

Successful response

      `{   "data": {     "liked": false   } }`