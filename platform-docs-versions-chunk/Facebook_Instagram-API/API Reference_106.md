platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/business_discovery


### Accessing Edges with Field Expansion

You can also use field expansion to access the `/media` edge on the targeted [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) and specify the fields and metrics that should be returned for each [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object. Refer to the [Media node reference](https://developers.facebook.com/docs/instagram-api/reference/ig-media) for a list of public fields.

**v10.0 and older calls until September 7, 2021:** The [`like_count`](https://developers.facebook.com/docs/instagram-api/reference/ig-media#fields) field on an IG Media will return `0` if the media [owner](https://developers.facebook.com/docs/instagram-api/overview#authorization) has [hidden](https://www.facebook.com/help/instagram/113355287252104) like counts on it.

**v11.0+ calls, and all versions on September 7, 2021:** If indirectly querying an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) through another endpoint or field expansion, the [`like_count`](https://developers.facebook.com/docs/instagram-api/reference/ig-media#fields) field will be omitted from API responses if the media owner has hidden like counts on it. Directly querying the IG Media (which can only be done by the IG Media owner) will return the actual like count, however, even if like counts have been hidden.