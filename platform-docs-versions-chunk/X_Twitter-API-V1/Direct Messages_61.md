platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/message-attachments/guides/attaching-media


### 1\. Chunk upload media

* Chunk upload the media file starting with [POST media/upload (INIT)](https://developer.twitter.com/en/docs/media/upload-media/api-reference/post-media-upload-init.html).
* Set the media\_category to dm\_image, dm\_gif or dm\_video appropriately.
* If reusing the media asset across multiple Direct Messages, you must set shared to true during the initial upload.
* If attaching a media asset to a Welcome Message, you must set shared to true during the initial upload.
* Uploaded media can only be shared across Direct Messages created by the same user.
* See [Uploading Media](https://developer.twitter.com/en/docs/media/upload-media/uploading-media/chunked-media-upload.html) for subsequent [APPEND](https://developer.twitter.com/en/docs/media/upload-media/api-reference/post-media-upload-append.html) and [FINALIZE](https://developer.twitter.com/en/docs/media/upload-media/api-reference/post-media-upload-finalize.html) steps.
* The returned media ID will be used when sending the Direct Message. If you did not set shared to true the media ID can only be used in a single Direct Message.

Once a media ID is generated, it must be attached to a Direct Message within 24 hours.

#### Parameters

|     |     |
| --- | --- |
| **media\_category  <br>**(required) | The media category: dm\_image, dm\_gif, dm\_video |
| **shared** | Set to true if media asset will be reused for multiple Direct Messages. Default is false. |

See [POST media/upload (INIT)](https://developer.twitter.com/en/docs/media/upload-media/api-reference/post-media-upload-init.html) documentation for all parameters and full details.