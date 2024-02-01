platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-update_with_media


# POST statuses/update\_with\_media (deprecated)

**This endpoint has been DEPRECATED should no longer be used. This endpoint does not support multiple images, animated GIFs, or video.** Replacement method: follow the [Uploading media guide](https://developer.twitter.com/en/docs/media/upload-media/overview) to upload one or more media entities, and then use [POST statuses/update](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-update) to attach them to a Tweet.

Updates the authenticated user's current status and attaches media for upload. This creates a Tweet with a (single) picture attached.

Unlike [POST statuses/update](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-update), this method expects raw multipart data. The POST request's `content-type` should be set to `multipart/form-data` with the `media[]` parameter.

The Tweet text will be rewritten to include the media URL(s), which will reduce the number of characters allowed in the Tweet text. If the URL(s) cannot be appended without text truncation, the Tweet will be rejected and this method will return an HTTP 403 error.

Users are limited to a specific daily media upload limit. Requests to this endpoint will return the following headers with information regarding the user's current media upload limits:

* `x-mediaratelimit-limit` - Indicates the total pieces of media the current user may upload before the time indicated in `x-mediaratelimit-reset`.
* `x-mediaratelimit-remaining` - The remaining pieces of media the current user may upload before the time indicated in `x-mediaratelimit-reset`.
* `x-mediaratelimit-reset` - A UTC-based timestamp (in seconds) indicating when `x-mediaratelimit-remaining` will reset to the value in `x-mediaratelimit-limit` and the user can resume uploading media.

If the user is over the daily media limit, this method will return an HTTP 403 error. In addition to media upload limits, the user is also limited in the number of statuses they can publish daily. If the user tries to exceed the number of updates allowed, this method will also return an HTTP 403 error, similar to [POST statuses/update](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-update).

There is a 30 second timeout for this endpoint, so network latency may prevent media being posted successfully.

OAuth is handled differently for POST messages. See [Uploading Media](https://developer.twitter.com/en/docs/media/upload-media/overview) for more details on this.