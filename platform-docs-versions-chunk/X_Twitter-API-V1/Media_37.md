platform: X
topic: Twitter-API-V1
subtopic: Media
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Media.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/media/upload-media/api-reference/post-media-subtitles-delete

# Response Codes

This endpoint returns the following HTTP responses:

|     |     |     |
| --- | --- | --- |
| Status | Text | Description |
| 200 | OK  | The request to create the subtitle was successful. |
| 400 | Bad Request | Generally, this response occurs due to the presence of invalid JSON in the request, or where the request failed to send any JSON payload. In this case this error could indicate an invalid subtitle file. |
| 403 | Unauthorized | HTTP authentication failed due to invalid credentials. Check your OAuth keys and tokens. |
| 404 | Not Found | The resource was not found at the URL to which the request was sent, likely because an incorrect media\_id |
| 500 | Internal Server Error | There was an error on Twitter's side. Retry your request using an exponential backoff pattern. |
| 503 | Service Unavailable | There was an error on Twitter's side. Retry your request using an exponential backoff pattern. |

# Resource URL

`https://upload.twitter.com/1.1/media/subtitles/delete.json`