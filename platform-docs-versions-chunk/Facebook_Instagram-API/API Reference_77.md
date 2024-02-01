platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-media/product_tags

# IG Media Product Tags

Represents product tags on an [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media). See [Product Tagging](https://developers.facebook.com/docs/instagram-api/guides/product-tagging) guide for complete usage details.

## Creating

**`POST /{ig-media-id}/product_tags`**

Create or update product tags on an existing [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media).

### Limitations

* Instagram Creator accounts are not supported.
* Stories, Instagram TV, Live, and Mentions are not supported.
* Tagging media is additive until the 5 tag limit has been reached. If the targeted media has already been tagged by a product in the request, the old tag's `x` and `y` values will be updated with their new values (a new tag will not be added).