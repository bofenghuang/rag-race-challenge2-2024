platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/api-reference/get-tweets


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const lookupTweetsById = await twitterClient.tweets.findTweetsById({       //A comma separated list of Tweet IDs. Up to 100 are allowed in a single request       ids: [         "1460323737035677698",         "1519781379172495360",         "1519781381693353984",       ],     });     console.dir(lookupTweetsById, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const lookupTweetsById = await twitterClient.tweets.findTweetsById({       //A comma separated list of Tweet IDs. Up to 100 are allowed in a single request.       ids: [         "1460323737035677698",         "1519781379172495360",         "1519781381693353984",       ],        //A comma separated list of fields to expand.       expansions: ["author_id"],        //A comma separated list of User fields to display.       "user.fields": ["created_at", "description", "name"],        //A comma separated list of Tweet fields to display.       "tweet.fields": ["created_at", "lang", "context_annotations"],     });     console.dir(lookupTweetsById, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// List<String> | A comma separated list of Tweet IDs. Up to 100 are allowed in a single request. List<String> ids = Arrays.asList("1460323737035677698","1519781379172495360", "1519781381693353984");  try {       MultiTweetLookupResponse result = apiInstance.tweets().findTweetsById(ids);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling TweetsApi#findTweetsById");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace();   }`
    

      `// Set the params values // For full list of params visit - https://github.com/twitterdev/twitter-api-java-sdk/blob/main/docs/TweetsApi.md#findTweetsById  // List<String> | A comma separated list of Tweet IDs. Up to 100 are allowed in a single request. List<String> ids = Arrays.asList("1460323737035677698","1519781379172495360", "1519781381693353984");  // Set<String> | A comma separated list of fields to expand. Set<String> expansions = new HashSet<>(Arrays.asList("author_id"));  // Set<String> | A comma separated list of Tweet fields to display. Set<String> tweetFields = new HashSet<>(Arrays.asList("created_at", "lang", "context_annotations"));  // Set<String> | A comma separated list of User fields to display. Set<String> userFields = new HashSet<>(Arrays.asList("created_at", "description", "name"));  try {       MultiTweetLookupResponse result = apiInstance.tweets().findTweetsById(ids, expansions, tweetFields, userFields, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling TweetsApi#findTweetsById");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace();   }`