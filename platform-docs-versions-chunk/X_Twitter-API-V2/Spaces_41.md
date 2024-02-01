platform: X
topic: Twitter-API-V2
subtopic: Spaces
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Spaces.md
url: https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/api-reference/get-spaces-id-buyers


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const getSpaceBuyers = await twitterClient.spaces.spaceBuyers(       //The space id from which buyers of the space will be retrieved       "1DXxyRYNejbKM"     );     console.dir(getSpaceBuyers, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const getSpaceBuyers = await twitterClient.spaces.spaceBuyers(       //The space id from which buyers of the space will be retrieved       "1DXxyRYNejbKM",       {         //A comma separated list of fields to expand         expansions: ["pinned_tweet_id"],          //A comma separated list of User fields to display         "user.fields": ["created_at"],          //A comma separated list of Tweet fields to display         "tweet.fields": ["created_at"],       }     );     console.dir(getSpaceBuyers, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String | The space id from which tweets will be retrieved String id = "1YqKDqWqdPLsV";  try {     MultiUserLookupResponse result = apiInstance.spaces().spaceBuyers(id, null, null, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling SpacesApi#spaceBuyers");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

      `// Set the params values // For full list of params visit - https://github.com/twitterdev/twitter-api-java-sdk/blob/main/docs/SpacesApi.md#spaceBuyers  // String | The space id from which tweets will be retrieved String id = "1YqKDqWqdPLsV";  // Set<String> | A comma separated list of fields to expand. Set<String> expansions = new HashSet<>(Arrays.asList("pinned_tweet_id"));  // Set<String> | A comma separated list of User fields to display. Set<String> userFields = new HashSet<>(Arrays.asList("created_at"));  // Set<String> | A comma separated list of Tweet fields to display. Set<String> tweetFields = new HashSet<>(Arrays.asList("created_at"));  try {     MultiUserLookupResponse result = apiInstance.spaces().spaceBuyers(id, null, null, userFields, expansions, tweetFields);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling SpacesApi#spaceBuyers");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`