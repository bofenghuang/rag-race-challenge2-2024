platform: Facebook
topic: Graph-API
subtopic: User Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/User Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/user/

### Return Type

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 2903 | Cannot delete this test account |
| 100 | Invalid parameter |
| 2904 | Cannot delete the OG Test User |
| 200 | Permissions error |
| 240 | Desktop applications cannot call this function for other users |

You can dissociate a [User](https://developers.facebook.com/docs/graph-api/reference/user/) from a [Page](https://developers.facebook.com/docs/graph-api/reference/page/) by making a DELETE request to [`/{page_id}/blocked`](https://developers.facebook.com/docs/graph-api/reference/page/blocked/).

### Parameters

| Parameter | Description |
| --- | --- |
| `asid`<br><br>user/page ID | App Scoped User ID to unblock |
| `psid`<br><br>UID | Page Scoped User ID to unblock |
| `uid`<br><br>UID | Deprecated. Same as `user` |
| `user`<br><br>UID | List of User or Page IDs to unblock. This or `uid` is required |

### Return Type

Struct {

`success`: bool,

}