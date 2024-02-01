platform: X
topic: Twitter-API-V2
subtopic: Lists
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Lists.md
url: https://developer.twitter.com/en/docs/twitter-api/lists/pinned-lists/api-reference/get-users-id-pinned_lists

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read`<br><br>`list.read` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Required | string | The user ID whose pinned Lists you would like to retrieve. The user’s ID must correspond to the user ID of the authenticating user, meaning that you must pass the [Access Tokens](https://developer.twitter.com/en/docs/authentication/oauth-2-0/user-access-token) associated with the user ID when authenticating your request. |