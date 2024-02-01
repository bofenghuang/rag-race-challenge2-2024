platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/migration/us-ss-migration-guide

### New features

The Account Activity API offers many new features, most notably that data is now delivered via webhooks as opposed to streaming. Webhooks offer many benefits compared to streaming, but the most prominent are speed and reliability. The API will send you data in the form of JSON events as they become available and you will no longer need to maintain an active connection or poll the endpoint. This limits the need for redundancy features and increases efficiency overall. More information on webhooks can be found in the [technical documentation](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/getting-started-with-webhooks).