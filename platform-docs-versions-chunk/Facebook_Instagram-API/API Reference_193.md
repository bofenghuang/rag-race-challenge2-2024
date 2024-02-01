platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/recently_searched_hashtags


## Reading

`GET /{ig-user-id}/recently_searched_hashtags`

Get the hashtags that an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) has queried using the [IG Hashtags](https://developers.facebook.com/docs/instagram-api/reference/ig-hashtag) endpoint within the last 7 days.

IG Users can query a maximum of 30 unique hashtags within a rolling, 7 day period. A queried hashtag will count against that user's limit as soon as it is queried. Subsequent queries on that hashtag within 7 days of the initial query will not count against the user's limit.

**Limitations**

* Emojis in hashtag queries are not supported.
* The API returns 25 results per page by default, but you can use the `limit` parameter to get up to 30 per page (`limit=30`).

#### Requirements

| Type | Description |
| --- | --- |
| [Features](https://developers.facebook.com/docs/apps/review/feature) | [`Instagram Public Content Access`](https://developers.facebook.com/docs/apps/review/feature#reference-INSTAGRAM_PUBLIC_CONTENT_ACCESS) |
| [Permissions](https://developers.facebook.com/docs/apps/review/login-permissions) | [`instagram_basic`](https://developers.facebook.com/docs/facebook-login/permissions#reference-instagram_basic)<br><br>  <br><br>If the token is from a User whose Page role was granted via the Business Manager, one of the following permissions is also required: `ads_management`, `business_management`, or `pages_read_engagement`. |
| [Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens) | A Facebook User [access token](https://developers.facebook.com/docs/instagram-api/overview#authentication). |

#### Sample Request

GET graph.facebook.com/17841405309211844/recently\_searched\_hashtags?limit=30

#### Sample Response

{
  "data": \[
    {
      "id": "17841562906103814"
    },
    {
      "id": "17841563587120501"
    }
  \]
}