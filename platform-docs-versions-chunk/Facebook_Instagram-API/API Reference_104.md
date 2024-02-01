platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/business_discovery

### Query String Parameters

* `{username}` (required) — The username of the Instagram Business or Creator [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) you want to get data about.

### Permissions

A Facebook User [access token](https://developers.facebook.com/docs/instagram-api/overview#authentication) with the following permissions:

* `instagram_basic`
* `instagram_manage_insights`
* `pages_read_engagement` or `pages_show_list`

If the token is from a User whose **Page role was granted via the Business Manager**, one of the following permissions is also required:

* `ads_management`
* `pages_read_engagement`
* `business_management`

### Field Expansion

You can use field expansion get public fields on the targeted [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user). Refer to the [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) reference for a list of public fields.