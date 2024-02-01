platform: Facebook
topic: Graph-API
subtopic: Application Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Application Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/app/scores

### Permissions

* A user access token is required to view scores by that user and their friends, from the app that generated the token.

### Fields

| Name | Description | Type |
| --- | --- | --- |
| `user` | The user who reached the score. | [`User`](https://developers.facebook.com/docs/graph-api/reference/user/) |
| `application` | The app in which the score was reached. | [`App`](https://developers.facebook.com/docs/graph-api/reference/app/) |
| `score` | The score itself. | `int` |

## Publishing

Use the [`/{user-id}/scores` edge](https://developers.facebook.com/docs/graph-api/reference/user/scores/) in order to create scores.