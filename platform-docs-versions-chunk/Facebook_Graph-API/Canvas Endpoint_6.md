platform: Facebook
topic: Graph-API
subtopic: Canvas Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Canvas Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/canvas/

### Parameters

| Parameter | Description |
| --- | --- |
| `background_color`<br><br>string | Background color of the canvas |
| `body_element_ids`<br><br>list<numeric string or integer> | A list of canvas element ids |
| `enable_swipe_to_open`<br><br>boolean | Field used to mark if swipe to open is enabled |
| `is_hidden`<br><br>boolean | Field used to hide a (published) canvas |
| `is_published`<br><br>boolean | Field used to mark the publish state of the canvas |
| `name`<br><br>string | Field used to label the canvas |
| `source_template_id`[](#)<br><br>numeric string or integer | ID of EntRichMediaDocumentTemplate that the Canvas document is created from |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |