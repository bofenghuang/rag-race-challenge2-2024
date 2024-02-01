platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/media


### Requirements

| Type | Description |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) |
| [Business Roles](https://www.facebook.com/business/help/442345745885606) | If creating containers for [product tagging](https://developers.facebook.com/docs/instagram-api/guides/product-tagging), the app user must have an admin role on the [Business Manager](https://business.facebook.com/) that owns the IG User's [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322&h=AT0tdtPbQP9XYMNtSKl1t6rs9rg2rG9rbrtbWSlxQBecJiAXDq3FH-GnVB2Lbq7T5XBwTO2LU2itf86EPqDOTLaUG6hIaBDAbk9oZJJ1RZuwE2umZRbKK6n5ijzKigVFgyDbGT-sAWZDcrBR). |
| [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT29F5phorn0Eg1Wh5dmg6FQjQQYipftrylLPgHKfiG1BCSA7Ivkz6SuB6JPNAsYyJvzI2y3E6UvB728OHfF81VYpGne31KI2v7Pp7HtckmK44YLwjuSAjOLc-5gi6lT_b9Yja6alwYO8GCQ) | If creating containers for [product tagging](https://developers.facebook.com/docs/instagram-api/guides/product-tagging), the IG User must have an approved [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT2MleGsZjg2jCX99T_QREy3ZjocvfgaiZ5vJhhgRA-nTN6dP-GY660B1rkiLuvi_VRYiHBEiVxNrcgfY7KGsjkNJJxFM8xmZhMYMxAlIrf8lfMbRplBqmrTpwE983dXhy4z_nxcAoX5TO62) with a product catalog containing products. |
| [Permissions](https://developers.facebook.com/docs/apps/review/login-permissions) | [`instagram_basic`](https://developers.facebook.com/docs/facebook-login/permissions#reference-instagram_basic)  <br>[`instagram_content_publish`](https://developers.facebook.com/docs/permissions/reference/instagram_content_publish)  <br>[`pages_read_engagement`](https://developers.facebook.com/docs/facebook-login/permissions#reference-pages_read_engagement) or [`pages_show_list`](https://developers.facebook.com/docs/facebook-login/permissions#reference-pages_show_list)<br><br>  <br><br>If the app user was granted a role on the Page via the Business Manager, you will also need one of:<br><br>  <br><br>[`ads_management`](https://developers.facebook.com/docs/permissions/reference/ads_management)  <br>[`business_management`](https://developers.facebook.com/docs/permissions/reference/business_management)<br><br>  <br><br>If creating containers for [product tagging](https://developers.facebook.com/docs/instagram-api/guides/product-tagging), you will also need:<br><br>  <br><br>[`catalog_management`](https://developers.facebook.com/docs/permissions/reference/catalog_management)  <br>[`instagram_shopping_tag_products`](https://developers.facebook.com/docs/permissions/reference/instagram_shopping_tag_products) |
| [Tasks](https://developers.facebook.com/docs/instagram-api/overview#tasks) | The app user whose token is used in the request must be able to perform `MANAGE` or `CREATE_CONTENT` tasks on the [Page](https://developers.facebook.com/docs/instagram-api/overview#pages) connected to the targeted Instagram account. |