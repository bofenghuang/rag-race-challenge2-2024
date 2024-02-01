platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/bookmarks/api-reference/get-users-id-bookmarks


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const getUserBookmarks =       await twitterClient.bookmarks.getUsersIdBookmarks(         //User ID         "2244994945"       );     console.dir(getUserBookmarks, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const getUserBookmarks =       await twitterClient.bookmarks.getUsersIdBookmarks(         //User ID         "2244994945",         {           //The maximum number of results           max_results: 5,            //A comma separated list of fields to expand.           expansions: "attachments.media_keys",            //A comma separated list of Media fields to display.           "media.fields": ["type", "duration_ms"],         }       );     console.dir(getUserBookmarks, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `//User ID String id = "2244994945";  try {     GenericTweetsTimelineResponse result = apiInstance.bookmarks().getUsersIdBookmarks(id, null, null, null, null, null, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling BookmarksApi#getUsersIdBookmarks");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace();   }`
    

      `// Set the params values // For full list of params visit - https://github.com/twitterdev/twitter-api-java-sdk/blob/main/docs/BookmarksApi.md#getUsersIdBookmarks  //User ID String id = "2244994945";  // Integer | The maximum number of results Integer maxResults = 5;  // Set<String> | A comma separated list of fields to expand. Set<String> expansions = new HashSet<>(Arrays.asList("attachments.media_keys"));  // Set<String> | A comma separated list of Media fields to display. Set<String> mediaFields = new HashSet<>(Arrays.asList());  try {     GenericTweetsTimelineResponse result = apiInstance.bookmarks().getUsersIdBookmarks(id, maxResults, null, expansions, null, null, mediaFields, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling BookmarksApi#getUsersIdBookmarks");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace();   }`