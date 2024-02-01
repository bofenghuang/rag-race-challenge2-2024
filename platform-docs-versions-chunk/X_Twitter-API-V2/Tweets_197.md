platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/counts/migrate


### Recent Tweet counts comparison

The enterprise version of the Tweet counts endpoints allow you to pull counts for either 30 days or from the full-archive. Therefore, the v2 recent Tweet counts endpoint, which looks at a 7 day time period, is not a direct replacement for either of the aforementioned endpoints.

However, to help with comparisons, we will look at how the v2 recent Tweet counts endpoint compares to the enterprise 30-day endpoint.

The following table compares the various types of recent Tweet counts endpoints:

| **Description** | **Enterprise** | **Twitter API v2** |
| --- | --- | --- |
| Host domain | https://gnip-api.twitter.com | https://api.twitter.com |
| Endpoint path | /search/30day/accounts/:account\_name/:label/counts.json | /2/tweets/counts/recent |
| [Authentication](https://developer.twitter.com/en/docs/authentication) | Basic authentication | OAuth 2.0 Bearer Token |
| Timestamp format | YYYYMMDDhhmm | YYYY-MM-DDTHH:mm:ssZ  <br>[ISO 8601 / RFC 3339](https://tools.ietf.org/html/rfc3339#section-5.6) |
| Returns counts of Tweets that are no older than | 31 days | 7 days |
| HTTP methods supported | GET | GET |
| Default request rate limits | 20 requests per 1 sec, aggregated across search data and counts requests  <br>The per minute rate limit will vary by partner as specified in your contract. | 180 requests per 15 min per user  <br>450 requests per 15 min per App |
| Supports filtering using [annotations](https://developer.twitter.com/en/docs/twitter-api/annotations) |     | ✔   |
| Supports filtering using [conversation\_id](https://developer.twitter.com/en/docs/twitter-api/conversation-id) |     | ✔   |
| JSON key name for Tweet data array | results | data |
| Time granularity | Day, hour, or minute | Day, hour, or minute |
| Timezone | UTC | UTC |
| Request parameters for selecting time period | fromDate  <br>toDate | start\_time  <br>end\_time |
| Request parameters for navigating by Tweet ID |     | since\_id  <br>until\_id |
| Requires the use of credentials from a [developer App](https://developer.twitter.com/en/docs/apps) associated with a [project](https://developer.twitter.com/en/docs/projects) |     | ✔   |