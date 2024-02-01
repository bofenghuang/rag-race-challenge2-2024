platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/migrate/standard-to-twitter-api-v2

## Standard v1.1 compared to Twitter API v2

If you have been working with the standard v1.1 GET statuses/show and GET statuses/lookup, the goal of this guide is to help you understand the similarities and differences between the standard and Twitter API v2 Tweets lookup endpoints..

You may also be interested in our [visual data format migration tool](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats/visual-data-format-migration-tool) to help you quickly see the differences between the [Twitter API v1.1 data format](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/overview/intro-to-tweet-json) and the [Twitter API v2 format](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction).

* **Similarities**
    * OAuth 1.0a User Context
    * Tweets per request limits
    * Support for Tweet edit history and metadata 
* **Differences**
    * Endpoint URLs
    * App and Project requirements
    * Response data format
    * Request parameters