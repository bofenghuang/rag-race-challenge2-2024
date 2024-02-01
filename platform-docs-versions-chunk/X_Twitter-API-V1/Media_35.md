platform: X
topic: Twitter-API-V1
subtopic: Media
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Media.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/media/upload-media/api-reference/post-media-metadata-create

## Response[¶](#response "Permalink to this headline")

A successful response returns HTTP 2xx.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://upload.twitter.com/1.1/media/metadata/create.json`

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

## Example Request[¶](#example-request "Permalink to this headline")

`POST https://upload.twitter.com/1.1/media/metadata/create.json`

    {
      "media_id":"692797692624265216",
      // image alt text metadata
      "alt_text": {
        "text":"dancing cat" // Must be <= 1000 chars
      }
    }