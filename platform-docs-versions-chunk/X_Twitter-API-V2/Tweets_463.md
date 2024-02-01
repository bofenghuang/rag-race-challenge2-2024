platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/bookmarks/api-reference/post-users-id-bookmarks

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Required | string | The user ID of an authenticated user who you are bookmarking a Tweet on behalf of. It must match your own user ID or that of an authenticating user, meaning that you must pass the [Access Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/user-access-token) associated with the user ID when authenticating your request. |

  
  

### JSON body parameters

| Name | Type | Description |
| --- | --- | --- |
| `tweet_id`  <br> Required | string | The ID of the Tweet that you would like an `id` to Bookmark. |