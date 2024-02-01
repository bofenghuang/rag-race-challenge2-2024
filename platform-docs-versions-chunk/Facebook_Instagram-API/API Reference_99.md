platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/available_catalogs


### Requirements

| Type | Requirement |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens/) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) |
| [Business Roles](https://www.facebook.com/business/help/442345745885606) | The app user must have an admin role on the [Business Manager](https://business.facebook.com/) that owns the IG User's [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322&h=AT3Verai7xEBsSSrJxHlMAeUXvw5a9EQjgGiidgzXfUuhEbhTn-wk9lDC3n8-vIVVeXLsqjkYKvfgRCViGD4FAiZPPZZBbsH-DyE4oHEt0loyT3t3OpnpcJzPxYHRH8-Amt1aPD256wx6NK2). |
| [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT2aXvknGdhMgE8niSqCm2edpTlzw-XbWb5YJD76xQcJxrz_ApC2ohwGiYgiIkzlFfenfxbXDPh8xAtGpaYIlz7I96tsXI6EAt-SgrNjgJ5JLmlyI0jP1qs6ufaxapc9ExdK81JDeg7uQwjE) | The IG User must have an approved [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT2ehkom6mRJNmzGPK12_eG3zCASg0GGCd9a3jIGNlfvoqv5D4uXoeLduZxYAAYtWPH_J4TPn54JrSntm9QMIT6udG0vzkvl4rMnDnbkM6jLVDZdM2-1wCfAWW7STIqzBrX5cZyhK9mFWmPC) with a product catalog containing products. |
| [Permissions](https://developers.facebook.com/docs/permissions/reference) | [`catalog_management`](https://developers.facebook.com/docs/permissions/reference/catalog_management)  <br>[`instagram_basic`](https://developers.facebook.com/docs/permissions/reference/instagram_basic)  <br>[`instagram_shopping_tag_products`](https://developers.facebook.com/docs/permissions/reference/instagram_shopping_tag_products)  <br>[`pages_show_list`](https://developers.facebook.com/docs/permissions/reference/pages_show_list)<br><br>  <br><br>If the app user was granted a role via the Business Manager on the [Page](https://developers.facebook.com/docs/instagram-api/overview#pages) connected to the targeted IG User, you will also need one of:<br><br>  <br><br>[`ads_management`](https://developers.facebook.com/docs/permissions/reference/ads_management)  <br>[`business_management`](https://developers.facebook.com/docs/permissions/reference/business_management) |