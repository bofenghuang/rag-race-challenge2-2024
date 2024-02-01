platform: X
topic: Twitter-API-V2
subtopic: Lists
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Lists.md
url: https://developer.twitter.com/en/docs/twitter-api/lists/list-lookup/api-reference/get-users-id-owned_lists


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const getListBtId = await twitterClient.lists.listUserOwnedLists(       //The ID of the user for whom to return results       2244994945     );     console.dir(getListBtId, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const getListBtId = await twitterClient.lists.listUserOwnedLists(       //The ID of the user for whom to return results       2244994945,       {         //A comma separated list of fields to expand         expansions: ["owner_id"],          //A comma separated list of List fields to display         "list.fields": ["follower_count"],          //A comma separated list of User fields to display         "user.fields": ["created_at"],       }     );     console.dir(getListBtId, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String | The ID of the user for whom to return results String id = "2244994945";  try {     MultiListResponse result = apiInstance.lists().listUserOwnedLists(id, null, null, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling ListsApi#listUserOwnedLists");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

      `// Set the params values // For full list of params visit - https://github.com/twitterdev/twitter-api-java-sdk/blob/main/docs/ListsApi.md#listUserOwnedLists  // String | The ID of the user for whom to return results String id = "2244994945";  // Set<String> | A comma separated list of List fields to display Set<String> listFields = new HashSet<>(Arrays.asList("follower_count"));  // Set<String> | A comma separated list of fields to expand Set<String> expansions = new HashSet<>(Arrays.asList("owner_id"));  // Set<String> | A comma separated list of User fields to display Set<String> userFields = new HashSet<>(Arrays.asList("created_at"));  try {     MultiListResponse result = apiInstance.lists().listUserOwnedLists(id, null, null, listFields, expansions, userFields);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling ListsApi#listUserOwnedLists");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`