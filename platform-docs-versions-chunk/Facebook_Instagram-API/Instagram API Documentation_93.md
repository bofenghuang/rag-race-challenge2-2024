platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/webhooks

### Limitations

* Webhook notifications for Comments on albums don't include the album ID. Get the album ID by querying the Comment ID in the webhook and request its `media` field.
* Apps don't receive a webhook notifications if the Media where the comment or @mention appears was created by a [private account](https://www.facebook.com/help/instagram/448523408565555).
* Story insights metrics with counts of less than 5 are returned as `-1`.
* Apps only receive webhook notifications for comments on live [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media/) if the media is on broadcast.
* Reels are not supported.
* Your app must have successfully completed App Review (advanced access) to receive webhooks notifications for `comments` and `live_comments` webhooks fields.

[](#)