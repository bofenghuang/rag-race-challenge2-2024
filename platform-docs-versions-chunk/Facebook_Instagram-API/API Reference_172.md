platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/mentioned_comment

# IG User Mentioned Comment

Returns data on an [IG Comment](https://developers.facebook.com/docs/instagram-api/reference/ig-comment) in which an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) has been @mentioned by another Instagram user.

## Creating

This operation is not supported.

## Reading

**`GET /{ig-user-id}?fields=mentioned_comment.comment_id`**

Returns data on an [IG Comment](https://developers.facebook.com/docs/instagram-api/reference/ig-comment) in which an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) has been @mentioned by another Instagram user.

### Limitations

This endpoint will return an error if comments have been disabled on the [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) on which the [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) has been @mentioned.