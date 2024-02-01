platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/managing-webhooks-and-subscriptions


### Creating & changing webhooks

In order to change webhook URLs, you must delete your existing webhook and then create a new one. Note that when you do this, you will be required to re-add user subscriptions to the new webhook.

#### Webhook configuration management endpoints:  
  

|     |     |
| --- | --- |
| **Method** | Enterprise |
| Registers a webhook URL / Generates a webhook\_id | [POST webhooks](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#post-account-activity-webhooks) |
| Returns all webhook URLs and their statuses | [GET webhooks](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#get-account-activity-webhooks) |
| Delete app’s current webhook configuration | [DELETE webhooks/:webhook\_id](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#delete-account-activity-webhooks-webhook-id) |
| Manually trigger a CRC request | [PUT webhooks/:webhook\_id](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#put-account-activity-webhooks-webhook-id) |

#### Why can’t I just update the webhook URL?

Why are webhook configurations immutable? Twitter takes security very seriously. If your webhook URL is changed, there is a possibility that your application consumer key and consumer secret have been compromised. By requiring you to create a new webhook configuration, you are also required to re-subscribe to your user’s events. This requires the use of access tokens that a malicious party is less likely to possess. As a result, the likelihood that another party will receive your user’s private information is reduced.