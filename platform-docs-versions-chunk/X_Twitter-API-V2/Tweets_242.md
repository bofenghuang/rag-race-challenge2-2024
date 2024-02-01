platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/matching-returned-tweets


## Matching returned Tweets to their associated rule

The filtered stream endpoint gives you the ability to have multiple rules in place through a single connection. Before you start receiving Tweets in your stream, you’ll need to create a rule which specifies what types of Tweets you’re interested in. 

When you specify your rules to match Tweets based on a wide variety of attributes, including user attributes, geo-location, language, and many others, you can attach a tag to distinguish this rule at a higher level. Tags are a good way to contextualize your rule, especially if you have many rules in place. The filtering rules determine which Tweet activities will be sent through the connection.

If you need to add a new filtering rule to capture a different type of Tweet, or remove an existing rule, your app can send a request to the [POST tweets/search/stream/rules](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/post-tweets-search-stream-rules.html) endpoint to make it happen. When that request is sent, the filtering rules are automatically modified and the changes simply take effect in the data stream with no need to reconnect. Most rule additions take effect  about 20 seconds or less. It’s unlikely, but depending on external factors (for example, network connectivity), it may take longer before you start receiving matching Tweets. If you can’t find a rule in the list rule endpoint, make sure that the rule creation request succeeded; this can be done by checking your logs for any error messages.