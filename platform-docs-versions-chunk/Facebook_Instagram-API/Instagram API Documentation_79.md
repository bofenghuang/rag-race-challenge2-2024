platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/product-tagging


## Get User Eligibility

Request the `shopping_product_tag_eligibility` field on the [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) endpoint to determine if the Instagram Business account has set up an [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT2aD-kcYOtEOFl14mmriXVjpTpQVnoKO-6-Y36FLTWXDEmvhZ2B7FcT6OYs6l5Yzs1RWWPHgustORbFGHXAEYLoMhq6qFm-q0s9Vc7AzJpRVVxvlfYDVntBR-RhGPcPp9I5dQW8uQ-RO1Rp-6Fjtg). Accounts that have not set up an Instagram Shop are ineligible for product tagging.

GET /{ig\-user\-id}?fields\=shopping\_product\_tag\_eligibility

Returns `true` if the Instagram Business account has been associated with a [Business Manager's](https://business.facebook.com/) approved Instagram Shop, otherwise returns `false`.

#### Sample Request

curl \-i \-X GET \\
 "https://graph.facebook.com/`v19.0`/90010177253934?fields=shopping\_product\_tag\_eligibility&access\_token=EAAOc..."

#### Sample Response

{
  "shopping\_product\_tag\_eligibility": true,
  "id": "90010177253934"
}

[](#)