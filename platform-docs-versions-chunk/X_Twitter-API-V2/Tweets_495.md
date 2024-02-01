platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/hide-replies/api-reference/put-tweets-id-hidden

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read`<br><br>`tweet.moderate.write` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Required | string | Unique identifier of the Tweet to hide or unhide. The Tweet must belong to a conversation initiated by the authenticating user. |

  
  

### JSON body parameters

| Name | Type | Description |
| --- | --- | --- |
| `hidden`  <br> Required | boolean | Indicates the action to perform. Specify `true` to hide the Tweet, `false` to unhide. Trying to hide a Tweet that's already hidden (or unhide a Tweet that is not hidden) will result in a successful call. |