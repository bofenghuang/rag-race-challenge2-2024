platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/content-publishing

## Story Posts

Only business accounts can publish stories with the Content Publising API at this time.

Stories are videos and images that are posted as IG stories on Instagram. To publish a story, follow the same steps for publishing a single media post and include the `media_type=STORIES` parameter along with the path to the image/video using the `image_url` or `video_url` parameter.

**Note:** Stories are not a new media type even though you are setting `media_type=STORIES` when publishing a story. If you publish a story and then request its `media_type` field, the value will be returned as `IMAGE/VIDEO`. To determine if a published image/video has been designated as a story, request its `media_product_type` field instead.

[](#)