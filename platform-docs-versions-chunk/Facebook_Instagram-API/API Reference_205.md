platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/page

### Getting a Page's IG User

`GET /{page-id}?fields=instagram_business_account`

Returns the [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) connected to the Facebook Page.

#### Permissions

A Facebook User [access token](https://developers.facebook.com/docs/instagram-api/overview#authentication) with the following permissions:

* `instagram_basic`
* `pages_show_list`

If the token is from a User whose **Page role was granted via the Business Manager**, one of the following permissions is also required:

* `ads_management`
* `pages_read_engagement`
* `business_management`

#### Sample Request

GET graph.facebook.com
  /134895793791914?fields=instagram\_business\_account

#### Sample Response

{
  "instagram\_business\_account": {
    "id": "17841405822304914"
  },
  "id": "134895793791914"
}

## Updating

This operation is not supported.