platform: Facebook
topic: Graph-API
subtopic: Page call to action Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Page call to action Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/page-call-to-action/

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |

## Deleting

You can delete a [PageCallToAction](https://developers.facebook.com/docs/graph-api/reference/page-call-to-action/) by making a DELETE request to [`/{page_call_to_action_id}`](https://developers.facebook.com/docs/graph-api/reference/page-call-to-action/).