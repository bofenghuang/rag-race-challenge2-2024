platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/catalog_product_search

### cURL Example

#### Request

curl -i -X GET \\
 "https://graph.facebook.com/`v19.0`/90010177253934/catalog\_product\_search?catalog\_id=960179311066902&q=gummy&access\_token=EAAOc"

#### Response

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

## Updating

This operation is not supported.