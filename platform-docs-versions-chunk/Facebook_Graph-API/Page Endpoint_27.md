platform: Facebook
topic: Graph-API
subtopic: Page Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Page Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/page/

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
| 370 | Invalid call to update this page |
| 371 | Invalid Page location update |
| 210 | User not visible |
| 375 | This Page doesn't have a location descriptor. Add one to continue. |
| 320 | Photo edit failure |
| 374 | Invalid store location descriptor update since this Page is not a location Page. |
| 160 | Invalid geolocation type |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |

You can update a [Page](https://developers.facebook.com/docs/graph-api/reference/page/) by making a POST request to [`/{page_id}/page_whatsapp_number_verification`](https://developers.facebook.com/docs/graph-api/reference/page/page_whatsapp_number_verification/).