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
| 210 | User not visible |
| 80001 | There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |

You can dissociate an [Application](https://developers.facebook.com/docs/graph-api/reference/application/) from an [AdAccount](https://developers.facebook.com/docs/marketing-api/reference/ad-account/) by making a DELETE request to [`/act_{ad_account_id}/subscribed_apps`](https://developers.facebook.com/docs/marketing-api/reference/ad-account/subscribed_apps/).

### Parameters

| Parameter | Description |
| --- | --- |
| `app_id`<br><br>string | Default value:<br><br>the id of app to be unsubscribed from ad account |

### Return Type

Struct {

`success`: bool,

}