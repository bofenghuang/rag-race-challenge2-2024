platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-hashtag/top-media

# IG Hashtag Top Media

Represents a collection of the most popular photo and video [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects that have been tagged with a hashtag.

Popularity is determined by a mix of views and viewer interaction using the same methodology that determines the top posts when [searching for a hashtag](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.instagram.com%2Fexplore%2Ftags%2Fhalloween%2F&h=AT2-4wVLUXgSyQPuQkKt5oMAQky1NvIhe0pJTzFNP0WRaiipX_obOG_LvaRnG5xcm2A9p735KTip9dQF7b_VaF9j-66fQXT7pspOBW-qr0wuMSK-tyRsAX6UjSQzyybPSKLdJ5QxOGKdvyqn) on [www.instagram.com](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.instagram.com%2F&h=AT01rPdPfnqWYSb_gmKLx2W-AMLM8-DZd6p41wDGru4cQKK-O_mmIDouz4WS5GnNQ1jzhArLk2vmJJa7TuH5i6zjZhZE48lJMJkseKAQo4HM3xWgeTnFcoY9e1EVm9PAfmzrDZUceiddfIwP).

**v10.0 and older calls until September 7, 2021:** The [`like_count`](https://developers.facebook.com/docs/instagram-api/reference/ig-media#fields) field on an IG Media will return `0` if the media [owner](https://developers.facebook.com/docs/instagram-api/overview#authorization) has [hidden](https://www.facebook.com/help/instagram/113355287252104) like counts on it.

**v11.0+ calls, and all versions on September 7, 2021:** If indirectly querying an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) through another endpoint or field expansion, the [`like_count`](https://developers.facebook.com/docs/instagram-api/reference/ig-media#fields) field will be omitted from API responses if the media owner has hidden like counts on it. Directly querying the IG Media (which can only be done by the IG Media owner) will return the actual like count, however, even if like counts have been hidden.