platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/webhooks

### Get the Comment's Contents

To get the comment's contents, use the `comment_id` property to query the [`GET /{ig-user-id}/mentioned_comment`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/mentioned_comment) edge:

#### Sample Query

GET https://graph.facebook.com/17841405726653026
  ?fields=mentioned\_comment.comment\_id(17894227972186120)

#### Sample Response

{
  "mentioned\_comment": {
    "timestamp": "2018-03-20T00:05:29+0000",
    "text": "@bluebottle challenge?",
    "id": "17894227972186120"
  },
  "id": "17841405726653026"
}