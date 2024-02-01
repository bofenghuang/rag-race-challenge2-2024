platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-media/comments


### Getting Comments on a Media Object

`GET /{ig-media-id}/comments`

Returns a list of [IG Comments](https://developers.facebook.com/docs/instagram-api/reference/ig-comment) on an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object.

#### Limitations

* Requests made using API version 3.1 or older will have results returned in chronological order. Requests made using version 3.2+ will have results returned in reverse chronological order.
* Returns only top-level comments. Replies to comments are not included unless you use field expansion to request the `replies` field.
* Returns a maximum of 50 comments per query.

#### Permissions

An [access token](https://developers.facebook.com/docs/instagram-api/overview#authentication) from a User who created the [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object, with the following permissions:

* `instagram_basic`
* `pages_show_list`
* `pages_read_engagement`

If the token is from a User whose **Page role was granted via the Business Manager**, one of the following permissions is also required:

* `ads_management`
* `pages_read_engagement`
* `business_management`

#### Sample Request

GET graph.facebook.com
  /17895695668004550/comments

#### Sample Response

{
  "data": \[
    {
      "timestamp": "2017-08-31T19:16:02+0000",
      "text": "This is awesome!",
      "id": "17870913679156914"
    },
    {
      "timestamp": "2017-08-31T18:10:30+0000",
      "text": "\*Sniff\*",
      "id": "17873440459141021"
    }
  \]
}