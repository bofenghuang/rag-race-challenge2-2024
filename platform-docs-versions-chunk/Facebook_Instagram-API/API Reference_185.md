platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/product_appeal


### Requirements

| Type | Requirement |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens/) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) |
| [Business Roles](https://www.facebook.com/business/help/442345745885606) | The app user must have an admin role on the [Business Manager](https://business.facebook.com/) that owns the IG User's [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322&h=AT1hQt8zAbLZJKPOWYcn6Du1XTXxuIygg4TFup-a4bXWZu2VMjieheAyTLU0hBYBLtmbrrRBlv2PhOorZERO4GjLFt8MBJN3z8UNB0SdcVMcAkwtuxjwauGNE_zROTWrmCVcUfsdnwqeHAOP). |
| [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT3a-5FpXbkYSBo_AfIsAMvrnuT2r4PjUQlJxF_LNQEfgfu-IHDLAsa_sKnXhOllie0JTmTJWZxayMhoFTVQpvbCZrWFETcNx3ISaW0zjxSyeB5aGe1AqmeggpzkCaC8lPaJnmiXUMcJ7AC3) | The IG User must have an approved [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT23KONXU81JFYcBiZ6IX091A9r6RNRvs58wD4U-ZfM-2ctuSv-0batjpWhOTTu45pp8jcYJBFf0R7F3RY4gfIBNfX3hgh6hG1VORVRjqMFQwJvB9igOe1nxmz5zOHI_4g2WMpkUlhd8rTC3) with a product catalog containing products. |
| [Permissions](https://developers.facebook.com/docs/permissions/reference) | [`catalog_management`](https://developers.facebook.com/docs/permissions/reference/catalog_management)  <br>[`instagram_basic`](https://developers.facebook.com/docs/permissions/reference/instagram_basic)  <br>[`instagram_shopping_tag_products`](https://developers.facebook.com/docs/permissions/reference/instagram_shopping_tag_products)  <br>[`pages_show_list`](https://developers.facebook.com/docs/permissions/reference/pages_show_list)<br><br>  <br><br>If the app user was granted a role via the Business Manager on the [Page](https://developers.facebook.com/docs/instagram-api/overview#pages) connected to the targeted IG User, you will also need one of:<br><br>  <br><br>[`ads_management`](https://developers.facebook.com/docs/permissions/reference/ads_management)  <br>[`business_management`](https://developers.facebook.com/docs/permissions/reference/business_management) |