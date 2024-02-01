platform: Facebook
topic: Graph-API
subtopic: Image copyright Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Image copyright Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/image-copyright/

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node represented by `id` in the return type.

Struct {

`id`: numeric string,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

## Updating

You can update an [ImageCopyright](https://developers.facebook.com/docs/graph-api/reference/image-copyright/) by making a POST request to [`/{image_copyright_id}`](https://developers.facebook.com/docs/graph-api/reference/image-copyright/).