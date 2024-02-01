platform: Facebook
topic: Graph-API
subtopic: Application Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Application Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/application/assets/

# Application Assets

## Reading

You can't perform this operation on this endpoint.

## Creating

You can make a POST request to `assets` edge from the following paths:

* [`/{application_id}/assets`](https://developers.facebook.com/docs/graph-api/reference/application/assets/)

When posting to this edge, no Graph object will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `asset`<br><br>file | The asset file to upload<br><br>Required |
| `comment`<br><br>string | Optional comment describing the asset |
| `type`<br><br>string | Type of the asset, e.g. SWF, JS, BUNDLE, UNITY\_WEBGL, GAMES\_DESKTOP, PRIVACY\_POLICY, TOS<br><br>Required |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |