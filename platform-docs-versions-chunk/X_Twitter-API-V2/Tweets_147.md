platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/search/migrate


### Full-archive search comparison

The following table compares the various types of full-archive search endpoints:  

| **Description** | **Enterprise** | **Twitter API v2** |
| --- | --- | --- |
| Host domain | https://gnip-api.twitter.com | https://api.twitter.com |
| Endpoint path | /search/fullarchive/accounts/:account\_name/:label | /2/tweets/search/all |
| [Authentication](https://developer.twitter.com/en/docs/authentication) | Basic auth | OAuth 2.0 App-Only |
| Timestamp format | YYYYMMDDHHMM | YYYY-MM-DDTHH:mm:ssZ  <br>[ISO 8601 / RFC 3339](https://tools.ietf.org/html/rfc3339#section-5.6) |
| Returns Tweets that are no older than | The full archive since March 2006 | The full archive since March 2006 |
| HTTP methods supported | GET  <br>POST | GET |
| Default request rate limits | The per minute rate limit will vary by partner as specified in your contract. <br><br>20 requests per sec with Basic auth | 300 requests per 15 min with OAuth 2.0 App-Only<br><br>1 requests per 1 sec with OAuth 2.0 App-Only |
| Offers fully unwound URLs | ✔   | ✔   |
| Tweets per response | Maximum: 500  <br>Default: 100 | Maximum: 500  <br>Default: 10 |
| Tweet JSON format | [Native Enriched or Activity Streams](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/overview) format | [Twitter API v2](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction) format (determined by fields and expansions request parameters) |
| Supports selecting which [fields](https://developer.twitter.com/en/docs/twitter-api/fields) return in the payload |     | ✔   |
| Supports requesting and receiving [annotations](https://developer.twitter.com/en/docs/twitter-api/annotations) |     | ✔   |
| Supports requesting specific [metrics](https://developer.twitter.com/en/docs/twitter-api/metrics) within Tweet object |     | ✔   |
| Supports the [conversation\_id](https://developer.twitter.com/en/docs/twitter-api/conversation-id) operator and field |     | ✔   |
| Provides Tweet edit history | ✔   | ✔   |
| JSON key name for Tweet data array | results | data |
| JSON key name for pagination | **next** | meta.next\_token |
| Time resolution of time-based requests | second | second |
| Timezone | UTC | UTC |
| Supports navigating archive by Tweet ID |     | ✔   |
| Request parameters for navigation by time | fromDate  <br>toDate | start\_time  <br>end\_time |
| Request parameters for navigating by Tweet ID |     | since\_id   <br>until\_id |
| Request parameter for pagination | next\_token | next\_token |
| Requires the use of credentials from a [developer App](https://developer.twitter.com/en/docs/apps) associated with a [Project](https://developer.twitter.com/en/docs/projects) that has Academic Research access |     | ✔   |