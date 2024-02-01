platform: X
topic: Twitter-API-V1
subtopic: Media
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Media.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/media/upload-media/overview


## Creation

Objects such as Tweets, Direct Messages, user profile pictures, hosted Ads cards, etc. can contain one or more media objects. These top-level objects are collectively known as entities. The relevant entity creation API (e.g. [POST statuses/update](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-update.html)) can be passed one or more media objects using a unique media\_id.

An entity which contains media object(s) can be created by following these steps:

1. Upload the media file(s) using either the recommended [chunked](https://developer.twitter.com/content/developer-twitter/en/docs/media/upload-media/uploading-media/chunked-media-upload) upload (images/GIF/video), or the older [simple](https://developer.twitter.com/en/docs/media/upload-media/api-reference/post-media-upload.html) upload (images only).
2. Receive a media\_id from step 1. This step may be repeated multiple times with different media if the entity allows multiple media\_id parameters to be passed in.
3. Create the entity by calling the appropriate endpoint, including the media\_id and other required parameters. For example, attach a media\_id to a Tweet using the [POST statuses/update](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-update.html) endpoint.