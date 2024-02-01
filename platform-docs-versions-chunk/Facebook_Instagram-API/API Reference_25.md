platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-hashtag-search


### Getting a Hashtag ID

`GET /ig_hashtag_search?user_id={user-id}&q={q}`

Returns the ID of an [IG Hashtag](https://developers.facebook.com/docs/instagram-api/reference/ig-hashtag). IDs are both static and global (i.e, the ID for `#bluebottle` will always be `17843857450040591` for all apps and all app users).

#### Query String Parameters

* `{user_id}` (required) — The ID of the [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) performing the request.
* `{q}` (required) — The hashtag name to query.

#### Limitations

* You can query a maximum of 30 unique hashtags [within a 7 day period](https://developers.facebook.com/docs/instagram-api/reference/ig-user/recently_searched_hashtags).
* The API will return a generic error for any queries that include hashtags that we have deemed sensitive or offensive.

**Requirements**

| Type | Description |
| --- | --- |
| [Features](https://developers.facebook.com/docs/apps/review/feature) | [`Instagram Public Content Access`](https://developers.facebook.com/docs/apps/review/feature#reference-INSTAGRAM_PUBLIC_CONTENT_ACCESS) |
| [Permissions](https://developers.facebook.com/docs/apps/review/login-permissions) | [`instagram_basic`](https://developers.facebook.com/docs/facebook-login/permissions#reference-instagram_basic)<br><br>  <br><br>If the token is from a User whose Page role was granted via the Business Manager, one of the following permissions is also required: `ads_management`, `business_management`, or `pages_read_engagement`. |
| [Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) | A User access token of a Facebook User who has been [approved for tasks on the connected Facebook Page](https://developers.facebook.com/docs/instagram-api/overview#access-tokens). |

#### Sample Request

curl -X GET \\
 "https://graph.facebook.com/`v19.0`/ig\_hashtag\_search?user\_id=17841405309211844&q=bluebottle&access\_token={access-token}"

#### Sample Response

{
    "data": \[
        {
            "id": "17843857450040591"
        }
    \]
}