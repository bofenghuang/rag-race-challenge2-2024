platform: Facebook
topic: Graph-API
subtopic: Whats app business hsm Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Whats app business hsm Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/whats-app-business-hsm/

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 80012 | There have been too many calls to this message template. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
| 192 | Invalid phone number |

## Deleting

You can dissociate a [WhatsAppMessageTemplate](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-hsm/) from a [WhatsAppBusinessAccount](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/) by making a DELETE request to [`/{whats_app_business_account_id}/message_templates`](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/message_templates/).