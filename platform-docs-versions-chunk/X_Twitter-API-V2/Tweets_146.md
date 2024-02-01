platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/search/migrate


### Recent search comparison

The following table compares the various types of recent search endpoints:  

| **Description** | **Standard v1.1** | **Twitter API v2** |
| --- | --- | --- |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint path | /1.1/search/tweets.json | /2/tweets/search/recent |
| [Authentication](https://developer.twitter.com/en/docs/authentication) | OAuth 1.0a User Context  <br>OAuth 2.0 App-Only | OAuth 1.0a User Context<br><br>OAuth 2.0 Authorization Code with PKCE<br><br>OAuth 2.0 App-Only |
| Timestamp format | YYYYMMDD | YYYY-MM-DDTHH:mm:ssZ  <br>[ISO 8601 / RFC 3339](https://tools.ietf.org/html/rfc3339#section-5.6) |
| Returns Tweets that are no older than | 7 days | 7 days |
| HTTP methods supported | GET | GET |
| Default request rate limits | 180 requests per 15 min with OAuth 1.0a User Context<br><br>450 requests per 15 min with OAuth 2.0 App-Only | **Basic:**<br><br>60 requests per 15 min with OAuth 2.0 App-Only<br><br>60 requests per 15 min with OAuth 1.0a User Context<br><br>60 requests per 15 min with OAuth 2.0 Authorization Code with PKCE<br><br>**Pro:**<br><br>450 requests per 15 min with OAuth 2.0 App-Only<br><br>180 requests per 15 min with OAuth 1.0a User Context<br><br>180 requests per 15 min with OAuth 2.0 Authorization Code with PKCE |
| Offers fully unwound URLs |     | ✔   |
| Maximum Tweets per response (default) | 100 (15) | 100 (10) |
| Tweet JSON format | Standard v1.1 format | [Twitter API v2 format](https://developer.twitter.com/en/docs/twitter-api/data-dictionary) (determined by fields and expansions request parameters, not backward-compatible with v1.1 formats)<br><br>To learn more about how to migrate from the Standard v1.1 format to the Twitter API v2 format, please visit our [data formats migration guide](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats). |
| Supports selecting which [fields](https://developer.twitter.com/en/docs/twitter-api/fields) return in the payload |     | ✔   |
| Supports requesting and receiving [annotations](https://developer.twitter.com/en/docs/twitter-api/annotations) |     | ✔   |
| Supports requesting specific [metrics](https://developer.twitter.com/en/docs/twitter-api/metrics) within Tweet object |     | ✔   |
| Supports the [conversation\_id](https://developer.twitter.com/en/docs/twitter-api/conversation-id) operator and field |     | ✔   |
| Provides Tweet edit history | ✔   | ✔   |
| JSON key name for Tweet data array | statuses | data |
| JSON key name for pagination | search\_metadata.next\_results | meta.next\_token |
| Supports navigating archive by time range | ✔   | ✔   |
| Time resolution of time-based requests | day | second |
| Timezone | UTC | UTC |
| Request parameters for navigating by time | until | start\_time  <br>end\_time |
| Request parameters for navigating by Tweet ID | since\_id   <br>max\_id | since\_id   <br>until\_id |
| Request parameter for pagination | Provides URL-encoded query | next\_token |
| Requires the use of credentials from a [developer App](https://developer.twitter.com/en/docs/apps) associated with a [Project](https://developer.twitter.com/en/docs/projects) |     | ✔   |