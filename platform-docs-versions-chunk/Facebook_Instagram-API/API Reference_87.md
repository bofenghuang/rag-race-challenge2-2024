platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-media/product_tags


### Requirements

| Type | Requirement |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens/) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) |
| [Business Roles](https://www.facebook.com/business/help/442345745885606) | The app user must have an admin role on the [Business Manager](https://business.facebook.com/) that owns the IG User's [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322&h=AT3UHxV7SmzluMkiCWS8iIJvNke6wbOvx0qZ4QLoeuAulUVYtjtrg_EiLQQeayT50w5LrllKwnMwlNLnfpbNhsc1mR4Ce5HPXGm59kOz17P357oprx84ZwiUMFpcmLD9YgkDC7j5cP27WJVx). |
| [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT1uLVBC2yZo05u49u_TUabN9QxBHJ7fvaGzAtKtg4OYBOp2FdzePW__IPxXXLy-tbg25vaaV0Fb4HH43WiqjKZlpuT5wR3DCHhncgIXRo33lW76jWHwAslruUYhijw02Zj2nVGmE7rC2_09) | The IG User that owns the IG Media must have an approved [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT1dS1zgKU_-oA8tyB8dSaURN6B6rFMMFvNpmkiAkEFsTgHayEwrBaX8uTghvX7poWu4tUtBajjS4hFvtLCzFqbtAVcVAOHEkBhRinkgIsHtJ3zA5fL29Ae8GOR7FRmRDPUAn0jRGNqgDbKX) with a product catalog containing products. |
| [Permissions](https://developers.facebook.com/docs/permissions/reference) | [`catalog_management`](https://developers.facebook.com/docs/permissions/reference/catalog_management)  <br>[`instagram_basic`](https://developers.facebook.com/docs/permissions/reference/instagram_basic)  <br>[`instagram_shopping_tag_products`](https://developers.facebook.com/docs/permissions/reference/instagram_shopping_tag_products)  <br>[`pages_show_list`](https://developers.facebook.com/docs/permissions/reference/pages_show_list)<br><br>  <br><br>If the app user was granted a role via the Business Manager on the [Page](https://developers.facebook.com/docs/instagram-api/overview#pages) connected to the targeted IG User, you will also need one of:<br><br>  <br><br>[`ads_management`](https://developers.facebook.com/docs/permissions/reference/ads_management)  <br>[`business_management`](https://developers.facebook.com/docs/permissions/reference/business_management) |