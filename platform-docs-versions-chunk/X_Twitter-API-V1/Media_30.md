platform: X
topic: Twitter-API-V1
subtopic: Media
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Media.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/media/upload-media/api-reference/post-media-upload


## Usage[¶](#usage "Permalink to this headline")

This is a simple image upload endpoint with a limited set of features. The preferred alternative is the chunked upload endpoint which supports both images and videos, provides better reliability, allows resumption of file uploads, and other important features. In the future, new features will only be supported for the chunked upload endpoint.

* See the [Uploading media guide](https://developer.twitter.com/en/docs/media/upload-media/uploading-media/media-best-practices) for constraints and requirements on media files.
* See the [Uploading Media tutorial](https://developer.twitter.com/en/docs/tutorials/uploading-media) for step-by-step instructions on uploading an image.
* Use the [media metadata endpoint](https://developer.twitter.com/en/docs/media/upload-media/api-reference/post-media-metadata-create) to provide image alt text information.
* Ensure the POST is a `multipart/form-data` request. Either upload the raw binary (`media` parameter) of the file, or its base64-encoded contents (`media_data` parameter). Use raw binary when possible, because base64 encoding results in larger file sizes
* The response provides a media identifier in the `media_id` (64-bit integer) and `media_id_string` (string) fields. Use the `media_id_string` provided in the API response from JavaScript and other languages that cannot accurately represent a long integer.
* The returned `media_id` and `media_key` are only valid for `expires_after_secs` seconds. Any attempt to use either after this time period in other endpoints will result in an HTTP 4xx Bad Request.
* The `additional_owners` field enables media to be uploaded as user A and then used to create Tweets as user B.
* Please note that to upload videos or GIFs (`tweet_video`, `amplify_video`, and `tweet_gif`), you need to use the [chunked upload end-point](https://developer.twitter.com/en/docs/media/upload-media/api-reference/post-media-upload-init).