platform: Facebook
topic: Graph-API
subtopic: Page Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Page Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/page/

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node represented by `id` in the return type.

Struct {

`id`: numeric string,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 192 | Invalid phone number |
| 200 | Permissions error |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |

You can make a POST request to `owned_pages` edge from the following paths:

* [`/{business_id}/owned_pages`](https://developers.facebook.com/docs/marketing-api/reference/business/owned_pages/)

When posting to this edge, a [Page](https://developers.facebook.com/docs/graph-api/reference/page/) will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `entry_point`<br><br>string | entry point of claiming BusinessClaimAssetEntryPoint |
| `page_id`<br><br>Page ID | Page ID.<br><br>Required |