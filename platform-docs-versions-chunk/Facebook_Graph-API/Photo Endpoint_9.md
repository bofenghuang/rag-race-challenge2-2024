platform: Facebook
topic: Graph-API
subtopic: Photo Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Photo Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/photo/

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node represented by `id` in the return type.

Struct {

`id`: numeric string,

`post_id`: token with structure: Post ID,

}

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 321 | Album is full |
| 100 | Invalid parameter |
| 220 | Album or albums not visible |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 120 | Invalid album id |

You can make a POST request to `photos` edge from the following paths:

* [`/{group_id}/photos`](https://developers.facebook.com/docs/graph-api/reference/group/photos/)

When posting to this edge, a [Photo](https://developers.facebook.com/docs/graph-api/reference/photo/) will be created.