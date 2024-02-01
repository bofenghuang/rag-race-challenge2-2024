platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-media/product_tags


### Requirements

| Type | Requirement |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens/) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) |
| [Business Roles](https://www.facebook.com/business/help/442345745885606) | The app user must have an admin role on the [Business Manager](https://business.facebook.com/) that owns the IG User's [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322&h=AT0hGjvVNUWtayU3WgwJ7nGTf_v62o-Veb_UqwiNqNm7apf953Mc0usPjgmy75JVHV-HOXePzdvFHDV2SD7T2XiAl9IhJTkkKgMnzg7Sd9jv1B8XiMi6MbBl1qGeL4ZJb_31ijnWJUMLTY3H). |
| [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT3Hpvb6nDODE1HwbvjLeYwXfz8ma4YKp7ENnwNjoyLlHI1WuIowdLlkF7WyZhhAxSDJD79cqCgh9ohtYSJ2otJBkvYPIkkKsStBdIXTJVjYHmHWhs3lkdV1djCLzxVrXUyhey7DGN7fC5NqR41ZqoitssFEcg) | The IG User that owns the IG Media must have an approved [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT1FkM50AL3DySRVu4QtdCTvB5JVwG8Q7IcoUv_L6RxyhGzLKw6rKa_IzFSyvthwRM-xZqQcsrL2muiNFykhNPC5E-K9uYABZR4sLhYiC0GcpaATN4-US2yPL6RPohQOxXAbgakkOjYoIG7-) with a product catalog containing products. |
| [Permissions](https://developers.facebook.com/docs/permissions/reference) | [`catalog_management`](https://developers.facebook.com/docs/permissions/reference/catalog_management)  <br>[`instagram_basic`](https://developers.facebook.com/docs/permissions/reference/instagram_basic)  <br>[`instagram_shopping_tag_products`](https://developers.facebook.com/docs/permissions/reference/instagram_shopping_tag_products)  <br>[`pages_show_list`](https://developers.facebook.com/docs/permissions/reference/pages_show_list)<br><br>  <br><br>If the app user was granted a role via the Business Manager on the [Page](https://developers.facebook.com/docs/instagram-api/overview#pages) connected to the targeted IG User, you will also need one of:<br><br>  <br><br>[`ads_management`](https://developers.facebook.com/docs/permissions/reference/ads_management)  <br>[`business_management`](https://developers.facebook.com/docs/permissions/reference/business_management) |