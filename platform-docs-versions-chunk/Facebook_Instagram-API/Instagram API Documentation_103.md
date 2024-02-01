platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/webhooks

### Get the Caption's Contents

To get the caption's contents, use the `media_id` property to query the [`GET /{ig-user-id}/mentioned_media`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/mentioned_media) edge:

#### Sample Query

GET https://graph.facebook.com/17841405726653026
  ?fields=mentioned\_media.media\_id(17918195224117851){caption,media\_type}

#### Sample Response

{
  "mentioned\_media": {
    "caption": "@bluebottle There can be only one!",
    "media\_type": "IMAGE",
    "id": "17918195224117851"
  },
  "id": "17841405726653026"
}