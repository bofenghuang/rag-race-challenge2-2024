platform: X
topic: Twitter-API-V2
subtopic: Compliance
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Compliance.md
url: https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance/api-reference/get-compliance-jobs

### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `type`  <br> Required | enum (`tweets`, `users`) | Allows to filter by job type - either by tweets or user ID. Only one filter (tweets or users) can be specified per request. |
| `status`  <br> Optional | enum (`created`, `in_progress`, `failed`, `complete`) | Allows to filter by job status. Only one filter can be specified per request.  <br>Default: `all` |