platform: X
topic: Twitter-API-V1
subtopic: Media
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Media.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/media/upload-media/api-reference/post-media-subtitles-delete

# Resource Information

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

# Example Request

    POST https://upload.twitter.com/1.1/media/subtitles/delete.json
    
      {
        "media_id":"692797692624265216",
        "media_category":"TweetVideo",
        "subtitle_info": {
          "subtitles": [
            "language_code":"EN", //The language code should be a BCP47 code (e.g. 'en", "sp")
          ]
        }
      }