platform: X
topic: Twitter-API-V1
subtopic: Media
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Media.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/media/upload-media/uploading-media/media-best-practices


## Video specifications and recommendations

Please use the [Async Path](https://developer.twitter.com/en/docs/media/upload-media/uploading-media/chunked-media-upload) for media uploads.

**Recommended:**

* Recommended Video Codec: H264 High Profile
* Recommended Frame Rates: 30 FPS, 60 FPS
* Recommended Video Resolution: 1280x720 (landscape), 720x1280 (portrait), 720x720 (square)
* Recommended Minimum Video Bitrate: 5,000 kbps
* Recommended Minimum Audio Bitrate: 128 kbps
* Recommended Audio Codec: AAC LC
* Recommended Aspect Ratio: 16:9 (landscape or portrait), 1:1 (square)

**Advanced:**

* Frame rate must be 60 FPS or less
* Dimensions must be between 32x32 and 1280x1024
* File size must not exceed 512 mb
* Duration must be between 0.5 seconds and 140 seconds
* Aspect ratio must be between 1:3 and 3:1
* Must have 1:1 [pixel aspect ratio](https://en.wikipedia.org/wiki/Pixel_aspect_ratio)
* Only [YUV](https://en.wikipedia.org/wiki/YUV) 4:2:0 pixel format is supported
* Audio must be [AAC with Low Complexity profile](https://en.wikipedia.org/wiki/Advanced_Audio_Coding#Modular_encoding). High-Efficiency AAC is not supported
* Audio must be mono or stereo, not 5.1 or greater
* Must not have [open GOP](https://en.wikipedia.org/wiki/Group_of_pictures)
* Must use [progressive scan](https://en.wikipedia.org/wiki/Progressive_scan) 

**Additional Information:**

In the table below each row represents an upload recommendation, but is not a requirement. All uploads are processed for optimization across multiple platforms.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Orientation** | **Width** | **Height** | **Video Bitrate** | **Audio Bitrate** |
| Landscape | 1280 | 720 | 2048K | 128K |
| Landscape | 640 | 360 | 768K | 64K |
| Landscape | 320 | 180 | 256K | 64K |
| Portrait | 720 | 1280 | 2048K | 128K |
| Portrait | 360 | 640 | 768K | 64K |
| Portrait | 180 | 320 | 256K | 64K |
| Square | 720 | 720 | 2048K | 128K |
| Square | 480 | 480 | 768K | 64K |
| Square | 240 | 240 | 256K | 32K |

  
For an example of how to upload media, please see the [chunked media upload documentation](https://developer.twitter.com/content/developer-twitter/en/docs/media/upload-media/uploading-media/chunked-media-upload).