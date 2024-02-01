platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/edit-tweets

## Compliance support

The [Compliance Firehose](https://developer-staging.twitter.com/en/docs/twitter-api/enterprise/compliance-firehose-api/overview) and the v2 [batch compliance endpoint](https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance) have both been updated to provide edit Tweet support: 

A new "tweet\_edit" event type has been added to the Compliance Firehose. 

      `{   "tweet_edit": {     "id": <tweetId>,     "initial_tweet_id": <tweetId>,     "edit_tweet_ids": [<tweetId1>, <tweetId2>, <tweetId3> ...],     "timestamp_ms": "<timestampMsStr>"   } }`