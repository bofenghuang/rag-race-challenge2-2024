platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/migrate


## Comparing Twitter API’s filtered stream endpoints

The v2 filtered stream endpoints group is replacing the [standard v1.1 statuses/filter](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/filter-realtime/api-reference/post-statuses-filter) and [PowerTrack API](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api). If you have code, apps, or tools that use an older version of the filtered stream endpoint, and are considering migrating to the newer Twitter API v2 endpoint, then this comparison can help you get started. 

See our more in depth migration guides for:

[Migrating from Standard v1.1 compared to Twitter API v2](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/migrate/standard-to-twitter-api-v2)

[Migrating from PowerTrack API migration to Twitter API v2](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/migrate/powertrack-api-migration-to-twitter-api-v2)

The following table compares the filtered streaming endpoints Twitter offers:  
 

| **Description** | **Standard v1.1** | **PowerTrack API** | **Twitter API v2** |
| --- | --- | --- | --- |
| Access | Twitter App | Requires an enterprise contract and account | Requires a developer account ([sign up](https://developer.twitter.com/en/portal/petition/essential/basic-info)), and [Twitter App](https://developer.twitter.com/en/docs/apps) within a [Project](https://developer.twitter.com/en/docs/projects) |
| --- | --- | --- | --- |
| Host domain | ******https://stream.twitter.com****** | ******https://gnip-stream.twitter.com****** | ******https://api.twitter.com****** |
| Endpoint path | ******1.1/statuses/filter.json****** | ******/stream/powertrack/accounts/{gnip\_account\_name}/publishers/twitter/{stream\_label}.json******<br><br>******/rules/powertrack/accounts/{gnip\_account\_name}/publishers/twitter/{stream\_label}.json****** <br><br>******/rules/powertrack/accounts/{gnip\_account\_name}/publishers/twitter/{stream\_label}/validation.json****** | ******/2/tweets/search/stream******<br><br>******/2/tweets/search/stream/rules****** |
| [Authentication](https://developer.twitter.com/en/docs/authentication) | OAuth 1.0a User Context | HTTP Basic Authentication | OAuth 2.0 App-Only |
| HTTP methods supported | POST | GET  <br>POST | GET  <br>POST |
| Required parameters | Rule defined on connection as parameter, at least one of:<br><br>* ******follow******<br>* ******track******<br>* ******locations****** | No required parameters for streaming connection, optional backfill parameter.<br><br>Rules managed separately | No required parameters for streaming connection, optional parameters to define response format and add [backfill recovery feature](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/recovering-missing-data) for Academic Research access.<br><br>Rules managed separately |
| Delivery type | Streaming | Streaming<br><br>REST (for rules management) | Streaming<br><br>REST (for rules management) |
| Default request rate limits | 5 connection attempts per 5 min | 60 requests per min aggregated for both POST and GET requests<br><br>/rules:  60 requests per minute, aggregated across all requests to /rules endpoint for the specific stream’s API (POST and GET). | Depends on the endpoint and the [access level](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level).<br><br>[GET /2/tweets/search/stream](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/get-tweets-search-stream):  <br>Pro - 50 requests per 15-minutes per App<br><br>[GET /2/tweets/search/stream/rules](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/get-tweets-search-stream-rules):  <br>Pro - 450 requests per 15-minutes per App<br><br>\---<br><br>[POST /2/tweets/search/stream/rules](https://developer-staging.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/post-tweets-search-stream-rules):  <br>Pro - 100 requests per 15 minutes per App |
| Maximum allowed connections | 2 concurrent per authorized user | Supports multiple/redundant connections, determined by contract | Pro access:  <br>1 |
| [Recovery and redundancy features](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/recovery-and-redundancy-features) | None | Backfill, redundant connections, and the Replay API |     |
| [Tweet caps](https://developer.twitter.com/en/docs/twitter-api/tweet-caps) | Limited to 1% of firehose | Determined by contract | There is a monthly, Project-level Tweet cap applied to all Tweets received from this endpoint:<br><br>Basic:  <br>10,000 Tweets<br><br>Pro:  <br>1 million Tweets |
| Keep-alive signal/heartbeats | blank lines (\\r\\n or similar) at least every 20 seconds | blank lines (\\r\\n or similar) every 10 seconds | blank lines (\\r\\n or similar) at least every 20 seconds |
| Latency | 10 seconds | 2 seconds<br><br>At least 10 seconds for URL unwinding enrichment | 10 seconds |
| Maximum allowed rules | 1 rule (within the endpoint connection request) | Determined by contract up to 250,000 | Pro access:  <br>1000 rules |
| Rule filter limitations | One query per connection, up to either:<br><br>\- 400 track keywords<br><br>\- 5000 follow user IDs<br><br>\- 25 location boxes | Up to 2,048 characters per rule | Pro Access:   <br>1,024 characters per rule |
| Tweet [JSON format](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction) | Standard v1.1 format | [Native Enriched](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/tweet.html) or [Activity Streams](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/activity.html) (selected within the [console](https://developer.twitter.com/en/docs/twitter-api/enterprise/console/overview.html)) | [Twitter API v2 format](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/data-dictionary) (determined by ******fields****** and ******expansions****** request parameters, not backward-compatible with v1.1 formats)<br><br>To learn more about how to migrate from the Standard v1.1 format to the Twitter API v2 format, please visit our [data formats migration guide](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats). We will be releasing additional data format migration guides for Native Enriched and Activity Streams soon. |
| Provides Tweet edit history and metadata | ✔   | ✔   | ✔   |
| Unique Features | Filtering done via query parameters on connection request<br><br>No configuration UI | Filtering done via rules created through an independent endpoint<br><br>[Enrichment](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview) features available in contract<br><br>Configuration on console.gnip.com UI | Filtering done via [rules](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/build-a-rule) created through an independent endpoint<br><br>[Metrics](https://developer.twitter.com/en/docs/twitter-api/metrics) and URL enrichment features included<br><br>Object [fields](https://developer.twitter.com/en/docs/twitter-api/fields) and  [expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) specified with request parameters<br><br>Tweet [Annotations](https://developer.twitter.com/en/docs/twitter-api/annotations)<br><br>[Conversation ID](https://developer.twitter.com/en/docs/twitter-api/conversation-id) operator and field<br><br>Configuration through [developer portal](https://developer.twitter.com/en/docs/developer-portal) |