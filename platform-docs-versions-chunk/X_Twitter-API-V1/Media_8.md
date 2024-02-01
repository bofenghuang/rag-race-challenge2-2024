platform: X
topic: Twitter-API-V1
subtopic: Media
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Media.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/media/upload-media/uploading-media/media-best-practices

## Animated GIF recommendations

A GIF may fail during Tweet creation even if it is within the file size limit. Adhere to the following constraints to improve success rates.

* Resolution should be <= 1280x1080 (width x height)
* Number of frames <= 350
* Number of pixels (width \* height \* num\_frames) <= 300 million
* File size <= 15Mb

In order to process larger GIFs, use the [chunked upload endpoint](https://developer.twitter.com/en/docs/media/upload-media/api-reference/post-media-upload-init.html) with the `media_category` parameter. This allows the server to process the GIF file asynchronously, which is a requirement for processing larger files. Pass `media_category=tweet_gif` to enable async upload behavior for Tweets with an animated GIF.