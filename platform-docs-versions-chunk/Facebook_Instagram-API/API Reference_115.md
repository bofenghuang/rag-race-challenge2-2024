platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/catalog_product_search


### Response

A JSON-formatted object containing an array of tag-eligible products and their metadata. Supports [cursor-based pagination](https://developers.facebook.com/docs/graph-api/results#cursors).

{
  "data": \[
    {
      "product\_id": {product-id},
      "merchant\_id": {merchant-id},
      "product\_name": "{product-name}",
      "image\_url": "{image-url}",
      "retailer\_id": "{retailer-id}",
      "review\_status": "{review-status}",
      "is\_checkout\_flow": {is-checkout-flow}
    }
  \]
}

#### Response Contents

| Property | Value |
| --- | --- |
| `product_id` | Product ID. |
| `merchant_id` | Merchant ID. |
| `product_name` | Product name. |
| `image_url` | Product image URL. |
| `retailer_id` | Retailer ID. |
| `review_status` | Review status. Values can be `approved`, `outdated`, `pending`, `rejected`. An approved product can appear in the app user's [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT0DnSKUCv2vbr3anwc9-FVfCN0FR_3gWJz_6cMNyzHPD9Y4Ppd4iT6DO2iEzM-UQZU9x9KIIR5svy_bRpwTpEUmTHwoThBFwkniesdV4fo4ZWLggZSR4FV95SkQL2Zft64r0heUpEMZmAuF), but an approved status does not indicate product availability (e.g, the product could be out of stock). Only tags associated with products that have a `review_status` of `approved` can appear on published posts. |
| `is_checkout_flow` | If `true`, product can be purchased directly in the Instagram app. If `false`, product must be purchased in the app user's app/website. |
| `product_variants` | Product IDs (`product_id`) and variant names (`variant_name`) of [product variants](https://developers.facebook.com/docs/marketing-api/catalog/guides/product-variants). |