platform: X
topic: Twitter-API-V2
subtopic: Spaces
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Spaces.md
url: https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/api-reference/get-spaces-by-creator-ids


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const getSpacesByCreatorId =       await twitterClient.spaces.findSpacesByCreatorIds({         //A list of user ids         user_ids: ["2244994945", "6253282"],       });     console.dir(getSpacesByCreatorId, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const getSpacesByCreatorId =       await twitterClient.spaces.findSpacesByCreatorIds({         //A list of user ids         user_ids: ["2244994945", "6253282"],          //A comma separated list of Space fields to display         "space.fields": ["host_ids"],       });     console.dir(getSpacesByCreatorId, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // List<String> | The users to search through List<String> userIds = Arrays.asList("2244994945", "6253282");  try {     MultiSpaceLookupResponse result = apiInstance.spaces().findSpacesByCreatorIds(userIds, null, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling SpacesApi#findSpacesByCreatorIds");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

      `// Set the params values // For full list of params visit - https://github.com/twitterdev/twitter-api-java-sdk/blob/main/docs/SpacesApi.md#findSpacesByCreatorIds  // List<String> | The users to search through List<String> userIds = Arrays.asList("2244994945", "6253282");  // Set<String> | A comma separated list of Space fields to display Set<String> expansions = new HashSet<>(Arrays.asList("host_ids"));  // Set<String> | A comma separated list of Tweet fields to display. Set<String> spaceFields = new HashSet<>(Arrays.asList("host_ids"));  try {     MultiSpaceLookupResponse result = apiInstance.spaces().findSpacesByCreatorIds(userIds, spaceFields, expansions, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling SpacesApi#findSpacesByCreatorIds");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`