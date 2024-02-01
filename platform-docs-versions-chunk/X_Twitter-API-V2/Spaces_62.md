platform: X
topic: Twitter-API-V2
subtopic: Spaces
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Spaces.md
url: https://developer.twitter.com/en/docs/twitter-api/spaces/search/quick-start


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const spacesSearch = await twitterClient.spaces.searchSpaces({       //The search query       query: "hello",        // A comma separated list of Space fields to display.       "space.fields": ["title", "host_ids"],     });     console.dir(spacesSearch, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values // For full list of params visit - https://github.com/twitterdev/twitter-api-java-sdk/blob/main/docs/SpacesApi.md#searchSpaces  // String | The search query String query = "hello";  // Set<String> | A comma separated list of Space fields to display. Set<String> spaceFields = new HashSet<>(Arrays.asList("title", "host_ids"));  try {     MultiSpaceLookupResponse result = apiInstance.spaces().searchSpaces(query, null, null, spaceFields, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling SpacesApi#searchSpaces");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`