platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/content-publishing

### Rate Limit

Instagram accounts are limited to 50 API-published posts within a 24-hour moving period. Carousels count as a single post. This limit is enforced on the [`POST /{ig-user-id}/media_publish`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/media_publish) endpoint when attempting to publish a media container. We recommend that your app also enforce the publishing rate limit, especially if your app allows app users to schedule posts to be published in the future.

To check an Instagram Professional account's current rate limit usage, query the [`GET /{ig-user-id}/content_publishing_limit`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/content_publishing_limit) endpoint.