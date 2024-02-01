platform: Facebook
topic: Graph-API
subtopic: User Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/User Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/user/permissions/

## Deleting

You can dissociate a [Permission](https://developers.facebook.com/docs/graph-api/reference/permission/) from a [User](https://developers.facebook.com/docs/graph-api/reference/user/) by making a DELETE request to [`/{user_id}/permissions`](https://developers.facebook.com/docs/graph-api/reference/user/permissions/).

### Parameters

| Parameter | Description |
| --- | --- |
| `permission`<br><br>string | permission which wanted to be remove |

### Return Type

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 240 | Desktop applications cannot call this function for other users |

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)