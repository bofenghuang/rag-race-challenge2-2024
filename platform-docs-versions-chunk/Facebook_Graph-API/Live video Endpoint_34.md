platform: Facebook
topic: Graph-API
subtopic: Live video Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Live video Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/live-video/input_streams/

# Live Video Input Streams

## Reading

You can't perform this operation on this endpoint.

## Creating

You can make a POST request to `input_streams` edge from the following paths:

* [`/{live_video_id}/input_streams`](https://developers.facebook.com/docs/graph-api/reference/live-video/input_streams/)

When posting to this edge, a [LiveVideoInputStream](https://developers.facebook.com/docs/graph-api/reference/live-video-input-stream/) will be created.

### Parameters

This endpoint doesn't have any parameters.

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node represented by `id` in the return type.

Struct {

`id`: numeric string,

}

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |

## Updating

You can't perform this operation on this endpoint.