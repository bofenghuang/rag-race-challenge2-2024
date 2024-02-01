platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/activity-replay-api

### Data availability and types

Activities from the Account Activity Replay API are available five days from the initiation of the request, with new data becoming available roughly 10 minutes after a given activity is created. You will be able to make requests specifying a timeframe within this five day window using the from\_date and to\_date parameters within the request. Events that were originally delivered prior to having access to Replay cannot be replayed. For example, if your account was enabled for access to the Account Activity Replay API on June 1, 2019 at 3:30PM UTC, you would not be able to use Replay to retrieve any events prior to that date and time.

Continue to the [Account Activity Replay API reference](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference/replay-api)