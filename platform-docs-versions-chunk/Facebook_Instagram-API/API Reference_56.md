platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-media/comments

# Comments

Represents a collection of [IG Comments](https://developers.facebook.com/docs/instagram-api/reference/ig-comment) on an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object.

### Non-Organic Comments

Comments on Ads containing IG Media (i.e. non-organic comments) are of a different type and are not supported. To get non-organic comments, use the [Marketing API](https://developers.facebook.com/docs/marketing-api/) and request the Ad's `effective_instagram_story_id`. You can then query the returned ID's `/comments` edge to get a collection of non-organic [Instagram Comments](https://developers.facebook.com/docs/graph-api/reference/instagram-comment/). Refer to the Marketing API's [Post Moderation](https://developers.facebook.com/docs/instagram/ads-api/guides/post-moderation) guide for more information.

## Creating