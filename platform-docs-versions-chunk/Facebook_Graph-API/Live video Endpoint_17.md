platform: Facebook
topic: Graph-API
subtopic: Live video Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Live video Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/live-video/

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node represented by `id` in the return type.

Struct {

`id`: numeric string,

`persistent_stream_url`: string,

`backup_persistent_stream_url`: string,

}

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 1005 | Fail to upload cover photo. |

## Deleting

You can delete a [LiveVideo](https://developers.facebook.com/docs/graph-api/reference/live-video/) by making a DELETE request to [`/{live_video_id}`](https://developers.facebook.com/docs/graph-api/reference/live-video/).

### Limitations

You cannot delete a LiveVideo on a [User](https://developers.facebook.com/docs/graph-api/reference/user) or [Group](https://developers.facebook.com/docs/graph-api/reference/group).

### Parameters

This endpoint doesn't have any parameters.

### Return Type

Struct {

`success`: bool,

}