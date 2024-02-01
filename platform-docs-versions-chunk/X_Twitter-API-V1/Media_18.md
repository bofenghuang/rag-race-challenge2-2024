platform: X
topic: Twitter-API-V1
subtopic: Media
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Media.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/media/upload-media/api-reference/post-media-upload-append

POST media/upload (APPEND)

post-media-upload-append

# POST media/upload (APPEND)

## Overview[¶](#overview "Permalink to this headline")

The `APPEND` command is used to upload a chunk (consecutive byte range) of the media file. For example, a 3 MB file could be split into 3 chunks of size 1 MB, and uploaded using 3 `APPEND` command requests. After the entire file is uploaded, the next step is to call the [FINALIZE command](https://developer.twitter.com/en/docs/media/upload-media/api-reference/post-media-upload-finalize).

There are a number of advantages of uploading a media file in small chunks:

* Improved reliability and success rates under low bandwidth network conditions
* Uploads can be paused and resumed
* File chunks can be retried individually
* Ability to tune chunk sizes to match changing network conditions e.g on cellular clients