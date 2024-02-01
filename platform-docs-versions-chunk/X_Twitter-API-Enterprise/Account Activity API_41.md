platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/activity-replay-api


### Using Account Activity Replay API

If your account is configured with Replay functionality, you can make requests in a similar manner as requests to the Account Activity API. It is important to note that your request must specify a webhook id parameter to indicate which webhook’s activities you would like to replay. In other words, a Replay request asks Account Activity Replay API to retrieve events from a start date and time to an end date and time based on the webhook id and application id.

Please note that UTC time is expected. These activities are delivered through the registered webhook associated with the id at a rate of up to 2,500 events per second. Also keep in mind that only one Replay job per webhook may be running at a time, although all subscriptions that were active during the date/time specified on that webhook will be replayed.

Events are delivered beginning with the first (oldest) minute of the specified time period, continuing chronologically (as best as possible) until the final minute is delivered. At that point, Replay will deliver a [job completion event](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference/replay-api#job-completed-successfully-message) to the webhook. Because we work chronologically in delivering activities, if there are little or no matching results near the start time, there will likely be a period of time before the first results are delivered.