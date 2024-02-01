platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const recentSearch =       await twitterClient.tweets.tweetsRecentSearch({         //One query/rule/filter for matching Tweets. Refer to https://t.co/rulelength to identify the max query length         query: "(from:TwitterDev) new -is:retweet",       });     console.dir(recentSearch, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const recentSearch =       await twitterClient.tweets.tweetsRecentSearch({         //One query/rule/filter for matching Tweets. Refer to https://t.co/rulelength to identify the max query length         query: "(from:TwitterDev) new -is:retweet",          //YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp from which the Tweets will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).         start_time: "2020-01-01T00:00:00Z",          //YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Tweets will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).         end_time: "2021-01-01T11:59:59Z",          //A comma separated list of fields to expand.         expansions: ["author_id"],          //A comma separated list of User fields to display.         "tweet.fields": ["created_at", "lang", "conversation_id"],          //A comma separated list of User fields to display.         "user.fields": ["created_at", "entities"],          //The maximum number of results         max_results: 10,       });     console.dir(recentSearch, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// String | One query/rule/filter for matching Tweets. Refer to https://t.co/rulelength to identify the max query length String query = "(from:TwitterDev) new -is:retweet";  try {     TweetSearchResponse result = apiInstance.tweets().tweetsRecentSearch(query, null, null, null, null, null, null, null, null, null, null, null, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling TweetsApi#tweetsRecentSearch");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

      `// Set the params values // For full list of params visit - https://github.com/twitterdev/twitter-api-java-sdk/blob/main/docs/TweetsApi.md#tweetsRecentSearch  // String | One query/rule/filter for matching Tweets. Refer to https://t.co/rulelength to identify the max query length String query = "(from:TwitterDev) new -is:retweet";  // Integer | The maximum number of results Integer maxResults = 10;  // Set<String> | A comma separated list of fields to expand. Set<String> expansions = new HashSet<>(Arrays.asList("author_id"));  // Set<String> | A comma separated list of Tweet fields to display. Set<String> tweetFields = new HashSet<>(Arrays.asList("created_at","lang","conversation_id"));  // Set<String> | A comma separated list of User fields to display. Set<String> userFields = new HashSet<>(Arrays.asList("created_at","entities"));  // OffsetDateTime | YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp from which the Tweets will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute). OffsetDateTime startTime = OffsetDateTime.parse("2020-01-01T00:00:00Z");  // OffsetDateTime | YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Tweets will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute). OffsetDateTime endTime = OffsetDateTime.parse("2021-01-01T11:59:59Z");   try {     TweetSearchResponse result = apiInstance.tweets().tweetsRecentSearch(query, startTime, endTime, null, null, maxResults, null, null, null, expansions, tweetFields, userFields, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling TweetsApi#tweetsRecentSearch");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`