platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/search/introduction


### Full-archive search

The v2 full-archive search endpoint is only available to Projects with [Enteprise](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level) access. The endpoint allows you to programmatically access public Tweets from the complete archive dating back to the first Tweet in March 2006, based on your search query.

You can authenticate your requests to this endpoint using [OAuth 2.0 App-Only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only), and the [App Access Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens) must come from an App that is within a Project that has Enterprise access. Since you cannot make a request on behalf of other users (OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE) with this endpoint, you will not be able to pull private [metrics](https://developer.twitter.com/en/docs/twitter-api/metrics). 

This endpoint can deliver up to 500 Tweets per request in reverse-chronological order, and [pagination](https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/paginate) tokens are provided for paging through large sets of matching Tweets.

**Note:** If requesting [annotations](https://developer.twitter.com/en/docs/twitter-api/annotations/overview.html) through the tweet.fields parameter, the max\_results parameter is currently limited to a max value of 100. This may change in the future, but please be mindful of this limitation.

Since this endpoint is only available to those that have been approved for Enterprise access, you have access to the full set of search [operators](https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-rule) and can make queries up to 1024 characters long.

[Quick start](https://developer.twitter.com/en/docs/twitter-api/tweets/search/quick-start)

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Search Tweets Python client](https://github.com/twitterdev/search-tweets-python)

[Search Tweets Ruby client](https://github.com/twitterdev/search-tweets-ruby)

[Run in Postman](https://t.co/twitter-api-postman)

[Try with API Explorer](https://developer.twitter.com/apitools/api?endpoint=/2/tweets/search/recent&method=get)

[Search and Visualize Tweets](https://developer.twitter.com/en/docs/tutorials/developer-guide--twitter-api-toolkit-for-google-cloud)