platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/product-tagging


## Requirements

* Refer to each endpoint's reference document to determine which permissions, features, and [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) access tokens are required for each operation.
* The Instagram Business account (IG User) that owns the IG Media (to be tagged) must have an approved [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT2wUtxcrJ99eIerp7ryBDpR4QXqsjvS_r4ZZzECVgtE3wh0Om3_TVsDzj_LmPiGVTnRwp9-gzGVBfCRPcR1unSO-zpGFfp4MG2g6JnIAjkdnfezHF5wOUM-sceoTdq0eF1LRL01ftabzSDRCP_3lg) with a product catalog containing products. In-app and external Instagram Shop [checkout methods](https://www.facebook.com/business/help/449169642911614) are supported.
* The app user must have an [admin role](https://www.facebook.com/business/help/442345745885606) on the [Business Manager](https://business.facebook.com/) that owns the Instagram Shop whose products are being used to tag media.
* In order to request [App Review](https://developers.facebook.com/docs/app-review) approval for the [`instagram_shopping_tag_products`](https://developers.facebook.com/docs/permissions/reference/instagram_shopping_tag_products) and [`catalog_management`](https://developers.facebook.com/docs/permissions/reference/catalog_management) permissions, which are required by several product tagging endpoints, your app must be associated with a [verified business](https://developers.facebook.com/docs/development/release/business-verification).

[](#)