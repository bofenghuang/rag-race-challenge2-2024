platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/api-reference/get-statuses-home_timeline

GET statuses/home\_timeline

get-statuses-home\_timeline

# GET statuses/home\_timeline

Returns a collection of the most recent [Tweets](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object) and Retweets posted by the authenticating user and the users they follow. The home timeline is central to how most users interact with the Twitter service.

Up to 800 Tweets are obtainable on the home timeline. It is more volatile for users that follow many users or follow users who Tweet frequently.

See [Working with Timelines](https://developer.twitter.com/en/docs/tweets/timelines/guides/working-with-timelines) for instructions on traversing timelines efficiently.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/statuses/home_timeline.json`