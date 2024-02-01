platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/get-tweets-search-stream-rules


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const getStreamRules = await twitterClient.tweets.getRules();     console.dir(getStreamRules, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `//Set the (optional) params values  //List<String> | A comma-separated list of Rule IDs. List<String> ids = Arrays.asList();  //Integer | The maximum number of results Integer maxResults = 1000;  //String | This value is populated by passing the 'next_token' returned in a request to paginate through results. String paginationToken = "paginationToken_example";  try {     GetRulesResponse result = apiInstance.tweets().getRules(ids, maxResults, paginationToken);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling TweetsApi#getRules");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`