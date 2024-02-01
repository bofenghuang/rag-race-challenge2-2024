platform: Facebook
topic: Graph-API
subtopic: Debug token Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Debug token Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/debug_token


### Fields

| Name | Description | Type |
| --- | --- | --- |
| `data` | Data wrapper around the result. | `object` |
| `app_id` | The ID of the application this access token is for. | `string` |
| `application` | Name of the application this access token is for. | `string` |
| `error` | Any error that a request to the graph api would return due to the access token. | `object` |
| `code` | The error code for the error. | `int` |
| `message` | The error message for the error. | `string` |
| `subcode` | The error subcode for the error. | `int` |
| `expires_at` | Timestamp when this access token expires. | `unixtime` |
| `data_access_expires_at` | Timestamp when app's access to user data expires. | `unixtime` |
| `is_valid` | Whether the access token is still valid or not. | `bool` |
| `issued_at` | Timestamp when this access token was issued. | `unixtime` |
| `metadata` | General metadata associated with the access token. Can contain data like 'sso', 'auth\_type', 'auth\_nonce' | `object` |
| `profile_id` | For impersonated access tokens, the ID of the page this token contains. | `string` |
| `scopes` | List of permissions that the user has granted for the app in this access token. | `string[]` |
| `granular_scopes` | List of granular permissions that the user has granted for the app in this access token. If permission applies to all, targets will not be shown. | `shape('scope' => string,'target_ids' => ?int[],)[]` |
| `user_id` | The ID of the user this access token is for. | `string` |