platform: Facebook
topic: Graph-API
subtopic: Whats app business account Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Whats app business account Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/

## Deleting

You can dissociate a [WhatsAppBusinessAccount](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/) from a [WhatsAppBusinessAccount](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/) by making a DELETE request to [`/{whats_app_business_account_id}/assigned_users`](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/assigned_users/).

### Parameters

| Parameter | Description |
| --- | --- |
| `user`<br><br>UID | Business user ID<br><br>Required |

### Return Type

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

## Supported values

### Currencies

Supported values for currency codes can be found in [currencies](https://developers.facebook.com/docs/marketing-api/currencies).