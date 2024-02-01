platform: X
topic: Twitter-API-V2
subtopic: Spaces
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Spaces.md
url: https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/api-reference/get-spaces-id


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const searchSpacesById = await twitterClient.spaces.findSpaceById(       //The space id to be retrieved       "1DXxyRYNejbKM"     );     console.dir(searchSpacesById, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const searchSpacesByIds = await twitterClient.spaces.findSpaceById(       //The space id to be retrieved       "1DXxyRYNejbKM",        //A comma separated list of Space fields to display.       { "space.fields": ["host_ids"] }     );     console.dir(searchSpacesByIds, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String | The space id to be retrieved String id = "1DXxyRYNejbKM";  try {     SingleSpaceLookupResponse result = apiInstance.spaces().findSpaceById(id, null, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling SpacesApi#findSpaceById");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

      `// Set the params values // For full list of params visit - https://github.com/twitterdev/twitter-api-java-sdk/blob/main/docs/SpacesApi.md#findSpaceById  // String | The space id to be retrieved String id = "1DXxyRYNejbKM";  // Set<String> | A comma separated list of Space fields to display. Set<String> spaceFields = new HashSet<>(Arrays.asList("host_ids"));  try {     SingleSpaceLookupResponse result = apiInstance.spaces().findSpaceById(id, spaceFields, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling SpacesApi#findSpaceById");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`