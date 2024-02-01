platform: X
topic: Twitter-API-V1
subtopic: Media
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Media.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/media/upload-media/api-reference/post-media-upload

POST media/upload

post-media-upload

# POST media/upload

## Overview[¶](#overview "Permalink to this headline")

Use this endpoint to upload images to Twitter.

This endpoint returns a `media_id` by default and can optionally return a `media_key` when a `media_category` is specified. These values are used by Twitter endpoints that accept images.

For example, a `media_id` value can be used to create a Tweet with an attached photo using the [POST statuses/update](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-update#post-statuses-update) endpoint.

All [Ads API endpoints](https://developer.twitter.com/en/docs/ads/) require a `media_key`. For example, a `media_key` value can be used to create a Draft Tweet with a photo using the [POST accounts/:account\_id/draft\_tweets](https://developer.twitter.com/en/docs/ads/creatives/api-reference/draft-tweets) endpoint.