platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/changelog


## October 20, 2021

#### IG Comments

_Applies to all versions._

Two new [fields](https://developers.facebook.com/docs/instagram-api/reference/ig-comment#fields) have been added to [IG Comments](https://developers.facebook.com/docs/instagram-api/reference/ig-comment):

* `from` — returns an object containing the [IGSID](https://developers.facebook.com/docs/messenger-platform/instagram/overview#igsid) (`id`) and username (`username`) of the comment creator.
* `parent_id` — returns the ID of the parent IG Comment if this comment was created on another IG Comment (i.e. a reply to another comment).

#### Instagram Webhooks

_Applies to all versions._

The `comments` Instagram webhooks [field](https://developers.facebook.com/docs/graph-api/webhooks/reference/instagram/#comments) now includes the following properties in the `value` field object:

* `from.id` — [IGSID](https://developers.facebook.com/docs/messenger-platform/instagram/overview#igsid) of the Instagram user who created the comment.
* `from.username` — Username of the Instagram user who created the comment
* `media.id` — ID of the IG Media upon which the comment was made.
* `media.media_product_type` — Surface (published location) of the IG Media upon which the comment was made.
* `parent_id` — ID of parent IG Comment if this comment was created on another IG Comment (i.e. a reply to another comment).

[](#)