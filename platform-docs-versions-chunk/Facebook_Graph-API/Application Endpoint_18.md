platform: Facebook
topic: Graph-API
subtopic: Application Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Application Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/application/

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |

You can update an [Application](https://developers.facebook.com/docs/graph-api/reference/application/) by making a POST request to [`/act_{ad_account_id}/subscribed_apps`](https://developers.facebook.com/docs/marketing-api/reference/ad-account/subscribed_apps/).

### Parameters

| Parameter | Description |
| --- | --- |
| `app_id`<br><br>string | Default value:<br><br>the id of app to be subscribed from ad account |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node represented by `id` in the return type.

Struct {

`success`: bool,

}