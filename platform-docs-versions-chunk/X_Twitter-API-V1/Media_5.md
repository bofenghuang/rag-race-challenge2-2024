platform: X
topic: Twitter-API-V1
subtopic: Media
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Media.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/media/upload-media/uploading-media/media-best-practices


## Keep in mind

* Because the method uses multipart POST, [OAuth](https://developer.twitter.com/en/docs/basics/authentication/guides/creating-a-signature) is handled differently. POST or query string parameters are not used when calculating an OAuth signature basestring or signature. Only the `oauth_*` parameters are used.
* You may attach up to 4 photos, 1 animated GIF or 1 video in a Tweet.
* The image passed should be the raw binary of the image or binary base64 encoded, no need to otherwise encode or escape the contents as long as the Content-Type is set appropriately (when in doubt: `application/octet-stream`).
* When posting base64 encoded images, be sure to set the “Content-Transfer-Encoding: base64” on the image part of the message.
* Multi-part message boundaries must be on their own line and terminated by a CRLF.
* For working examples of how to POST using this endpoint, we recommend testing with [twurl](https://github.com/twitter/twurl). Also, take a look at the [Twitter Libraries](https://developer.twitter.com/en/docs/developer-utilities/twitter-libraries.html) available, including the [large-video-upload-python](https://github.com/twitterdev/large-video-upload-python) library.
* Use the `media_id_string` provided in the API response for Javascript and any other languages that cannot accurately represent a long integer.