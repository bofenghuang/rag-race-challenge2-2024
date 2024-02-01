platform: Facebook
topic: Graph-API
subtopic: Canvas Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Canvas Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/canvas-product-list/

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

## Creating

You can't perform this operation on this endpoint.

## Updating

Provide a list of products for the element. This must include more than four IDs. IDs must be from Dynamic Ads product catalog or Dynamic Ads for Travel, hotel catalog.

`curl \ -F 'bottom_padding=8' \ -F 'name=Product List Name' \ -F 'product_id_list=[product_id_1, product_id_2, product_id_3, product_id_4]' \ -F 'item_headline=See more at {{product.url}}' \ -F 'item_description={{product.current_price}}' \ -F 'top_padding=24' \ -F 'access_token=TOKEN' \ https://graph.facebook.com/VERSION/CANVAS_ELEMENT_PRODUCT_LIST_ID`  
  

You can update a [CanvasProductList](https://developers.facebook.com/docs/graph-api/reference/canvas-product-list/) by making a POST request to [`/{canvas_product_list_id}`](https://developers.facebook.com/docs/graph-api/reference/canvas-product-list/).