platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/mentioned_media

### Sample Request

curl -X GET \\
  'https://graph.facebook.com/`v19.0`/17841405309211844?fields=mentioned\_media.media\_id(17873440459141021){caption,media\_type}&access\_token=IGQVJ...'

### Sample Response

{
  "mentioned\_media": {
    "caption": "metricsaurus headquarters!",
    "media\_type": "IMAGE",
    "id": "17873440459141021"
  },
  "id": "17841405309211844"
}

Note that in the sample above, the API has stripped out the leading `@` symbol from the original caption (@metricsaurus headquarters!) because the app user did not create the caption.