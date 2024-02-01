platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/curate-a-collection/overview/about_collections

About collections

### About Collections

Collections are a type of timeline that can be controlled and hand-curated, or programmed using an API.

As a unit, collections operate under the following rules:

* Collections are created by users.
* Each collection has a name and description.
* The collection creator can add any public Tweet to the collection.
* When new Tweets are added, they appear at the top of the collection.
* Collections are public, have their own URL on twitter.com, and are viewable by all.

By design, collections do not implement specific rules or logic for sourcing or adding Tweets, leaving that strategy entirely up to you. For example if you want a collection that sources Tweets from multiple lists + a search + your own secret sauce, you can build that easily using the API.