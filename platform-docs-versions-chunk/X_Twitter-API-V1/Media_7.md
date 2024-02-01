platform: X
topic: Twitter-API-V1
subtopic: Media
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Media.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/media/upload-media/uploading-media/media-best-practices

## Image specifications and recommendations

Image files must meet all of the following criteria:

* Supported image media types: JPG, PNG, GIF, WEBP
* Image size <= 5 MB, animated GIF size <= 15 MB

The file size limit above is enforced by the media upload endpoint. In addition, there is a separate product entity specific file size limit which is applied when calling the Tweet creation (or similar) endpoints with `media_id`. The file size limit and other constraints may vary depending on the `media_category` parameter.