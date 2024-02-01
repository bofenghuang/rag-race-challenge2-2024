platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-media/comments


### Creating a Comment on a Media Object

`POST /{ig-media-id}/comments?message={message}`

Creates an [IG Comment](https://developers.facebook.com/docs/instagram-api/reference/ig-comment) on an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object.

#### Limitations

Comments on live video IG Media are not supported.

#### Query String Parameters

Query string parameters are optional unless indicated as required.

* `{message}` (required) — The text to be included in the comment.

#### Permissions

An [access token](https://developers.facebook.com/docs/instagram-api/overview#authentication) from a User who created the [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object, with the following permissions:

* `instagram_basic`
* `instagram_manage_comments`
* `pages_show_list`
* `pages_read_engagement`

If the token is from a User whose **Page role was granted via the Business Manager**, one of the following permissions is also required:

* `ads_management`
* `pages_read_engagement`
* `business_management`

#### Sample Request

POST graph.facebook.com
  /17895695668004550/comments?message=This%20is%20awesome!

#### Sample Response

{
  "id": "17870913679156914"
}