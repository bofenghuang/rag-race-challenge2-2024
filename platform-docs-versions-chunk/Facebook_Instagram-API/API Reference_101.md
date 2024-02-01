platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/available_catalogs

### Response

A JSON-formatted object containing the data you requested.

{
  "data": \[
    {
      "catalog\_id": "{catalog-id}",
      "catalog\_name": "{catalog-name}",
      "shop\_name": "{shop-name}",
      "product\_count": {product-count}
    }
  \]
}

#### Response Contents

| Property | Value |
| --- | --- |
| `catalog_id` | Catalog ID. |
| `catalog_name` | Catalog name. |
| `shop_name` | Shop name. |
| `product_count` | Number of products in catalog. Includes all products regardless of review status. |

### cURL Example

#### Request

curl -i -X GET \\
 "https://graph.facebook.com/`v19.0`/90010177253934/available\_catalogs?access\_token=EAAOc..."

#### Response

{
  "data": \[
    {
      "catalog\_id": "960179311066902",
      "catalog\_name": "Jay's Favorite Snacks",
      "shop\_name": "Jay's Bespoke",
      "product\_count": 11
    }
  \]
}

## Updating

This operation is not supported.