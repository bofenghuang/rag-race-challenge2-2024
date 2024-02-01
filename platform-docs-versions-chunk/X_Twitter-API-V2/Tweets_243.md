platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/matching-returned-tweets


### Matching rules

When an activity is delivered through your filtered stream connection, in a matching\_rules array, it contains which list of filters matched against the Tweet delivered.

In the Tweet payload there is additional string metadata which includes the rule id and tag that caused a specific Tweet to be delivered. If multiple rules match a single Tweet, the activity is delivered a single time with each of the matching rules included in this metadata. The matching rules provide an easy way to associate a specific Tweet with specific rules, which is especially helpful if you have many distinct rules. Since the data is delivered through a single stream in this manner, ensuring you have unique id and tag is essential for matching. 

#### Here is an example of how the ”matching\_rules” array appears in the Tweet payload:  
 

      `"matching_rules": [     {       "id": "1166916266197536768",       "tag": "test-rule-tag-00000"     },     {       "id": "1166916266197536769",       "tag": "test-rule-tag-12345"     }   ]`