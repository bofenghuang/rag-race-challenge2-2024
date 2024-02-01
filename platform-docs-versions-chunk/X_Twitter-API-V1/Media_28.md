platform: X
topic: Twitter-API-V1
subtopic: Media
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Media.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/media/upload-media/api-reference/post-media-upload-finalize

## Example Result[¶](#example-result "Permalink to this headline")

    // Example of sync FINALIZE response
    {
      "media_id": 710511363345354753,
      "media_id_string": "710511363345354753",
      "size": 11065,
      "expires_after_secs": 86400,
      "video": {
        "video_type": "video/mp4"
      }
    }
    
    // Example of async FINALIZE response which requires further STATUS command call(s)
    {
      "media_id": 710511363345354753,
      "media_id_string": "710511363345354753",
      "expires_after_secs": 86400,
      "size": 10240,
      "processing_info": {
        "state": "pending",
        "check_after_secs": 5 // check after 5 seconds for update using STATUS command
      }
    }