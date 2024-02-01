platform: X
topic: Twitter-API-V2
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/users/mutes/introduction


### Manage mutes

The manage mute endpoints enable you to mute or unmute a specified account on behalf of an authenticated user. For these endpoints, there are two methods available: POST and DELETE. The POST method allows you to mute an account, and the DELETE method allows you to unmute an account. There is a user rate limit of 50 requests per 15 minutes for both the POST and DELETE endpoints.

**Please note:** If a user mutes from [Twitter](https://twitter.com/), there is a limit of 200 requests per 15 minutes.

**Account setup**

To access these endpoints, you will need:

* An approved [developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info).
* To authenticate using the keys and tokens from a [developer App](https://developer.twitter.com/en/docs/apps) that is located within a [Project](https://developer.twitter.com/en/docs/projects). 

Learn more about getting access to the Twitter API v2 endpoints in our [getting started guide](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api).

[Quick start](https://developer.twitter.com/en/docs/twitter-api/users/mutes/quick-start)

[Sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Run in Postman](https://t.co/twitter-api-postman)

[Try with API Explorer](https://developer.twitter.com/apitools/api?endpoint=/2/users/%7Bid%7D/muting&method=get)