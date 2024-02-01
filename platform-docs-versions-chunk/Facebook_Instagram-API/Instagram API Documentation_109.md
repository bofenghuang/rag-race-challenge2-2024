platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/changelog

## June 28, 2022

#### Reels

_Applies to all versions._

Reels are now supported. To publish a video as a reel, set the `media_type` parameter to `REELS` when creating a [single media post](https://developers.facebook.com/docs/instagram-api/guides/content-publishing#single-media-posts) container. Refer to the [`POST /ig-user/media endpoint`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media#creating) reference to learn which parameters can be used with reels as well as requirements for reels videos.

**Note:** Beginning November 9, 2023, the `VIDEO` value for `media_type` will no longer be supported. Use the `REELS` media type to publish a video to your feed.

[](#)