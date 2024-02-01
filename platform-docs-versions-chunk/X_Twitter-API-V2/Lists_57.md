platform: X
topic: Twitter-API-V2
subtopic: Lists
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Lists.md
url: https://developer.twitter.com/en/docs/twitter-api/lists/manage-lists/api-reference/post-lists

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read`<br><br>`list.read`<br><br>`list.write` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### JSON body parameters

| Name | Type | Description |
| --- | --- | --- |
| `name`  <br> Required | string | The name of the List you wish to create. |
| `description`  <br> Optional | string | Description of the List. |
| `private`  <br> Optional | boolean | Determine whether the List should be private. |