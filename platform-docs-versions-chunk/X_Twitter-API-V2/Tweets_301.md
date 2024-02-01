platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/volume-streams/migrate


## Comparing Twitter API’s sample stream endpoints

The v2 sampled stream endpoint is replacing the v1.1 [statuses/sample](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/sample-realtime/overview/get_statuses_sample) endpoint. If you have some code, apps, or tools that use an older version of the sample stream endpoint, and are considering migrating to the newer Twitter API v2 endpoint, then this set of guides is for you. 

The following tables compare the various types of sampled stream endpoints:

| **Description** | **Standard v1.1** | **Twitter API v2** |
| --- | --- | --- |
| Host domain | ********https://stream.twitter.com******** | ********https://api.twitter.com******** |
| Endpoint path | ********1.1/statuses/sample.json******** | ********/2/tweets/sample/stream******** |
| [Authentication](https://developer.twitter.com/en/docs/authentication) | OAuth 1.0a User Context | OAuth 2.0 App-Only |
| HTTP methods supported | GET | GET |
| Default request rate limits | 8 connection requests per minute | 50 connection requests per 15 min |
| Maximum allowed connections | 2   | 1   |
| [Recovery and redundancy features](https://developer.twitter.com/en/docs/twitter-api/tweets/sampled-stream/integrate/recovery-and-redundancy-features) | None | Essential and Elevated [access levels](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level):  <br>None<br><br>Academic research access level:  <br>Backfill and redundant connections |
| New [JSON format](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction) | Standard v1.1 format | [Twitter API v2 format](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/data-dictionary) (determined by **fields** and **expansions** request parameters, not backward-compatible with v1.1 formats)<br><br>To learn more about how to migrate from the Standard v1.1 format to the Twitter API v2 format, please visit our [data formats migration guide](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats). |
| Supports selecting which [fields](https://developer.twitter.com/en/docs/twitter-api/fields) return in the payload | No, data format pre-determined | ✔   |
| Supports specifying the language of Tweets returned | ✔   |     |
| Supports the [annotations](https://developer.twitter.com/en/docs/twitter-api/annotations) field |     | ✔   |
| Supports requesting specific [metrics](https://developer.twitter.com/en/docs/twitter-api/metrics) |     | ✔   |
| Supports the [conversation\_id](https://developer.twitter.com/en/docs/twitter-api/conversation-id) field |     | ✔   |
| Provides Tweet edit history | ✔   | ✔   |
| Requires the use of credentials from a [developer App](https://developer.twitter.com/en/docs/apps) associated with a [Project](https://developer.twitter.com/en/docs/projects) |     | ✔   |