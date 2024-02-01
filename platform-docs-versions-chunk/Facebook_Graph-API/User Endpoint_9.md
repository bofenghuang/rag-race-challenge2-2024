platform: Facebook
topic: Graph-API
subtopic: User Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/User Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/user/

### Error Codes

| Error | Description |
| --- | --- |
| 190 | Invalid OAuth 2.0 Access Token |
| 459 | The session is invalid because the user has been checkpointed |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 240 | Desktop applications cannot call this function for other users |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 210 | User not visible |
| 270 | This Ads API request is not allowed for apps with development access level (Development access is by default for all apps, please request for upgrade). Make sure that the access token belongs to a user that is both admin of the app and admin of the ad account |

You can update a [User](https://developers.facebook.com/docs/graph-api/reference/user/) by making a POST request to [`/{custom_audience_id}/users`](https://developers.facebook.com/docs/marketing-api/reference/custom-audience/users/).