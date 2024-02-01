platform: Facebook
topic: Graph-API
subtopic: User Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/User Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/user/

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

You can dissociate a [User](https://developers.facebook.com/docs/graph-api/reference/user/) from an [AdAccount](https://developers.facebook.com/docs/marketing-api/reference/ad-account/) by making a DELETE request to [`/act_{ad_account_id}/assigned_users`](https://developers.facebook.com/docs/marketing-api/reference/ad-account/assigned_users/).

### Parameters

| Parameter | Description |
| --- | --- |
| `user`<br><br>UID | Business user id or system user id<br><br>Required |

### Return Type

Struct {

`success`: bool,

}