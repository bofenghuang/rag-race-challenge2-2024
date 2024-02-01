platform: Facebook
topic: Graph-API
subtopic: Application Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Application Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/application/

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |

## Deleting

You can dissociate an [Application](https://developers.facebook.com/docs/graph-api/reference/application/) from a [Page](https://developers.facebook.com/docs/graph-api/reference/page/) by making a DELETE request to [`/{page_id}/subscribed_apps`](https://developers.facebook.com/docs/graph-api/reference/page/subscribed_apps/).

### Parameters

This endpoint doesn't have any parameters.

### Return Type

Struct {

`success`: bool,

`messaging_success`: bool,

}