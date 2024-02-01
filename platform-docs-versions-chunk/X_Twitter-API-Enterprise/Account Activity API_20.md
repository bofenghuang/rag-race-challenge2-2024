platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/securing-webhooks

Securing webhooks

## Securing webhooks

Twitter's webhook-based APIs provide two methods for confirming the security of your webhook server:

1. The challenge-response checks enable Twitter to confirm the ownership of the web app receiving webhook events. 
2. The signature header in each POST request enables you to confirm that Twitter is the source of the incoming webhooks.