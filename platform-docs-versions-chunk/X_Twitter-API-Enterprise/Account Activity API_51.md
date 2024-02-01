platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/migration/us-ss-migration-guide

### Managing user subscriptions

The Account Activity API allows multiple subscriptions for a single registered webhook.  This allows multiple user subscriptions activities to be delivered to the same location, similar to the Site Streams architecture, with webhooks.  This means you can track subscriptions, as they pertain to your subscription limits, independently from the webhook connection.  This also allows scalability from only one or a few subscriptions to thousands of subscriptions for a single webhook.

### **How to Migrate**