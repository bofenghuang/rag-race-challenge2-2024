platform: Facebook
topic: Graph-API
subtopic: User Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/User Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/user/live_videos/

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
| 200 | Permissions error |
| 100 | Invalid parameter |
| 1005 | Fail to upload cover photo. |
| 1000 | Invalid time for an event. |

## Updating

You can't perform this operation on this endpoint.