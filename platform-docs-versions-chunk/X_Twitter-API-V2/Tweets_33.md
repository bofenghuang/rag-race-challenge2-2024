platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/api-reference/get-tweets-id


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const lookupTweetById = await twitterClient.tweets.findTweetById(       //The ID of the Tweet       "1460323737035677698"     );     console.dir(lookupTweetById, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const lookupTweetById = await twitterClient.tweets.findTweetById(       //The ID of the Tweet       "1460323737035677698",       {         //A comma separated list of fields to expand         expansions: ["attachments.media_keys"],          //A comma separated list of Media fields to display         "media.fields": ["duration_ms", "type"],       }     );     console.dir(lookupTweetById, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `//The ID of the Tweet   String id = "1460323737035677698"  try {       SingleTweetLookupResponse result = apiInstance.tweets().findTweetById(ids);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling TweetsApi#findTweetById");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace();   }    }`
    

      `// Set the params values // For full list of params visit - https://github.com/twitterdev/twitter-api-java-sdk/blob/main/docs/TweetsApi.md#findTweetById  //The ID of the Tweet   String id = "1460323737035677698"  // Set<String> | A comma separated list of fields to expand. Set<String> expansions = new HashSet<>(Arrays.asList("attachments.media_keys"));  // Set<String> | A comma separated list of Media fields to display. Set<String> mediaFields = new HashSet<>(Arrays.asList("type", "duration_ms"));  try {       SingleTweetLookupResponse result = apiInstance.tweets().findTweetById(ids, expansions, null, null, mediaFields, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling TweetsApi#findTweetById");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace();   }`