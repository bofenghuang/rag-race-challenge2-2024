platform: Facebook
topic: Graph-API
subtopic: Canvas Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Canvas Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/canvas-product-set/


### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | The id of the element |
| `bottom_padding`<br><br>numeric string | The padding below the element |
| `element_group_key`<br><br>string | The element group key to bundle multiple elements in editing |
| `element_type`<br><br>enum | The type of the element<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `image_overlay_spec`[](#)<br><br>[AdCreativeLinkDataImageOverlaySpec](https://developers.facebook.com/docs/marketing-api/reference/ad-creative-link-data-image-overlay-spec/) | How to render overlays over a product item |
| `item_description`<br><br>string | A token to represent which field from the product to show in the product description |
| `item_headline`<br><br>string | A token to represent which field from the product to show in the product headline |
| `max_products`<br><br>unsigned int32 | Maximum number of products to show |
| `name`<br><br>string | The name of the element<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `product_set_id`<br><br>numeric string | The product set id which contains a subset of products within a product catalog |
| `retailer_item_ids`<br><br>list<string> | An array of items that should be shown first in the product set element. If this is not set then products will be dynamically chosen |
| `show_in_feed`<br><br>bool | A flag that products should be shown in feed unit |
| `top_padding`<br><br>numeric string | The padding above the element |