platform: Facebook
topic: Graph-API
subtopic: User Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/User Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/user/live_videos/

### Error Codes

| Error | Description |
| --- | --- |
| 190 | Invalid OAuth 2.0 Access Token |
| 100 | Invalid parameter |
| 200 | Permissions error |

## Creating

You can make a POST request to `live_videos` edge from the following paths:

* [`/{user_id}/live_videos`](https://developers.facebook.com/docs/graph-api/reference/user/live_videos/)

When posting to this edge, a [LiveVideo](https://developers.facebook.com/docs/graph-api/reference/live-video/) will be created.

Scheduling is deprecated. Calls to the `POST /ID/live-video` endpoint with the `planned_start_time` parameter will return an error. To schedule a live video, use the `event_params` parameter.