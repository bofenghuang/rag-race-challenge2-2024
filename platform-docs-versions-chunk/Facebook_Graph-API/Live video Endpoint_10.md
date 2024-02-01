platform: Facebook
topic: Graph-API
subtopic: Live video Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Live video Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/live-video/

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node represented by `id` in the return type.

Struct {

`id`: numeric string,

`stream_url`: string,

`secure_stream_url`: string,

`stream_secondary_urls`: List \[

string

\],

`secure_stream_secondary_urls`: List \[

string

\],

`dash_ingest_url`: string,

`dash_ingest_secondary_urls`: List \[

string

\],

`event_id`: numeric string,

}

### Error Codes

| Error | Description |
| --- | --- |
| 6000 | There was a problem uploading your video file. Please try again with another file. |

You can make a POST request to `live_videos` edge from the following paths:

* [`/{group_id}/live_videos`](https://developers.facebook.com/docs/graph-api/reference/group/live_videos/)

When posting to this edge, a [LiveVideo](https://developers.facebook.com/docs/graph-api/reference/live-video/) will be created.