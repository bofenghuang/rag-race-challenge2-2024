platform: Facebook
topic: Graph-API
subtopic: Page Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Page Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/page/

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |

## Deleting

This is only available to select developers. Please contact your Facebook Partner for more information.

You can dissociate a [Page](https://developers.facebook.com/docs/graph-api/reference/page/) from a [Page](https://developers.facebook.com/docs/graph-api/reference/page/) by making a DELETE request to [`/{page_id}/locations`](https://developers.facebook.com/docs/graph-api/reference/page/locations/).

### Parameters

| Parameter | Description |
| --- | --- |
| `location_page_ids`<br><br>array<location\_page ID> | Array of Page IDs for the pages to delete<br><br>Required |
| `store_numbers`<br><br>array<int64> | Array of Store numbers for the pages to delete<br><br>Required |

### Return Type

Struct {

`status`: bool,

`data`: List \[

Struct {

`child_id`: string,

`success`: bool,

}

\],

}