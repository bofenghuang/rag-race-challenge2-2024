platform: X
topic: Twitter-API-Enterprise
subtopic: Search API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Search API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/overview

### Retry Logic

If you experience a 503 error with the enterprise search APIs, it is likely a transient error and can be resolved by re-trying the request a short time later.

If the request fails 4 times in a row, and you have waited at least 10 minutes between failures, use the following steps to troubleshoot:

* Retry the request after reducing the amount of time it covers. Repeat this down to a 6-hour time window if unsuccessful.
* If you are ORing a large number of terms together, split them into separate rules and retry each individually.
* If you are using a large number of exclusions in your rule, reduce the number of negated terms in the rule and retry.