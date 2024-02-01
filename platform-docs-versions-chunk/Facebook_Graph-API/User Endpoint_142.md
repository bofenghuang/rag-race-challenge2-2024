platform: Facebook
topic: Graph-API
subtopic: User Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/User Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/user/scores

### Permissions

* An app access token can be used to see the scores that a person has received in that app.
    
* A user access token with `user_games_activity` permission is required to see all scores that person has received from other apps.
    

### Fields

| Name | Description | Type |
| --- | --- | --- |
| `user` | The person associated with the scores. | [`User`](https://developers.facebook.com/docs/graph-api/reference/user/) |
| `score` | The actual score. | `int` |
| `application` | The app in which the score was achieved. | [`App`](https://developers.facebook.com/docs/reference/api/application/). |