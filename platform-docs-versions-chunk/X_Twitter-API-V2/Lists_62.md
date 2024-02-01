platform: X
topic: Twitter-API-V2
subtopic: Lists
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Lists.md
url: https://developer.twitter.com/en/docs/twitter-api/lists/manage-lists/api-reference/put-lists-id

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `tweet.read`<br><br>`users.read`<br><br>`list.write` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `id`  <br> Required | string | The ID of the List to be updated. |

  
  

### JSON body parameters

| Name | Type | Description |
| --- | --- | --- |
| `description`  <br> Optional | string | Updates the description of the List. |
| `name`  <br> Optional | string | Updates the name of the List. |
| `private`  <br> Optional | boolean | Determines whether the List should be private. |