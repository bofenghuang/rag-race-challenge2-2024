platform: X
topic: Twitter-API-V2
subtopic: Lists
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Lists.md
url: https://developer.twitter.com/en/docs/twitter-api/lists/pinned-lists/api-reference/post-users-id-pinned-lists


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const pinList = await twitterClient.lists.listUserPin(       //The ID of the authenticated source user that will pin the List       2244994945,              //The ID of the List to be pinned       1441162269824405510     );     console.dir(pinList, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String | The ID of the List to be pinned String listsId = "1441162269824405510"; ListPinRequest listPinRequest = new ListPinRequest(); listPinRequest.listId(listsId);  // String | The ID of the authenticated source user that will pin the List String id = "2244994945";   try {     ListPinnedResponse result = apiInstance.lists().listUserPin(listPinRequest, id);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling ListsApi#listUserPin");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`