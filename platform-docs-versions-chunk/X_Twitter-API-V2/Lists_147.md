platform: X
topic: Twitter-API-V2
subtopic: Lists
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Lists.md
url: https://developer.twitter.com/en/docs/twitter-api/lists/list-members/api-reference/get-lists-id-members


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const getMembers = await twitterClient.users.listGetMembers(       //The ID of the List for which to return members       84839422     );     console.dir(getMembers, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const getMembers = await twitterClient.users.listGetMembers(       //The ID of the List for which to return members       84839422,       {         //A comma separated list of fields to expand         expansions: ["pinned_tweet_id"],          //The maximum number of results         max_results: 5,          //A comma separated list of User fields to display         "user.fields": ["username"],       }     );     console.dir(getMembers, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String | The ID of the List for which to return members String id = "84839422";  try {     ListLookupMultipleUsersLookupResponse result = apiInstance.users().listGetMembers(id, null, null, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsersApi#listGetMembers");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

      `// Set the params values // For full list of params visit - https://github.com/twitterdev/twitter-api-java-sdk/blob/main/docs/UsersApi.md#listGetMembers  // String | The ID of the List for which to return members String id = "84839422";  // Integer | The maximum number of results Integer maxResults = 5;  // Set<String> | A comma separated list of fields to expand Set<String> expansions = new HashSet<>(Arrays.asList("pinned_tweet_id"));  // Set<String> | A comma separated list of User fields to display Set<String> userFields = new HashSet<>(Arrays.asList("username"));  try {     ListLookupMultipleUsersLookupResponse result = apiInstance.users().listGetMembers(id, maxResults, null, expansions, null, userFields);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsersApi#listGetMembers");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`