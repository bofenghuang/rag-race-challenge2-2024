platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/insights


## Limitations

* Some metrics are [not available](https://developers.facebook.com/docs/instagram-api/reference/ig-user/insights#limitations) on IG Users with fewer than 100 followers.
* The API only reports organic interaction metrics; interactions on ads containing a media object are not counted.
* Metrics data is stored for 2 years.
* You can only get insights for a single user at a time.
* You cannot get insights for Facebook Pages.
* Stories insights are only available for 24 hours, even if the stories are archived or highlighted. If you want to get the latest insights for a story before it expires, set up a [Webhook](https://developers.facebook.com/docs/instagram-api/guides/webhooks) for the [`Instagram`](https://developers.facebook.com/docs/graph-api/webhooks/reference/instagram/) topic and subscribe to the [`story_insights`](https://developers.facebook.com/docs/graph-api/webhooks/reference/instagram/#story_insights) field.
* Insights on album child IG Media is not supported.
* If insights data you are requesting does not exist or is currently unavailable the API will return an empty data set instead of `0` for individual metrics.

[](#)