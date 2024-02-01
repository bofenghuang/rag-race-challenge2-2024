platform: X
topic: Twitter-API-V1
subtopic: Media
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Media.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/media/upload-media/uploading-media/chunked-media-upload


## 

Using the [chunked POST media/upload](https://developer.twitter.com/en/docs/media/upload-media/api-reference/post-media-upload-init.html) endpoints requires an adjusted workflow from single image uploads. For video or chunked uploads, you must:

* Initialize the upload using the INIT command
* Upload each chunk of bytes using the APPEND command
* Complete the upload using the FINALIZE command

See the [large video upload sample](https://github.com/twitterdev/large-video-upload-python/) for an example written in Python.

Below is a working example using the command-line [twurl](https://github.com/twitter/twurl) utility. To see full headers of the requests and responses when using twurl, use the -t option to enable trace mode.

**INIT**

      `twurl -H upload.twitter.com "/1.1/media/upload.json" -d "command=INIT&media_type=video/mp4&total_bytes=4430752"`
    

      `{   "media_id": 601413451156586496,   "media_id_string": "601413451156586496",   "expires_after_secs": 3599 }`
    

**APPEND**  

      `twurl -H upload.twitter.com "/1.1/media/upload.json" -d "command=APPEND&media_id=601413451156586496&segment_index=0" --file /path/to/video.mp4 --file-field "media"`
    

HTTP 2XX will be returned with an empty response body on successful upload.  

**FINALIZE**

      `twurl -H upload.twitter.com "/1.1/media/upload.json" -d "command=FINALIZE&media_id=601413451156586496"`
    

      `{   "media_id": 601413451156586496,   "media_id_string": "601413451156586496",   "size": 4430752,   "expires_after_secs": 3600,   "video": {     "video_type": "video/mp4"   } }`
    

Troubleshooting