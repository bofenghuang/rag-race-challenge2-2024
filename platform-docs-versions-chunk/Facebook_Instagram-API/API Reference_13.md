platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-comment


### Deleting a Comment

`DELETE /{ig-comment-id}`

#### Permissions

A User [access token](https://developers.facebook.com/docs/instagram-api/overview#authentication) from a User who created the comment, with the following permissions:

* `instagram_basic`
* `instagram_manage_comments`

If the token is from a User whose **Page role was granted via the Business Manager**, one of the following permissions is also required:

* `ads_management`
* `pages_read_engagement`
* `business_management`

#### Limitations

* A comment can only be deleted by the owner of the object upon which the comment was made, even if the user attempting to delete the comment is the comment's author.
* Comments on live video IG Media are not supported.

#### Sample Request

DELETE graph.facebook.com
  /17873440459141021

#### Sample Response

{
  "success": true
}

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)