platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/media

# IG User Media

Represents a collection of [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects on an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user).

Beginning November 9, 2023, the `VIDEO` value for `media_type` will no longer be supported. Use the `REELS` media type to publish a video to your feed.

## Creating

**`POST /{ig-user-id}/media`**

* Create an image, carousel, story or reel [IG Container](https://developers.facebook.com/docs/instagram-api/reference/ig-container) for use in the post publishing process. See the [Content Publishing](https://developers.facebook.com/docs/instagram-api/guides/content-publishing) guide for complete publishing steps.