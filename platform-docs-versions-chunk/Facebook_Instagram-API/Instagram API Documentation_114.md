platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/changelog


## November 9, 2021

#### Live Videos

_Applies to all versions._

You can now use the Instagram API to get live video IG Media being broadcast by your app users, get comments on those videos, and use the Instagram Messaging API to send private replies (direct messages) to the comment authors. To support this functionality, the following changes have been made:

* a new [GET /ig-user/live\_media](https://developers.facebook.com/docs/instagram-api/reference/ig-user/live_media#reading) edge can return live video [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media/) being broadcast by your app user at the time of the request
* the `media` field on an [IG Comment](https://developers.facebook.com/docs/instagram-api/reference/ig-comment/) now returns and object containing both the ID (`id`) and published location (`media_product_type`) of the media upon which the comment was made
* a new [`live_comments`](https://developers.facebook.com/docs/graph-api/webhooks/reference/instagram/#live_comments) Instagram Webhooks field can send notifications containing live comments made on your app users' live videos as they are being broadcast

Please refer to the [Instagram Messaging API](https://developers.facebook.com/docs/messenger-platform/instagram) private replies documentation to learn how to send [private replies](https://developers.facebook.com/docs/messenger-platform/instagram/features/private-replies) to users who have commented on your app users' live video IG Media.

[](#)