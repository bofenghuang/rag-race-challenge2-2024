platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/changelog

## May 5, 2020

* **Hashtag Search** — _This change applies to v7.0+_ — You can now request the `timestamp` field on [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media/) returned by [`GET /{ig-hashtag-id}/top_media`](https://developers.facebook.com/docs/instagram-api/reference/ig-hashtag/top-media#reading) and [`GET /{ig-hashtag-id}/recent_media`](https://developers.facebook.com/docs/instagram-api/reference/ig-hashtag/recent-media#reading) [Hashtag Search](https://developers.facebook.com/docs/instagram-api/guides/hashtag-search) queries. For example: `GET /{ig-hashtag-id}/top_media?fields=timestamp`.

[](#)

## December 3, 2019

* **Insights** — To align API behavior with Instagram app behavior, insights on [IG Users](https://developers.facebook.com/docs/instagram-api/reference/ig-user/) are now only available on IG Users that have 100 or more followers.

[](#)