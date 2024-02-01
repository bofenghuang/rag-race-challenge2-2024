platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/mentioned_media

# Mentioned Media

Returns data on an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) in which an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) has been @mentioned in a caption by another Instagram user.

## Creating

This operation is not supported.

## Reading

**`GET /{ig-user-id}?fields=mentioned_media.media_id`**

Returns data on an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) in which an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) has been @mentioned in a caption by another Instagram user.

### Limitations

* Mentions on Stories are not supported.
* Commenting on photos in which you were tagged is not supported.
* Webhooks will not be sent if the Media upon which the comment or @mention appears was created by an account that is set to private.