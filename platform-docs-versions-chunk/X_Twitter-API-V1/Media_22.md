platform: X
topic: Twitter-API-V1
subtopic: Media
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Media.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/media/upload-media/api-reference/get-media-upload-status

GET media/upload (STATUS)

get-media-upload-status

# GET media/upload (STATUS)

## Overview[¶](#overview "Permalink to this headline")

The `STATUS` command is used to periodically poll for updates of media processing operation. After the `STATUS` command response returns `succeeded`, you can move on to the next step which is usually create Tweet with media\_id.

## Request[¶](#request "Permalink to this headline")

It should be a HTTP GET request with url params.

**Note:** The domain for this endpoint is **upload.twitter.com**

## Response[¶](#response "Permalink to this headline")

The response body contains `processing_info` field which provides information about current state of media processing operation. It contains a `state` field which has transition flow: “pending” -> “in\_progress” -> \[“failed” | “succeeded”\]. You can not use the media\_id to create Tweet or other entities before the state field is set to “succeeded”.