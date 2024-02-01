platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/introduction


## Introduction

Creating and deleting Tweets using the Twitter API is essential for engaging with the public conversation. The new manage Tweets endpoints allow you to do just that and much more. 

We have two available methods for manage Tweets, POST and DELETE. The POST method lets you post polls, quote Tweets, Tweet with reply settings, Tweet with geo, Tweet with media and tag users, and Tweet to Super Followers, in addition to other features. Likewise, the DELETE method allows you to delete a specific Tweet. For the POST method, you can pass in [the parameters](https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/api-reference) you are looking for to enable you to further customize your request.

The 'delete Tweet' method has been updated to support edited Tweets. When any Tweet in a chain of Tweet edits is deleted, all Tweets in that edit chain are also deleted. To learn more about Edit Tweet metadata, check out the [Edit Tweets fundamentals](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/edit-tweets) page.

There is a user rate limit of 200 requests per 15 minutes for the POST method. The DELETE method has a rate limit of 50 requests per 15 minutes. Additionally, there is a limit of 300 requests per 3 hours, including Tweets created with either manage Tweets or manage Retweets. 

Since you are making requests on behalf of a user with the manage Tweets endpoints, you must authenticate with either [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code), and use a user Access Tokens associated with a user that has authorized your App. To generate this user Access Token with OAuth 1.0a, you can use the [3-legged OAuth flow](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens). To generate a user Access Token with OAuth 2.0, you can use the [Authorization Code with PKCE grant flow](https://developer.twitter.com/en/docs/authentication/oauth-2-0/user-access-token).

**Account setup**

To access these endpoints, you will need:

* An approved [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info).
* To authenticate using the keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).

[Quick start](https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/quick-start)

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Run in Postman](https://t.co/twitter-api-postman)

[Try with API Explorer](https://developer.twitter.com/apitools/api?endpoint=/2/tweets&method=post)