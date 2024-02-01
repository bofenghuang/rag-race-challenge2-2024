platform: X
topic: Twitter-API-V1
subtopic: Media
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Media.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/media/upload-media/api-reference/post-media-subtitles-create

POST media/subtitles/create

post-media-subtitles-create

# POST media/subtitles/create

# Overview

Use this endpoint to associate uploaded subtitles to an uploaded video. You can associate subtitles to video before or after Tweeting.

Request flow for associating subtitle to video before the video is Tweeted : 1. Upload video using the chunked upload endpoint and get the video media\_id. 2. Upload subtitle using the chunked upload endpoint with media category set to “Subtitles” and get the subtitle media\_id. 3. Call this endpoint to associate the subtitle to the video. 4. Create Tweet with the video media\_id.

Request flow for associating subtitle to video after the video is Tweeted : 1. Upload video using the chunked upload endpoint and get the video media\_id. 2. Create Tweet with the video media\_id. 3. Upload subtitle using the chunked upload endpoint with media category set to SUBTITLES and get the subtitle media\_id. 4. Call this endpoint to associate the subtitle to the video.