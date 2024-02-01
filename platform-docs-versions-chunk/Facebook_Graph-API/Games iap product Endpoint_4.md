platform: Facebook
topic: Graph-API
subtopic: Games iap product Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Games iap product Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/games-iap-product/


### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | The id of the object |
| `description`<br><br>string | Description of the product (e.g. "Used as in-app currency")<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `image_uri`<br><br>string | The associated image of the product for the Facebook Pay dialog<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `local_price_amount_cents`<br><br>integer | Local price of the product in 1/100ths of the major unit of currency (e.g. 1 JPY -> 100, 1.23 USD -> 123)<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `local_price_formatted`<br><br>string | Human-readable local price of the product (e.g. "$1.23")<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `price`<br><br>string | Human-readable price of the product (e.g. "$1.23")<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `price_amount_cents`<br><br>unsigned int32 | Price of the product in 1/100ths of the major unit of currency (e.g. 1 JPY -> 100, 1.23 USD -> 123)<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `price_currency_code`<br><br>string | Currency code of price (e.g. "JPY", "USD")<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `product_id`<br><br>string | Identifier for the product (e.g. "gold\_bar")<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `product_type`<br><br>enum | Type of the product (e.g. managed)<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `subscription_term`<br><br>enum | The subscription renewal length of time if ProductType is SUBSCRIPTION<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `title`<br><br>string | Title of the product displayed to the user (e.g. "Gold Bar")<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |