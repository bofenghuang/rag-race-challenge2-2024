platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/webhooks

### Parse the Payload and Respond

When you get the response, parse the payload for the `text` property to determine if you want to respond to the comment. To respond, use the webhook notification payload's `caption_id` and `media_id` property values to query the [`POST /{ig-user-id}/mentions`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/mentions) endpoint:

#### Sample Query

curl \-i \-X POST \\
  \-d "comment\_id=17894227972186120" \\
  \-d "media\_id=17918195224117851" \\
  \-d "message=Challenge%20accepted!" \\
  \-d "access\_token={access-token}" \\
  "https://graph.facebook.com/17841405726653026/mentions"

#### Sample Response

{
  "id": "17911496353086895"
}