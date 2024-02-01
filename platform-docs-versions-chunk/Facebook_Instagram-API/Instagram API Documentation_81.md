platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/product-tagging


## Get Eligible Products

Use the [IG User Catalog Product Search](https://developers.facebook.com/docs/instagram-api/reference/ig-user/catalog_product_search) endpoint to get a collection of products in the catalog that can be used to tag media. Product variants are supported.

Although the API will not return an error when publishing a post tagged with an unapproved product, the tag will not appear on the published post until the product has been approved. Therefore, we recommend that you only allow your app users to publish posts with tags whose products have a `review_status` of `approved`. This field is returned for each product by default when you get an app user's eligible products.

GET /{ig\-user\-id}/catalog\_product\_search

#### Parameters

* `catalog_id` — **(required)** Catalog ID.
* `q` — A string to search for in each product's name, or a product's SKU number (the **Content ID** column in the catalog management interface). If no string is specified, all tag-eligible products will be returned.

Returns an object containing an array of tag-eligible products and their metadata. Supports [cursor-based pagination](https://developers.facebook.com/docs/graph-api/results#cursors). Responses can include the following product fields:

* `image_url` — Product image URL.
* `is_checkout_flow` — If `true`, product can be purchased directly in the Instagram app. If `false`, product must be purchased in the app user's app/website.
* `merchant_id` — Merchant ID.
* `product_id` — Product ID.
* `product_name` — Product name.
* `retailer_id` — Retailer ID.
* `review_status` — Review status. Values can be `approved`, `outdated`, `pending`, `rejected`. An approved product can appear in the app user's [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT32AwtsjVX-D2WfqpME6AEjUIKSIL932NNQcbRTNDPeb4xf0uSmTeZXvqb0EC0cT9VaGzNkAhaE6jnIL_XDtFkS3G5CHk8fsVbb8Lp2AwKzZqkyvZYg0tCXlx_uJpp57GfA6v8i7Xd9DenDalww9A), but an approved status does not indicate product availability (e.g, the product could be out of stock). Only tags associated with products that have a `review_status` of `approved` can appear on published posts.
* `product_variants` — Product IDs (`product_id`) and variant names (`variant_name`) of [product variants](https://developers.facebook.com/docs/marketing-api/catalog/guides/product-variants).

#### Sample Request

curl \-i \-X GET \\
 "https://graph.facebook.com/`v19.0`/90010177253934/catalog\_product\_search?catalog\_id=960179311066902&q=gummy&access\_token=EAAOc..."

#### Sample Response

{
  "data": \[
    {
      "product\_id": 3231775643511089,
      "merchant\_id": 90010177253934,
      "product\_name": "Gummy Wombats",
      "image\_url": "https://scont...",
      "retailer\_id": "oh59p9vzei",
      "review\_status": "approved",
      "is\_checkout\_flow": true,
      "product\_variants": \[
            {
              "product\_id": 5209223099160494
            },
            {
              "product\_id": 7478222675582505,
              "variant\_name": "Green Gummy Wombats"
            }
          \]
    }
  \]
}

[](#)