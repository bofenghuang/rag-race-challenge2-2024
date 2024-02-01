platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-comment


### Hiding/Unhiding a Comment

`POST /{ig-comment-id}?hide={hide}`

#### Query String Parameters

* `{hide}` (required) — Set to `true` to hide the comment, or `false` to show the comment.

#### Limitations

* Comments made by media object owners on their own media objects will always be displayed, even if the comments have been set to `hide=true`.
* Comments on live video IG Media are not supported.

#### Permissions

A User [access token](https://developers.facebook.com/docs/instagram-api/overview#authentication) from a Facebook User who created the comment, with the following permissions:

* `instagram_basic`
* `instagram_manage_comments`
* `pages_show_list`
* `pages_read_engagement`

If the token is from a User whose **Page role was granted via the Business Manager**, one of the following permissions is also required:

* `ads_management`
* `pages_read_engagement`
* `business_management`

#### Sample Request

Hiding a comment:

POST graph.facebook.com
  /17873440459141021?hide=true

#### Sample Response

{
  "success": true
}