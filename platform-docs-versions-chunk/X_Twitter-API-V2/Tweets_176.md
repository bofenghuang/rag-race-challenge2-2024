platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/counts/introduction


### Full-archive Tweet counts

Academic Research or Enterprise access only

The full-archive Tweet counts endpoint allows you to programmatically retrieve the numerical count of Tweets for a query, from the entire archive of public Tweets. Currently, this endpoint is only available to those that have been approved for [Academic Research or Enterprise access](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level) and use the [OAuth 2.0 App-Only](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-2-0) for authentication.

One example: You could use the full-archive Tweet counts endpoint to see the number of Tweets for the hashtag #SOSHurricaneHarvey per day between August and September 2017.

**Please note:** The counts endpoint paginates at 31 days per response. For example, setting a day granularity, will return the count of results per day for 31 days per page.  Setting an hour granularity, will return the count of results per hour for 744 (31 days x 24 hours) hours per page.  If you do not specify the granularity and time period, this endpoint will give you Tweet counts for a query per hour, for the last 30 days.

[Quick start](https://developer.twitter.com/en/docs/twitter-api/tweets/counts/quick-start)

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Search Tweets Python client](https://github.com/twitterdev/search-tweets-python)

[Run in Postman](https://t.co/twitter-api-postman)

[Try with API Explorer](https://developer.twitter.com/apitools/api?endpoint=/2/tweets/counts/recent&method=get)