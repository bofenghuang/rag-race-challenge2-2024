platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/migrate/powertrack-api-migration-to-twitter-api-v2


## PowerTrack API migration to Twitter API v2 filtered stream

Use this migration guide to understand the similarities and differences between [PowerTrack API](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/overview.html) and Twitter API v2 [filtered stream](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/introduction.html), and to help migrate a current PowerTrack API integration to v2 filtered stream.

* **Similarities**
    * Streaming delivery method
    * Integration process
    * Persistent stream connection with separate rules management endpoints
    * Rule syntax
    * Rule operators (with exceptions)
    * Rule matching logic
    * Support for Tweet edit history and metadata
* **Differences**
    * Rule length
    * Rule volume
    * Endpoint URLs
    * App and Project requirement for access
    * Authentication method
    * Request parameters
    * Usage tracking
    * Multiple streams, redundant conections, backfill and Replay recovery
    * Request parameters and response format
    * Response JSON data structure