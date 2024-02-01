platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/counts/api-reference/get-tweets-counts-recent


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const getTweetCountsRecent =       await twitterClient.tweets.tweetCountsRecentSearch({         //One query/rule/filter for matching Tweets. Refer to https://t.co/rulelength to identify the max query length         query: "lakers",       });     console.dir(getTweetCountsRecent, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const getTweetCountsRecent =       await twitterClient.tweets.tweetCountsRecentSearch({         //One query/rule/filter for matching Tweets. Refer to https://t.co/rulelength to identify the max query length         query: "lakers",          //YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp (from most recent 7 days) from which the Tweets will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).         start_time: "2021-01-01T00:00:00.000Z",          //YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Tweets will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).         end_time: "2021-01-15T00:00:00.000Z",          //Granularity | The granularity for the search counts results.         granularity: "day",       });     console.dir(getTweetCountsRecent, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `//Set the params values  //String | One query/rule/filter for matching Tweets. Refer to https://t.co/rulelength to identify the max query length String query = "lakers";  try {     TweetCountsResponse result = apiInstance.tweets().tweetCountsRecentSearch(query, null, null, null, null, null, null, granularity);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling TweetsApi#tweetCountsRecentSearch");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

      `// Set the params values // For full list of params visit - https://github.com/twitterdev/twitter-api-java-sdk/blob/main/docs/TweetsApi.md#tweetCountsRecentSearch  //String | One query/rule/filter for matching Tweets. Refer to https://t.co/rulelength to identify the max query length String query = "lakers";  //OffsetDateTime | YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp (from most recent 7 days) from which the Tweets will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute). OffsetDateTime startTime = OffsetDateTime.parse("2021-01-01T00:00:00.000Z");  //OffsetDateTime | YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Tweets will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute). OffsetDateTime endTime = OffsetDateTime.parse("2021-01-15T00:00:00.000Z");  //Granularity | The granularity for the search counts results. Granularity granularity = Granularity.fromValue("day");  try {     TweetCountsResponse result = apiInstance.tweets().tweetCountsRecentSearch(query, startTime, endTime, null, null, null, null, granularity);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling TweetsApi#tweetCountsRecentSearch");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`