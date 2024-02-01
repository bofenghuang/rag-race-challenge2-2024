platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/authenticating-with-the-account-activity-api

Authenticating with the Account Activity API

**Please note**: 

Twitter needs to enable access to the Account Activity API for your developer App before you can start using the API. To this end, make sure to share the App ID that you intend to use for authentication purposes with your account manager or technical support team.

The [Account Activity API](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/overview) consists of a set of endpoints that allow you to create and manage user subscriptions to receive real-time account activities for all of your subscribed accounts through a single connection. 

There are two authentication methods available with the Account Activity API ([OAuth 1.0a](https://developer.twitter.com/en/docs/tutorials/authenticating-with-twitter-api-for-enterprise/authentication-method-overview#oauth1.0a) and [OAuth 2.0 Bearer Token](https://developer.twitter.com/en/docs/tutorials/authenticating-with-twitter-api-for-enterprise/authentication-method-overview#oauth2.0)). The authentication method that you should use will depend on which endpoint you are using.

|     |     |     |     |
| --- | --- | --- | --- |
| **Description** | **Endpoint** | OAuth 1.0a  <br>(user context) | OAuth 2.0 Bearer Token (application-only) |
| Register a new webhook URL for the given application context | [POST account\_activity/webhooks](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#post-account-activity-webhooks) | ✓   |     |
| Return all URLs and their statuses for the given application | [GET account\_activity/webhooks](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#get-account-activity-webhooks) |     | ✓   |
| Trigger a challenge response check (CRC) for a given webhook's URL | [PUT account\_activity/webhooks/:webhook\_id](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#put-account-activity-webhooks-webhook-id) | ✓   |     |
| Subscribe the application to a user’s account events | [POST account\_activity/webhooks/:webhook\_id/subscriptions/all](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#post-account-activity-webhooks-webhook-id-subscriptions-all) | ✓ \* |     |
| Return a count of currently active subscriptions | [GET account\_activity/subscriptions/count](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#get-account-activity-subscriptions-count) |     | ✓   |
| Check if a webhook configuration is subscribed to a user’s events | [GET account\_activity/webhooks/:webhook\_id/subscriptions/all](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#get-account-activity-webhooks-webhook-id-subscriptions-all) | ✓ \* |     |
| Return a list of currently active subscriptions | [GET account\_activity/webhooks/:webhook\_id/subscriptions/all/list](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#get-account-activity-webhooks-webhook-id-subscriptions-all-list) |     | ✓   |
| Delete a webhook | [DELETE account\_activity/webhooks/:webhook\_id](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#delete-account-activity-webhooks-webhook-id) | ✓   |     |
| \[DEPRECATED\] Deactivate a subscription for the provided user context and application | [DELETE account\_activity/webhooks/:webhook\_id/subscriptions/all](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#delete-account-activity-webhooks-webhook-id-subscriptions-all-deprecated-) | ✓ \* |     |
| Deactivate a subscription using application-only OAuth | [DELETE /account\_activity/webhooks/:webhook\_id/subscriptions/:user\_id/all.json](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#delete-account-activity-webhooks-webhook-id-subscriptions-user-id-all-json) |     | ✓   |
| Redelivers activities to a webhook | [POST /1.1/account\_activity/replay/webhooks/:webhook\_id/subscriptions/all.json](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/replay-api) |     | ✓   |

\* _Authentication requires the access tokens of the subscribing user._ 

For those endpoints that require OAuth 1.0a user context authentication, you will need to provide the following credentials to authenticate the request: 

* Consumer Keys (API Key and Secret)
* Access Tokens (Access Token and Secret)

In the case of the following three endpoints, you perform write actions within the context of your application (no Twitter users are involved). Therefore, the Access Tokens you need to provide are the ones belonging to your developer App. These can be generated directly from within the [developer portal](https://developer.twitter.com/en/portal/projects-and-apps), under the “Keys and tokens” tab for your App.  

* [POST account\_activity/webhooks](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#post-account-activity-webhooks): Register a new webhook URL for the given application context
* [PUT account\_activity/webhooks/:webhook\_id](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#put-account-activity-webhooks-webhook-id): Trigger a challenge response check (CRC) for a given webhook's URL
* [DELETE account\_activity/webhooks/:webhook\_id](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#delete-account-activity-webhooks-webhook-id): Delete a webhook

On the other hand, in the case of the following three endpoints, you are making a request that allows your application to access protected data on behalf of a Twitter user (for example, Direct Messages). You must therefore provide the Access Tokens that belong to the subscribing user in question. The required Access tokens can be obtained using the 3-legged OAuth flow (see [OAuth 1.0a: how to obtain a user’s Access Tokens](https://developer.twitter.com/en/docs/tutorials/authenticating-with-twitter-api-for-enterprise/oauth1-0a-and-user-access-tokens)). These endpoints have been marked with an asterisk in the above table (\*).

* [POST account\_activity/webhooks/:webhook\_id/subscriptions/all](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#post-account-activity-webhooks-webhook-id-subscriptions-all): Subscribe the application to a user’s account events
* [GET account\_activity/webhooks/:webhook\_id/subscriptions/all](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#get-account-activity-webhooks-webhook-id-subscriptions-all): Check if a webhook configuration is subscribed to a user’s events
* [DELETE account\_activity/webhooks/:webhook\_id/subscriptions/all](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#delete-account-activity-webhooks-webhook-id-subscriptions-all-deprecated-): Deactivate a subscription for the provided user context and application \[DEPRECATED\]

**Please note**: 

Make sure that your developer App is enabled for "Read, Write, and Direct Messages." You can change this setting in the [Projects & Apps section](https://developer.twitter.com/en/portal/projects-and-apps) of your developer account, under “App permissions” for the selected developer App. You will need to regenerate your App credentials after changing the permissions settings.

A list of all endpoints available with the Account Activity API, including associated description and example cURL requests with authentication implementation examples, can be found in [the API reference documentation](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise).

For additional information, check out TwitterDev’s [sample web app and helper scripts](https://github.com/twitterdev/account-activity-dashboard-enterprise) to get started with the Enterprise Account Activity API.