platform: Facebook
topic: Graph-API
subtopic: Canvas Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Canvas Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/canvas-product-list/

### Parameters

| Parameter | Description |
| --- | --- |
| `bottom_padding`<br><br>float | The padding below the product list |
| `item_description`<br><br>string | A token to represent which field from the product to show in the product description |
| `item_headline`<br><br>string | A token to represent which field from the product to show in the product headline |
| `name`<br><br>string | Name of the product list element |
| `product_id_list`<br><br>list<int64> | A list of product ids inside the canvas<br><br>Required |
| `top_padding`<br><br>float | The padding above the product list |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |