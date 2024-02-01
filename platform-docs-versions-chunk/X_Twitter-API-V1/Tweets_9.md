platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/api-reference/get-search-tweets

Standard search API

get-search-tweets

# Standard search API

Returns a collection of relevant [Tweets](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object) matching a specified query.

Please note that Twitter's search service and, by extension, the Search API is not meant to be an exhaustive source of Tweets. Not all Tweets will be indexed or made available via the search interface.

To learn how to use [Twitter Search](https://twitter.com/search) effectively, please see the [Standard search operators](https://developer.twitter.com/en/docs/tweets/search/guides/standard-operators) page for a list of available filter operators. Also, see the [Working with Timelines](https://developer.twitter.com/en/docs/tweets/timelines/guides/working-with-timelines) page to learn best practices for navigating results by `since_id` and `max_id`.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/search/tweets.json`