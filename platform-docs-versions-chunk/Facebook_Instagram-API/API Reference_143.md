platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/live_media

# IG User Live Media

Represents a collection of live video [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) on an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user).

## Creating

This operation is not supported.

## Reading

**`GET /{ig-user-id}/live_media`**

Get a collection of live video [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) on an [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user).

### Limitations

Only live video IG Media being broadcast at the time of the request will be returned.

### Time-based Pagination

This endpoint supports [time-based pagination](https://developers.facebook.com/docs/graph-api/using-graph-api#time). Include `since` and `until` query-string paramaters with Unix timestamp or `strtotime` data values to define a time range.