platform: X
topic: Twitter-API-V1
subtopic: Media
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Media.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/media/upload-media/api-reference/post-media-upload-init

POST media/upload (INIT)

post-media-upload-init

# POST media/upload (INIT)

## Overview[¶](#overview "Permalink to this headline")

The `INIT` command request is used to initiate a file upload session. It returns a `media_id` which should be used to execute all subsequent requests. The next step after a successful return from INIT command is the [APPEND command](https://developer.twitter.com/en/docs/media/upload-media/api-reference/post-media-upload-append).

See the [Uploading media guide](https://developer.twitter.com/en/docs/media/upload-media/uploading-media/media-best-practices) for constraints and requirements on media files.

## Request[¶](#request "Permalink to this headline")

Requests should be either `multipart/form-data` or `application/x-www-form-urlencoded` POST formats.

**Note:** The domain for this endpoint is **upload.twitter.com**