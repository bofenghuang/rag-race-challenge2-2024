platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/mentions


### Replying to a Captioned IG Media Object

`POST /{ig-user-id}/mentions?media_id={media_id}&message={message}`

Creates an [IG Comment](https://developers.facebook.com/docs/instagram-api/reference/ig-comment) on an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object in which an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) has been @mentioned in a caption.

#### Limitations

* Mentions on Stories are not supported.
* Commenting on photos in which you were tagged is not supported.
* Webhooks will not be sent if the Media upon which the comment or @mention appears was created by an account that is set to private.

#### Query String Parameters

Query string parameters are optional unless indicated as required.

* `{media_id}` (required) — the media ID contained in the [Webhook notification](https://developers.facebook.com/docs/instagram-api/guides/webhooks#reply-caption-mention) payload
* `{message}` (required) — text to include in the commment

#### Permissions

A Facebook User [access token](https://developers.facebook.com/docs/instagram-api/overview#authentication) with the following permissions:

* `instagram_basic`
* `instagram_manage_comments`
* `pages_read_engagement`
* `pages_show_list`

If the token is from a User whose **Page role was granted via the Business Manager**, one of the following permissions is also required:

* `ads_management`
* `pages_read_engagement`
* `business_management`

#### Sample cURL Request

curl -i -X POST \\
 -d "media\_id=17920112008063024" \\
 -d "message=Thanks%20for%20the%20dinosaur!" \\
 -d "access\_token=a-valid-access-token-goes-here" \\
 "https://graph.facebook.com/17841405309211844/mentions"

#### Sample Response

{
  "id": "17846319838228163"
}