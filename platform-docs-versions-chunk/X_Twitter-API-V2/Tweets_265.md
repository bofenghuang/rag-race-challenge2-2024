platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/get-tweets-search-stream-rules

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | string | Unique identifier of this rule. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. |
| `value` | string | The rule text as submitted when creating the rule. |
| `tag` | string | The tag label as defined when creating the rule. |
| `meta.sent` | number | The time when the request body was returned. |
| `errors` | object | Contains details about errors that affected any of the requested Tweets. See [Status codes and error messages](https://developer.twitter.com/en/support/twitter-api/error-troubleshooting) for more details. |