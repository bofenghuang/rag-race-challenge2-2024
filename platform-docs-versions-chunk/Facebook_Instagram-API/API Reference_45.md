platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-media

### cURL Example

#### Request

curl -X GET \\
  'https://graph.facebook.com/`v19.0`/17895695668004550?fields=id,media\_type,media\_url,owner,timestamp&access\_token=IGQVJ...'

#### Response

{
  "id": "17918920912340654",
  "media\_type": "IMAGE",
  "media\_url": "https://sconten...",
  "owner": {
    "id": "17841405309211844"
  },
  "timestamp": "2019-09-26T22:36:43+0000"
}

## Updating

**`POST /{ig-media-id}`**

Enable or disable comments on an IG Media.

### Limitations

Live video IG Media not supported.