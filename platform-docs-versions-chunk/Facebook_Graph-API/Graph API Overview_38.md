platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/overview/rate-limiting


## Business Use Case Rate Limits

All Marketing API requests, and Pages API requests made with a system or page access token, are subject to Business Use Case (BUC) Rate Limits, and depend on the endpoints you are querying.

For Marketing API, the rate limit is applied to the ad account across the same Business Use Case. For example, all endpoints with the Ads Management business use case will share the total quota within the same ad account. If a certain endpoint makes a lot of API requests and causes throttling, other endpoints configured with the same business use case will also receive rate limiting errors. The quota depends on the app's Marketing API Access Tier. The standard access Marketing API tier will have more quotas than the development access Marketing API tier. By default, an new app should be on the development tier. If you need to upgrade to get more rate limiting quota, upgrade to Advanced Access of [Ads Management Standard Access](https://developers.facebook.com/docs/features-reference/ads-management-standard-access/) in App Review.

|     |     |
| --- | --- |
| * [Ad Insights](#ads-insights)<br>* [Ads Management](#ads-management)<br>* [Catalog](#catalog)<br>* [Custom Audience](#custom-audience)<br>* [Instagram Graph API](#instagram-graph-api)<br>* [Lead Generation](#leadgen) | * [Messenger](#messenger)<br>* [Pages](#pages)<br>* [Spark AR Commerce Effect Management](#spark-ar)<br>* [WhatsApp Business Management API](#wa-biz-api) |