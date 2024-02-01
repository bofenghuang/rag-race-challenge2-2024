platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-comment

# IG Comment

Represents a comment on an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media).

## Creating

This operation is not supported.

## Reading

**`GET /{ig-comment-id}?fields={fields}`**

Get [fields](#fields) and [edges](#edges) on an IG Comment.

### Limitations

* Requests cannot be performed on comments discovered through the [Mentions API](https://developers.facebook.com/docs/instagram-api/guides/mentions) unless the request is made by the comment owner. Instead, use the [Mentioned Comment](https://developers.facebook.com/docs/instagram-api/reference/ig-user/mentioned_comment) node.
* Comments on age-gated media are not returned.
* Comments created by IG Users who have been restricted by the app user will not be returned unless the IG Users are unrestricted and the Comments are approved.
* Comments on live video IG Media can only be read while the IG Media upon which the comment was created is being broadcast.