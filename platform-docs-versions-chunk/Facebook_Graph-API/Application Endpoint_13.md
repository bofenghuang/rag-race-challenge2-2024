platform: Facebook
topic: Graph-API
subtopic: Application Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Application Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/application/

### Return Type

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

You can make a POST request to `client_apps` edge from the following paths:

* [`/{business_id}/client_apps`](https://developers.facebook.com/docs/marketing-api/reference/business/client_apps/)

When posting to this edge, an [Application](https://developers.facebook.com/docs/graph-api/reference/application/) will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `app_id` | App ID.<br><br>Required |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`access_status`: enum,

}