platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-comment/replies


### Getting All Replies (Comments) on a Comment

`GET /{ig-comment-id}/replies`

Returns a list of [IG Comments](https://developers.facebook.com/docs/instagram-api/reference/ig-comment) on an [IG Comment](https://developers.facebook.com/docs/instagram-api/reference/ig-comment).

#### Limitations

You cannot get replies to a comment that has been deleted.

#### Permissions

An [access token](https://developers.facebook.com/docs/facebook-login/access-tokens) from a User who created the comment, with the following permissions:

* `instagram_basic`
* `pages_show_list`
* `page_read_engagement`

If the token is from a User whose **Page role was granted via the Business Manager**, one of the following permissions is also required:

* `ads_management`
* `pages_read_engagement`
* `business_management`

#### Sample Request

GET graph.facebook.com
  /17873440459141021/replies

#### Sample Response

{
  "data": \[
    {
      "timestamp": "2017-08-31T16:53:49+0000",
      "text": "This is a great comment",
      "id": "17871618799146774"
    },
    {
      "timestamp": "2017-08-30T04:24:45+0000",
      "text": "It's me. Trust me.",
      "id": "17887288333072596"
    }
  \]
}