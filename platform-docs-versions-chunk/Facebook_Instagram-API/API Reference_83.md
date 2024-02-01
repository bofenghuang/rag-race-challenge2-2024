platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-media/product_tags


### Requirements

| Type | Requirement |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens/) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) |
| [Business Roles](https://www.facebook.com/business/help/442345745885606) | The app user must have an admin role on the [Business Manager](https://business.facebook.com/) that owns the IG User's [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322&h=AT0aoE5CXNHCuNpMbF2iLZfvJIL4N335-sXJANZtOvMFKJWs4mgBGTA-0VtZZZJ51gpydjcy7Mfb3-OxlcXlE4VsYhMmwIf7-QTqCtYTJS6IV4-fLJoBqia80lbiarJMkZ7fXAbLa1dRJfg-). |
| [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT1RzjUcoVkmDAcd1EsQicmaIokD2D8n_qTLDB2HSInH5dl_iDKBnRCsZ8XfrxRJsks5J0-IprDL2Hu7LGvGaubj7mBUYcAhV5Mf79GpjwPcx8D1030p6LpCznV7hC6PHnji36EuEAQS65E6) | The IG User that owns the IG Media must have an approved [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT14g4i_efn9PsybPvOa97qDcCXgGcFCHnxcf2SJgiTc6ul6ssZ6SnbqEtWySIEY-H8LJcavtNbm2pHxpxE5LZaxnegE3ZndEvtzYcekPYzELdslVeZiUpSGd0-PMN4Wu8DEzPgQiWq83U_O) with a product catalog containing products. |
| [Permissions](https://developers.facebook.com/docs/permissions/reference) | [`catalog_management`](https://developers.facebook.com/docs/permissions/reference/catalog_management)  <br>[`instagram_basic`](https://developers.facebook.com/docs/permissions/reference/instagram_basic)  <br>[`instagram_shopping_tag_products`](https://developers.facebook.com/docs/permissions/reference/instagram_shopping_tag_products)  <br>[`pages_show_list`](https://developers.facebook.com/docs/permissions/reference/pages_show_list)<br><br>  <br><br>If the app user was granted a role via the Business Manager on the [Page](https://developers.facebook.com/docs/instagram-api/overview#pages) connected to the targeted IG User, you will also need one of:<br><br>  <br><br>[`ads_management`](https://developers.facebook.com/docs/permissions/reference/ads_management)  <br>[`business_management`](https://developers.facebook.com/docs/permissions/reference/business_management) |