platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/quick-start/enterprise-account-activity-api


## Manage webhooks and subscribed users

**⏱ 10 min read**

The enterprise Account Activity API provides you webhook-based JSON messages any time there are events associated with Twitter accounts subscribed to your service. Twitter delivers those activities to your registered webhook. In the following steps, you will learn how to manage webhooks and subscribed users.

You will learn how to register, view, and remove, both webhooks and subscribed users. We'll be using simple cURL commands to make requests to the various API endpoints. cURL is a command-line tool for getting or sending requests using the URL syntax.

You will need:

* A registered Twitter app - _[register here](https://developer.twitter.com/content/developer-twitter/en/apps)_
* A bearer token - _[learn more](https://developer.twitter.com/content/developer-twitter/en/docs/basics/authentication/guides/bearer-tokens)_
* A webhook that passes a Challenge-Response Check (CRC) - _[learn more](https://developer.twitter.com/en/docs/accounts-and-users/subscribe-account-activity/guides/securing-webhooks)_
* An enterprise account - _[apply here](https://developer.twitter.com/en/enterprise)_

_Before you get started, we recommend you check out our [Github repo here](https://github.com/twitterdev/account-activity-dashboard) that provides a sample web app and helper scripts to get started with Twitter's Account Activity API_