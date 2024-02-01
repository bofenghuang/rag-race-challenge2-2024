platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/matching-returned-tweets


### Rule tags

At the time they are created, each filtering rule may be created with a tag. Rule tags have no special meaning as they are simply treated as opaque strings carried along with a rule. They will be included in the matching\_rules metadata in activities returned, and are aimed at making distinguishing your rules easier at a higher level. 

Tags provide an easy way to create logical groupings of filtering rules. For example, you may generate a unique ID for a specific rule as its tag, and allow your app to reference that ID within activities it processes to associate a result with specific customers, campaigns, categories, or other related groups.

Note that tags cannot be updated on an existing rule and can only be included when a rule is created. In order to “update” or “rename” a tag, you need to first delete the rule, then add it again with the desired tag. The best solution is to simply use a unique identifier as your tag, which your system can associate with various other data points within your own app, all without having to change anything in the rule set.