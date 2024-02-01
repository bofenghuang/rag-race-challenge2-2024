platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-media/children


### Getting Child Media Objects

`GET /{ig-media-id}/children`

Returns a list of [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects on an album [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object.

#### Permissions

An [access token](https://developers.facebook.com/docs/instagram-api/overview#authentication) from a User who created the album [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object, with the following permissions:

* `instagram_basic`
* `pages_read_engagement` or `pages_show_list`

If the token is from a User whose **Page role was granted via the Business Manager**, one of the following permissions is also required:

* `ads_management`
* `pages_read_engagement`
* `business_management`

#### Limitations

* Some fields, such as `permalink`, cannot be used on photos within albums (children).

#### Sample Request

GET graph.facebook.com
  /17896450804038745/children

#### Sample Response

{
  "data": \[
    {
      "id": "17880997618081620"
    },
    {
      "id": "17871527143187462"
    }
  \]
}