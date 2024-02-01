platform: X
topic: Twitter-API-V2
subtopic: Lists
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Lists.md
url: https://developer.twitter.com/en/docs/twitter-api/lists/manage-lists/api-reference/put-lists-id


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const updateList = await twitterClient.lists.listIdUpdate(       //The ID of the List to modify       1441163524802158595,       {         name: "test v2 create list",         description: "example code",         private: false,       }     );     console.dir(updateList, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  ListUpdateRequest listUpdateRequest = new ListUpdateRequest(); listUpdateRequest.name("test v2 update list"); listUpdateRequest.description("example update"); listUpdateRequest.private(false);  // String | The ID of the List to modify String id = "1441163524802158595";  try {     ListUpdateResponse result = apiInstance.lists().listIdUpdate(listUpdateRequest, id);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling ListsApi#listIdUpdate");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`