platform: X
topic: Twitter-API-V2
subtopic: Spaces
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Spaces.md
url: https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/api-reference/get-spaces


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const searchSpacesByIds = await twitterClient.spaces.findSpacesByIds({       //A list of space ids       ids: ["1DXxyRYNejbKM", "1nAJELYEEPvGL"],     });     console.dir(searchSpacesByIds, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const searchSpacesByIds = await twitterClient.spaces.findSpacesByIds({       //A list of space ids       ids: ["1DXxyRYNejbKM", "1nAJELYEEPvGL"],        //A comma separated list of Space fields to display.       "space.fields": ["host_ids"],     });     console.dir(searchSpacesByIds, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // List<String> | A list of space ids List<String> ids = Arrays.asList("1DXxyRYNejbKM", "1nAJELYEEPvGL");  try {     MultiSpaceLookupResponse result = apiInstance.spaces().findSpacesByIds(ids, null, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling SpacesApi#findSpacesByIds");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

      `// Set the params values // For full list of params visit - https://github.com/twitterdev/twitter-api-java-sdk/blob/main/docs/SpacesApi.md#findSpacesByIds  // String | The search query String query = "hello";  // Set<String> | A comma separated list of Space fields to display. Set<String> spaceFields = new HashSet<>(Arrays.asList("title", "host_ids"));  try {     MultiSpaceLookupResponse result = apiInstance.spaces().findSpacesByIds(ids, spaceFields, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling SpacesApi#findSpacesByIds");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`