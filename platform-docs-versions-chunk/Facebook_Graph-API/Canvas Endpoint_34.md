platform: Facebook
topic: Graph-API
subtopic: Canvas Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Canvas Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/canvas-product-set/

### Create a Collection Ads Product Set

To create a product set used in Collection ads from a set of products in Dynamic Ads:

`curl -F 'canvas_product_set={ "bottom_padding": 8, "max_items": 50, "name": "Collection Product Set Name", "product_set_id": "PRODUCT_SET_ID", "show_in_feed": true, "item_headline": "See more at {{product.brand | titleize}}", "item_description": "{{product.price}}", "retailer_item_ids": [ "RETAILER_ID_1", "RETAILER_ID_2", "RETAILER_ID_3", "RETAILER_ID_4", ], "top_padding": 24 }' \ -F 'access_token=ACCESS_TOKEN' \ https://graph.facebook.com/VERSION/PAGE_ID/canvas_elements`

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)