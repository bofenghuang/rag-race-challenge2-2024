platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/insights

### Range

This edge supports [time-based pagination](https://developers.facebook.com/docs/graph-api/results#time), so you can include the `since` and `until` parameters with Unix timestamps to define a _range_. For example, to get 28 days worth of impressions — _every day for the last 10 days_ — you could generate Unix timestamps for _10 days ago_ and _today_, assign them to the `since` and `until` parameters, and include them in your request:

metric=impressions&period=days\_28&since=1501545600&until=1502493720

The `since` and `until` parameters are inclusive, so if your range includes a day that hasn't ended (i.e, today), subsequent queries throughout the day may return increased values. If you do not include the `since` and `until` parameters, the API will default to a 2 day range: yesterday through today.

### Sample Request

curl -X GET \\
  'https://graph.facebook.com/`v19.0`/17841405822304914/insights?metric=impressions,reach,profile\_views&period=day&access\_token=IGQVJ...'