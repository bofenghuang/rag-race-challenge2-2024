platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/customer-feedback/api-reference/events

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |
| --- | --- |
| **from\_time** (required) | Required on the 1st page. Epoch timestamp in milliseconds. Example: 1451936737470<br><br>The range is inclusive. |
| **to\_time** (required) | Required on the 1st page. Epoch timestamp in milliseconds. Example: 1451936737470<br><br>The range is inclusive. The max to\_time is 24 hours before current time. Requests for more recent data via this endpoint will receive an error. |
| **count** (required) | Max number of results returned. Default and max is 100. |
| **cursor** (optiona) | For paging through results. Required for paging through result sets greater than 1 page.<br><br>An empty value indicates you have reached the end of the result set. |