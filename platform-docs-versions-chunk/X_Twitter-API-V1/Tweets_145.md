platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/curate-a-collection/overview/about_collections

## Differences with other methods

Those familiar with Twitter’s family of REST APIs may notice some differences in object structure compared to typical APIs.

Pay close attention to the differences in how collections are presented — often they will be decomposed, efficient objects with information about users, Tweets, and timelines grouped, simplified, and stripped of unnecessary repetition.

[Navigating collections](https://dev.twitter.com/rest/reference/get/collections/entries) also differs from the other APIs in that the collection is not strictly creation-time oriented. Navigating by since\_id and last\_id has been replaced with a position-based pagination system that should still be familiar.

See [Response structures](https://dev.twitter.com/rest/collections/responses) for a deeper overview of these differences.