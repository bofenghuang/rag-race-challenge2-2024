platform: X
topic: Twitter-API-V1
subtopic: Media
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Media.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/media/upload-media/api-reference/post-media-upload-init

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| command | required | Must be set to `INIT` (case sensitive). |     |     |
| total\_bytes | required | The size of the media being uploaded in bytes. |     |     |
| media\_type | required | The MIME type of the media being uploaded. |     | `video/mp4` |
| media\_category | sometimes | A string enum value which identifies a media usecase. This identifier is used to enforce usecase specific constraints (e.g. file size, video duration) and enable advanced features. |     |     |
| additional\_owners | optional | A comma-separated list of user IDs to set as additional owners allowed to use the returned `media_id` in Tweets or Cards. Up to 100 additional owners may be specified. |     |     |