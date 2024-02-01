platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/overview

## Rate Limiting

All endpoints are subject to [Instagram Business Use Case rate limiting](https://developers.facebook.com/docs/graph-api/overview/rate-limiting#instagram-graph-api) except for [Business Discovery](https://developers.facebook.com/docs/instagram-api/guides/business-discovery) and [Hashtag Search](https://developers.facebook.com/docs/instagram-api/guides/hashtag-search) endpoints, which are subject to [Platform Rate limiting](https://developers.facebook.com/docs/graph-api/overview/rate-limiting#platform-rate-limits).

[](#)

## Webhooks

You can use Webhooks to have notifications sent to you whenever someone comments on your app users' media objects or when any of their stories expire. Refer to our [Webhooks documentation](https://developers.facebook.com/docs/graph-api/webhooks) to learn how to use Webhooks, then set up a webhook for the `Instagram` topic and subscribe to its `comments` and `story_insights` fields.

[](#)