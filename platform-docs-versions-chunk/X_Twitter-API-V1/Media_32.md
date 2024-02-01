platform: X
topic: Twitter-API-V1
subtopic: Media
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Media.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/media/upload-media/api-reference/post-media-upload

## Parameters[¶](#parameters "Permalink to this headline")

| Name | Required | Description | Default Value | Example |
| --- | --- | --- | --- | --- |
| media | required | The raw binary file content being uploaded. Cannot be used with `media_data`. |     |     |
| media\_category | optional | The category that represents how the media will be used. This field is required when using the media with the Ads APIPossible values: `amplify_video`, `tweet_gif`, `tweet_image`, and `tweet_video` |     |     |
| media\_data | required | The base64-encoded file content being uploaded. Cannot be used with `media`. |     |     |
| additional\_owners | optional | A comma-separated list of user IDs to set as additional owners allowed to use the returned `media_id` in Tweets or Cards. Up to 100 additional owners may be specified. |     |     |

## Example Request[¶](#example-request "Permalink to this headline")

`POST https://upload.twitter.com/1.1/media/upload.json?media_category=tweet_image`