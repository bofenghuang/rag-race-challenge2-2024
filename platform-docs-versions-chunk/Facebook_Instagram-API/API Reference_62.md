platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-media/insights


### Limitations

* Insights data is not available for any media within an album [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media).
* Story media metrics are only available for 24 hours, even if the stories are archived or highlighted. To get the latest insights for a story before it expires, set up a [Webhook](https://developers.facebook.com/docs/instagram-api/guides/webhooks) for the `Instagram` topic and subscribe to the `story_insights` field.
* Story media metrics with values less than 5 return an error code `10` with the message `(#10) Not enough viewers for the media to show insights`.
* For Stories created by users in Europe and Japan, the `replies` metric now returns a value of `0`.
* For Stories, replies made by users in Europe and Japan are not included in `replies` calculations.
* If insights data you are requesting does not exist or is currently unavailable, the API returns an empty data set instead of `0` for individual metrics.
* Data used to calculate metrics can be delayed up to 48 hours.