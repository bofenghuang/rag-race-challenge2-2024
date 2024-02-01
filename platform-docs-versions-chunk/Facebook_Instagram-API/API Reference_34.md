platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-hashtag/recent-media


### Getting Hashtagged Media

`GET /{ig-hashtag-id}/recent_media?user_id={user-id}&fields={fields}`

Returns a list of the most recently published photo and video [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects published with a specific hashtag.

#### Query String Parameters

* `{user_id}` (required) — The ID of the [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) performing the query.
* `{fields}` — A comma-separated list of fields you want returned. See [Returnable Fields](#returnable-fields).

#### Limitations

* Only returns public photos and videos.
* Only returns media objects published within 24 hours of query execution.
* Will not return promoted/boosted/ads media.
* Responses are paginated with a maximum `limit` of 50 results per page.
* Responses will not always be in chronological order.
* You can query a maximum of 30 unique hashtags [within a 7 day period](https://developers.facebook.com/docs/instagram-api/reference/ig-user/recently_searched_hashtags).
* You cannot request the `username` field on returned media objects.
* This endpoint only returns an `after` cursor for paginated results; a `before` cursor will not be included. In addition, the `after` cursor value will always be the same for each page, but it can still be used to get the next page of results in the result set.

**Requirements**

| Type | Description |
| --- | --- |
| [Features](https://developers.facebook.com/docs/apps/review/feature) | [`Instagram Public Content Access`](https://developers.facebook.com/docs/apps/review/feature#reference-INSTAGRAM_PUBLIC_CONTENT_ACCESS) |
| [Permissions](https://developers.facebook.com/docs/apps/review/login-permissions) | [`instagram_basic`](https://developers.facebook.com/docs/facebook-login/permissions#reference-instagram_basic)<br><br>  <br><br>If the token is from a User whose Page role was granted via the Business Manager, one of the following permissions is also required: `ads_management`, `business_management`, or `read_pages_engagement`. |
| [Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens) | A User access token of a Facebook User who has been [approved for tasks on the connected Facebook Page](https://developers.facebook.com/docs/instagram-api/overview#authentication). |

#### Response

An array of [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) objects. Excess results will be paginated.

#### Returnable Fields

You can use the `fields` parameter to request the following fields on returned media objects:

* `caption`
* `children` (only returned for Album [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media))
* `comments_count`
* `id`
* `like_count` (v10.0 and older calls: value will be `0` if the media owner has [hidden](https://www.facebook.com/help/instagram/113355287252104) like counts it. v11.0+ calls: field will be omitted if media owner has hidden like counts in it)
* `media_type`
* `media_url` (not returned for Album [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media))
* `permalink`
* `timestamp` (only available on v7.0+)

#### Sample Request

GET graph.facebook.com/17873440459141021/recent\_media
  ?user\_id=17841405309211844
  &fields=id,media\_type,comments\_count,like\_count

#### Sample Response

{
  "data": \[
    {
      "id": "17880997618081620",
      "media\_type": "IMAGE",
      "comments\_count": 84,
      "like\_count": 177
    },
    {
      "id": "17871527143187462"
      "media\_type": "IMAGE",
      "comments\_count": 24,
      "like\_count": 57
    },
    {       
      "id": "17896450804038745"
      "media\_type": "IMAGE",
      "comments\_count": 19,
      "like\_count": 36
    }
  \],
  "paging":
    {
      "cursors":
        {
          "after": "NTAyYmE4..."
        },
      "next": "https://graph.facebook.com/..."
    }
}