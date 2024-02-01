platform: X
topic: Twitter-API-V2
subtopic: Lists
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Lists.md
url: https://developer.twitter.com/en/docs/twitter-api/lists/pinned-lists/api-reference/delete-users-id-pinned-lists-list_id


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const unpinList = await twitterClient.lists.listUserUnpin(       //The ID of the authenticated source user that will remove the pinned List       2244994945,        //The ID of the List to unpin       1441162269824405510     );     console.dir(unpinList, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String | The ID of the authenticated source user that will remove the pinned List String id = "2244994945";   // String | The ID of the List to unpin String listId = "1441162269824405510"; try {     ListPinnedResponse result = apiInstance.lists().listUserUnpin(id, listId);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling ListsApi#listUserUnpin");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`