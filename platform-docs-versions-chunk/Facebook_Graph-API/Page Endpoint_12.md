platform: Facebook
topic: Graph-API
subtopic: Page Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Page Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/page/

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

You can make a POST request to `subscribed_apps` edge from the following paths:

* [`/{page_id}/subscribed_apps`](https://developers.facebook.com/docs/graph-api/reference/page/subscribed_apps/)

When posting to this edge, a [Page](https://developers.facebook.com/docs/graph-api/reference/page/) will be created.