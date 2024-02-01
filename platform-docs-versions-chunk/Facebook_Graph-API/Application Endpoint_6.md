platform: Facebook
topic: Graph-API
subtopic: Application Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Application Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/application/

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 190 | Invalid OAuth 2.0 Access Token |
| 459 | The session is invalid because the user has been checkpointed |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 278 | Reading advertisements requires an access token with the extended permission ads\_read |

## Creating

You can make a POST request to `owned_apps` edge from the following paths:

* [`/{business_id}/owned_apps`](https://developers.facebook.com/docs/marketing-api/reference/business/owned_apps/)

When posting to this edge, an [Application](https://developers.facebook.com/docs/graph-api/reference/application/) will be created.

### Parameters

This endpoint doesn't have any parameters.

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`access_status`: string,

}