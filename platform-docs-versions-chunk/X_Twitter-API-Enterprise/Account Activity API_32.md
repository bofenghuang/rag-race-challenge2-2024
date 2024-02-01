platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/activity-retries

Activity retries

## Retries

Enterprise

One of the benefits of the enterprise tier of the Account Activity API is a retry mechanism for webhook events. If a 'success' 200 HTTP response code is not received, the Twitter server will initiate a retry mechanism, resending the webhook event up to three times over a five-minute period. This webhook event retry service helps provide reliability and event recovery when network problems occur and during client-side service interruptions and deploys.