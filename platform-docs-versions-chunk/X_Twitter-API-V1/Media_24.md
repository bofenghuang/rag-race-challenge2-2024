platform: X
topic: Twitter-API-V1
subtopic: Media
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Media.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/media/upload-media/api-reference/get-media-upload-status


## Example Result[¶](#example-result "Permalink to this headline")

    // Example of an in_progress response:
    
    {
      "media_id":710511363345354753,
      "media_id_string":"710511363345354753",
      "expires_after_secs":3595,
      "processing_info":{
        "state":"in_progress", // state transition flow is pending -> in_progress -> [failed|succeeded]
        "check_after_secs":10, // check for the update after 10 seconds
        "progress_percent":8 // Optional [0-100] int value. Please don't use it as a replacement of "state" field.
      }
    }
    
    // Example of a failed response:
    
    {
      "media_id":710511363345354753,
      "media_id_string":"710511363345354753",
      "processing_info":{
        "state":"failed",
        "progress_percent":12,
        "error":{
          "code":1,
          "name":"InvalidMedia",
          "message":"Unsupported video format"
        }
      }
    }
    
    // Example of a succeeded response:
    
    {
      "media_id":710511363345354753,
      "media_id_string":"710511363345354753",
      "expires_after_secs":3593,
      "video":{
        "video_type":"video/mp4"
      },
      "processing_info":{
        "state":"succeeded",
        "progress_percent":100,
      }
    }