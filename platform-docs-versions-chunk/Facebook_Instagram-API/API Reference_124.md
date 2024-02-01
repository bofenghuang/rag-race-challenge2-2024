platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/insights

### Limitations

* `follower_count`, `online_followers`, and all `audience_*` metrics are not available on IG Users with fewer than 100 followers.
* Insights data for the `online_followers` metric is only available for the last 30 days.
* If insights data you are requesting does not exist or is currently unavailable, the API will return an empty data set instead of `0` for individual metrics.
* Demographic metrics only return the top 45 performers (e.g., for `audience_city`, up to 45 cities with the highest number of followers can be returned).
* Only viewers for whom we have demographic data are used in demographic metric calculations.
* Summing demographic metric values may result in a value less than the follower count (see previous bullet point).
* `audience_*` [metrics](#metrics-and-periods) do not support `since` and `until` [range](#range) parameters.
* Data used to calculate metrics may be delayed up to 48 hours.