platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/changelog


## October 5, 2021

The following changes apply to Instagram TV videos created on or after October 5, 2021. Instagram TV videos created before this date are exempt from these changes.

* the `media_product_type` [field](https://developers.facebook.com/docs/instagram-api/reference/ig-media/#fields) will return `FEED` instead of `IGTV`
* the `video_title` [field](https://developers.facebook.com/docs/instagram-api/reference/ig-media/#fields) will not be returned
* [Instagram Webhooks](https://developers.facebook.com/docs/instagram-api/guides/webhooks) `comments` and `mentions` fields are now supported

On January 3, 2022, the changes above will apply to all API versions and all Instagram TV videos, regardless of video creation date. This means that starting January 3, 2022, apps using older API versions will be able to query Instagram TV videos (read support was introduced in v10.0 and limited to v10.0+).

Starting with v14.0, the `video_title` field will no longer be supported and the API will throw an error if the field is requested.

[](#)