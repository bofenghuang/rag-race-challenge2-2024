platform: X
topic: Twitter-API-V1
subtopic: Media
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Media.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/media/upload-media/api-reference/post-media-upload-finalize


## Response[¶](#response "Permalink to this headline")

The response provides a media identifier in the `media_id` (64-bit integer) and `media_id_string` (string) fields. Use the `media_id_string` provided in the API response from JavaScript and other languages that cannot accurately represent a long integer.

The returned mediaId is only valid for `expires_after_secs` seconds. Any attempt to use mediaId after this time period in other API calls will result in a Bad Request (HTTP 4xx) response.

If the response contains a `processing_info` field, then use the `STATUS` command to poll for the status of the `FINALIZE` operation. The async finalize approach is used for cases where media processing requires more time. In future, all video and animated GIF processing will only be supported using async finalize. This behavior is enabled if an upload session was [initialized](https://developer.twitter.com/en/docs/media/upload-media/api-reference/post-media-upload-init) with a media\_category parameter, and when then media type is either video or animated GIF.

If a `processing_info` field is NOT returned in the response, then `media_id` is ready for use in other API endpoints.