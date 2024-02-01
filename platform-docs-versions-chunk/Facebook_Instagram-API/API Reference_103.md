platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/business_discovery

# IG User Business Discovery

Allows you to get data about other Instagram Business or Creator [IG Users](https://developers.facebook.com/docs/instagram-api/reference/ig-user).

## Creating

This operation is not supported.

## Reading

**`GET /{ig-user-id}?fields=business_discovery.username({username})`**

Returns data about another Instagram Business or Creator [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user). Perform this request on the Instagram Business or Creator [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) who is making the query, and identify the targeted business with the `username` parameter.

### Limitations

Data about age-gated Instagram Business [IG Users](https://developers.facebook.com/docs/instagram-api/reference/ig-user) will not be returned.