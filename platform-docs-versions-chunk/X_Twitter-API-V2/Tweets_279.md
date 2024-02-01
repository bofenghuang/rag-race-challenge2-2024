platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/post-tweets-search-stream-rules


### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `id` | string | Unique identifier of this rule. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. |
| `value` | string | The rule text as submitted when creating the rule. |
| `tag` | string | The tag label as defined when creating the rule. |
| `meta`  <br> Default | object | Contains information about when the rule was created, and whether the rule was either created or not created, or deleted or not deleted. |
| `meta.sent`  <br> Default | number | The time when the request body was returned. |
| `meta.summary`  <br> Default | object | Contains fields that describe whether you were successful or unsuccessful in creating or deleting the different rules that you passed in your request. |
| `errors` | object | Contains details about errors that affected any of the requested Tweets. See [Status codes and error messages](https://developer.twitter.com/en/support/twitter-api/error-troubleshooting) for more details. |