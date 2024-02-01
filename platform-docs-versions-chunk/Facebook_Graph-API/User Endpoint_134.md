platform: Facebook
topic: Graph-API
subtopic: User Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/User Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/user/posts

### Limitations

This endpoint will only returns Posts created on the app user's Timeline and Posts in which the app user has been tagged.

### Requirements

| Type of Requirement | Description |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) |
| [Permissions](https://developers.facebook.com/docs/permissions/reference/) | [`user_posts`](https://developers.facebook.com/docs/permissions/reference/user_posts) |

### Query String Parameters

| Name | Description |
| --- | --- |
| `include_hidden`  <br>boolean | Set to `true` to have results include hidden Posts. |
| `show_expired`  <br>boolean | Set to `true` to have results include expired Posts. |
| `with`  <br>enum {LOCATION} | Only return Posts that have set a location. |