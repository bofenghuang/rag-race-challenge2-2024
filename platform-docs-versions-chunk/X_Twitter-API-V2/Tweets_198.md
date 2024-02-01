platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/counts/migrate


###   
  
  
Full-archive Tweet counts comparison

The following table compares the various types of full-archive search endpoints:

| Description | Enterprise | Twitter API v2 |
| --- | --- | --- |
| Host domain | https://gnip-api.twitter.com | https://api.twitter.com |
| Endpoint path | /search/fullarchive/accounts/:account\_name/:label/counts | /2/tweets/counts/all |
| [Authentication](https://developer.twitter.com/en/docs/authentication) | Basic auth | OAuth 2.0 Bearer Token |
| Timestamp format | YYYYMMDDHHMM | YYYY-MM-DDTHH:mm:ssZ  <br>[ISO 8601 / RFC 3339](https://tools.ietf.org/html/rfc3339#section-5.6) |
| Returns Tweet counts that are no older than | The full archive since March 2006 | The full archive since March 2006 |
| HTTP methods supported | GET  <br>POST | GET |
| Default request rate limits | The per minute rate limit will vary by partner as specified in your contract.  <br>20 requests per sec | 300 requests per 15 min per App  <br>1 request per 1 sec per App |
| Granularity | Day, hour, minute | Day, hour, minute |
| Supports filtering using [annotations](https://developer.twitter.com/en/docs/twitter-api/annotations) |     | ✔   |
| Supports filtering using [conversation\_id](https://developer.twitter.com/en/docs/twitter-api/conversation-id) |     | ✔   |
| JSON key name for Tweet data array | results | data |
| Request parameters for selecting time period | fromDate  <br>toDate | start\_time  <br>end\_time |
| Request parameters for navigating by Tweet ID |     | since\_id  <br>until\_id |
| JSON key name for pagination | next | meta.next\_token |
| Request parameter for pagination | next\_token | next\_token or pagination\_token |
| Timezone | UTC | UTC |
| Requires the use of credentials from a [developer App](https://developer.twitter.com/en/docs/apps) associated with a [Project](https://developer.twitter.com/en/docs/projects) that has [Academic Research access](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level) |     | ✔   |