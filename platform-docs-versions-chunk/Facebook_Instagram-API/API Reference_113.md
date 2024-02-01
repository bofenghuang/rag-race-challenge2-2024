platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/catalog_product_search


### Requirements

| Type | Requirement |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens/) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens/#usertokens) |
| [Business Roles](https://www.facebook.com/business/help/442345745885606) | The app user must have an admin role on the [Business Manager](https://business.facebook.com/) that owns the IG User's [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322&h=AT1tz02oi10gNZJnjItKLR3YM0tNpE4vEu344-AEnaOhBe0mK_9BcwwuQaF_C98jwhSQSMRpvAppqiIWSc7fX7mC4iwc5g2oKoGGcyguWoXQGuxfQrz4SpkvfXnuxUZ28Arzcwb6FzbQ4Q97). |
| [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT0Lhm6Mswai4tOICnSC1Ab1rvC-xm3XZOGgg1ivPT2rgLkkHJ8TgKaDYdOVdpP0R599Ehxp-3EjmDZIO72ywooK7_DIIen2SFCu3DQxO-_YBCTvj5pNiPmUJ3iYje_JHAgovpnf_kwFpE8t) | The IG User must have an approved [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT1paVsTRBevIj-Z6yZt1Bz-12YQD3f6t_xti-SVuaHw0Tola5nX3WfySOThDt0l_l2yu51ZdE9_rbQ4Osb4ztUDAS1q_HqlU_QdqTAtp9JjDWrnNOVfNPl0SPLVuYB042CT8CXL_PfBqCH8) with a product catalog containing products. |
| [Permissions](https://developers.facebook.com/docs/permissions/reference) | [`catalog_management`](https://developers.facebook.com/docs/permissions/reference/catalog_management)  <br>[`instagram_basic`](https://developers.facebook.com/docs/permissions/reference/instagram_basic)  <br>[`instagram_shopping_tag_products`](https://developers.facebook.com/docs/permissions/reference/instagram_shopping_tag_products)  <br>[`pages_show_list`](https://developers.facebook.com/docs/permissions/reference/pages_show_list)<br><br>  <br><br>If the app user was granted a role via the Business Manager on the [Page](https://developers.facebook.com/docs/instagram-api/overview#pages) connected to the targeted IG User, you will also need one of:<br><br>  <br><br>[`ads_management`](https://developers.facebook.com/docs/permissions/reference/ads_management)  <br>[`business_management`](https://developers.facebook.com/docs/permissions/reference/business_management) |