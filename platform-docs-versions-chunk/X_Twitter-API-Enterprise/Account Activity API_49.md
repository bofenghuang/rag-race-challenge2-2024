platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/migration/us-ss-migration-guide

### Differences & migration considerations

**API format:** The new Account Activity API operates differently than User Streams and Site Streams. You will need to alter your web app to receive data with webhooks. You can find more information on webhooks [here](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/getting-started-with-webhooks).

**Data Available:** Another key difference you will notice is in regards to the data being delivered. Twitter will no longer send events from people that you follow on Twitter (aka your home timeline). This was an intentional change and is not something we plan to alter going forward.

**Reliability:** Unlike streaming, webhooks enable confirmation of delivery and options to retry POSTed activities that do not make it to the webhook URL.  This gives more assurance that the app is receiving all applicable activities, even if there are brief disconnections or periods of downtime.