platform: X
topic: Twitter-API-V1
subtopic: Media
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Media.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/media/upload-media/api-reference/post-media-upload-init

## Example Request[¶](#example-request "Permalink to this headline")

`POST https://upload.twitter.com/1.1/media/upload.json?command=INIT&total_bytes=10240&media_type=image/jpeg`

## Example Result[¶](#example-result "Permalink to this headline")

    {
      "media_id": 710511363345354753,
      "media_id_string": "710511363345354753",
      "size": 11065,
      "expires_after_secs": 86400,
      "image": {
        "image_type": "image/jpeg",
        "w": 800,
        "h": 320
      }
    }