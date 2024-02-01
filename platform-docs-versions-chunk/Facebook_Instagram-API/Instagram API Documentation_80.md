platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/product-tagging


## Get Catalogs

Use the [IG User Available Catalogs](https://developers.facebook.com/docs/instagram-api/reference/ig-user/available_catalogs) endpoint to get the Instagram Business account's product catalog.

GET /{ig\-user\-id}/available\_catalogs

Returns an array of catalogs and their metadata. Responses can include the following catalog fields:

* `catalog_id` — Catalog ID.
* `catalog_name` — Catalog name.
* `shop_name` — Shop name.
* `product_count` — Total number of products in the catalog.

#### Limitations

Collaborative catalogs such as shopping partner catalogs or affiliate creator catalogs are not supported.

#### Sample Request

curl \-i \-X GET \\
 "https://graph.facebook.com/`v19.0`/90010177253934?fields=available\_catalogs&access\_token=EAAOc..."

#### Sample Response

{
  "available\_catalogs": {
    "data": \[
      {
        "catalog\_id": "960179311066902",
        "catalog\_name": "Jay's Favorite Snacks",
        "shop\_name": "Jay's Bespoke",
        "product\_count": 11
      }
    \]
  },
  "id": "90010177253934"
}

[](#)