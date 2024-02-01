platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/overview/rate-limiting


### Instagram Graph API

Calls to the [Instagram Graph API](https://developers.facebook.com/docs/instagram-api) are counted against the calling app's call count. An app's call count is unique for each app and app user pair, and is the number of calls the app has made in a rolling 24 hour window. It is calculated as follows:

`Calls within 24 hours = 4800 * Number of Impressions`

The Number of Impressions is the number of times any content from the app user's Instagram account has entered a person's screen within the last 24 hours.

#### Notes

* The [Instagram Basic Display API](https://developers.facebook.com/docs/instagram-basic-display-api) uses [Platform Rate Limits](https://developers.facebook.com/docs/graph-api/overview/rate-limiting#platform-rate-limits).
* [Business Discovery](https://developers.facebook.com/docs/instagram-api/guides/business-discovery) and [Hashtag Search](https://developers.facebook.com/docs/instagram-api/guides/hashtag-search) are subject to [Platform Rate Limits](https://developers.facebook.com/docs/graph-api/overview/rate-limiting#platform-rate-limits).