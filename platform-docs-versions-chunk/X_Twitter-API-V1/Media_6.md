platform: X
topic: Twitter-API-V1
subtopic: Media
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Media.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/media/upload-media/uploading-media/media-best-practices

## Media Categories

The Media Category parameter defines the use case of the media file to be uploaded, and can affect file size limits or other constraints enforced for media uploads. It’s important to use the correct media category when uploading media to avoid problems when trying to use the media. It is an optional value passed in the INIT request as part of the upload flow. If media category is not specified, the uploaded media is assumed to be a Tweet media (image, video, or GIF), depending on the content type.

The most common media categories are as follows:

* `tweet_image`
* `tweet_video`
* `tweet_gif`
* `dm_image`
* `dm_video`
* `dm_gif`
* `subtitles`

If you are an Ads API partner please refer to [these docs](https://developer.twitter.com/en/docs/ads/creatives/overview/promoted-video-overview) for more information on recommended media category for promoted video.