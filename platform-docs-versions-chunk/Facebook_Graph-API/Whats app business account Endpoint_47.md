platform: Facebook
topic: Graph-API
subtopic: Whats app business account Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Whats app business account Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/subscribed_apps/

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
| 2200 | subscription validation failed |
| 2201 | received an invalid hub.challenge while validating endpoint |

## Updating

You can't perform this operation on this endpoint.

## Deleting

You can dissociate a [WhatsAppApplication](https://developers.facebook.com/docs/graph-api/reference/whats-app-application/) from a [WhatsAppBusinessAccount](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/) by making a DELETE request to [`/{whats_app_business_account_id}/subscribed_apps`](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/subscribed_apps/).

### Parameters

This endpoint doesn't have any parameters.