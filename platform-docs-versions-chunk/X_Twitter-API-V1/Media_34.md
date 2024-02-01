platform: X
topic: Twitter-API-V1
subtopic: Media
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Media.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/media/upload-media/api-reference/post-media-metadata-create

POST media/metadata/create

post-media-metadata-create

# POST media/metadata/create

## Overview[¶](#overview "Permalink to this headline")

This endpoint can be used to provide additional information about the uploaded `media_id`. This feature is currently only supported for images and GIFs.

The request flow should be:

1. Upload media using either the [simple upload endpoint](https://developer.twitter.com/en/docs/media/upload-media/api-reference/post-media-upload) or the (preferred) [chunked upload endpoint](https://developer.twitter.com/en/docs/media/upload-media/api-reference/post-media-upload-init).
2. Call this endpoint to attach additional metadata such as image alt text.
3. Create Tweet with `media_id(s)` attached.

## Request[¶](#request "Permalink to this headline")

Requests should be HTTP POST with a JSON content body, and Content-Type `application/json; charset=UTF-8` or `text/plain; charset=UTF-8`.

**Note:** The domain for this endpoint is **upload.twitter.com**