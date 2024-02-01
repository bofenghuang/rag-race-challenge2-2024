platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/bookmarks/introduction


### Bookmarks lookup

The Bookmarks lookup endpoint has one method available, GET. This method allows you to get Bookmarks back from yourself or an authenticated account. Pagination tokens will be provided for paging through large sets of results for this endpoint.

There is a per-user rate limit of 180 requests per 15 min window for the GET method. With this endpoint you will get back 800 of your most recent Bookmarked Tweets.

Since you are making requests on behalf of a user with the lookup Bookmarks endpoints, you must authenticate by generating a user Access Token with OAuth 2.0. You can use the [Authorization Code with PKCE grant flow](https://developer.twitter.com/en/docs/authentication/oauth-2-0/user-access-token) to do so. To use this endpoint you must pass in the scopes `tweet.read`, `users.read`, and `bookmark.read`.

**Account setup**

To access these endpoints, you will need:

* An approved [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info).
* To authenticate using the keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).

[Quick start](https://developer.twitter.com/en/docs/twitter-api/tweets/bookmarks/quick-start)

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Run in Postman](https://t.co/twitter-api-postman)

[Try with API Explorer](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Ftweets%2F%7Bid%7D%2Fbookmarks&method=get)