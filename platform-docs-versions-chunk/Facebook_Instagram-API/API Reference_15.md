platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-comment/replies


### Replying to a Comment

`POST /{ig-comment-id}/replies?message={message}`

Creates an [IG Comment](https://developers.facebook.com/docs/instagram-api/reference/ig-comment) on an [IG Comment](https://developers.facebook.com/docs/instagram-api/reference/ig-comment).

#### Query String Parameters

Query string parameters are optional unless indicated as required.

* `{message}` (required) — The text to be included in the comment.

#### Limitations

* You can only reply to top-level comments; replies to a reply will be added to the top-level comment.
* You cannot reply to hidden comments.
* You cannot reply to comments on a live video; use the [Instagram Messaging API](https://developers.facebook.com/docs/messenger-platform/instagram) to send a [private reply](https://developers.facebook.com/docs/messenger-platform/instagram/features/private-replies) instead.

#### Permissions

A User [access token](https://developers.facebook.com/docs/instagram-api/overview#authentication) from a User who created the comment, with the following permissions:

* `instagram_basic`
* `instagram_manage_comments`
* `pages_show_list`
* `page_read_engagement`

If the token is from a User whose **Page role was granted via the Business Manager**, one of the following permissions is also required:

* `ads_management`
* `pages_read_engagement`
* `business_management`

#### Sample Request

POST graph.facebook.com
  /17870913679156914/replies?message=\*sniff\*

#### Sample Response

{
  "id": "17873440459141021"
}