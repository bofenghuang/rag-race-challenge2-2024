platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/managing-webhooks-and-subscriptions


### Adding & removing User subscriptions

Support for thousands of subscriptions is available with the enterprise tier. If you already have an account manager, please reach out to them with questions.  To apply for access to the enterprise APIs, [click here](https://developer.twitter.com/content/developer-twitter/en/enterprise).   

#### Subscription management endpoints  
 

|     |     |
| --- | --- |
| Method | Enterprise |
| Add new user subscription | [POST webhooks/:webhook\_id/subscriptions/all](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#post-account-activity-webhooks-webhook-id-subscriptions-all) |
| Retrieve a user subscription | [GET webhooks/:webhook\_id/subscriptions/all](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#get-account-activity-webhooks-webhook-id-subscriptions-all) |
| Returns a list of all active subscriptions | [GET webhooks/:webhook\_id/subscriptions/all/list](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#get-account-activity-webhooks-webhook-id-subscriptions-all-list) |
| Deactivates a user subscription using application only OAuth | [DELETE webhooks/:webhook\_id/subscriptions/:user\_id/all.json](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise#delete-account-activity-webhooks-webhook-id-subscriptions-user-id-all-json) |