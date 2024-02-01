platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/api-reference/get-statuses-mentions_timeline

GET statuses/mentions\_timeline

get-statuses-mentions\_timeline

# GET statuses/mentions\_timeline

**Important notice:** On June 19, 2019, we began enforcing a limit of 100,000 requests per day to the /statuses/mentions\_timeline endpoint. This is in addition to existing user-level rate limits (75 requests / 15-minutes). This limit is enforced on a per-application basis, meaning that a single developer app can make up to 100,000 calls during any single 24-hour period.

Returns the 20 most recent mentions (Tweets containing a users's @screen\_name) for the authenticating user.

The timeline returned is the equivalent of the one seen when you view [your mentions](http://twitter.com/mentions) on twitter.com.

This method can only return up to 800 tweets.

See [Working with Timelines](https://developer.twitter.com/en/docs/tweets/timelines/guides/working-with-timelines) for instructions on traversing timelines.