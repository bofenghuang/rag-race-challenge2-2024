platform: Facebook
topic: Graph-API
subtopic: Video Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Video Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/video/gaming_clip_create/

# Video Gaming Clip Create

## Reading

You can't perform this operation on this endpoint.

## Creating

You can make a POST request to `gaming_clip_create` edge from the following paths:

* [`/{video_id}/gaming_clip_create`](https://developers.facebook.com/docs/graph-api/reference/video/gaming_clip_create/)

When posting to this edge, a [Video](https://developers.facebook.com/docs/graph-api/reference/video/) will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `duration_seconds`<br><br>float | Default value: `60`<br><br>The duration in seconds to create the clip. Should be a positive number. |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`id`: numeric string,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

## Updating

You can't perform this operation on this endpoint.