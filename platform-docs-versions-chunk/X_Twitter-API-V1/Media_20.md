platform: X
topic: Twitter-API-V1
subtopic: Media
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Media.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/media/upload-media/api-reference/post-media-upload-append

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| command | required | Must be set to `APPEND` (case sensitive). |     |     |
| media\_id | required | The `media_id` returned from the `INIT` command. |     |     |
| media | required | The raw binary file content being uploaded. It must be <= 5 MB, and cannot be used with `media_data`. |     |     |
| media\_data | required | The base64-encoded chunk of media file. It must be <= 5 MB and cannot be used with `media`. Use raw binary (media parameter) when possible. |     |     |
| segment\_index | required | An ordered index of file chunk. It must be between 0-999 inclusive. The first segment has index 0, second segment has index 1, and so on. |     |     |