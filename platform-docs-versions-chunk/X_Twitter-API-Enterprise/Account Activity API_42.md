platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/activity-replay-api

### Limitations

Replay is intended as a tool for easily recovering activities as far back as five days ago, but it will not deliver events prior to a subscription’s creation time. For example, if three days ago, you added a new subscription and ran a Replay job with a window for five days prior to today, you would only receive data for the three days that this new subscription was active.