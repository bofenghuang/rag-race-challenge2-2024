platform: X
topic: Twitter-API-V2
subtopic: Lists
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Lists.md
url: https://developer.twitter.com/en/docs/twitter-api/lists/manage-lists/api-reference/delete-lists-id

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const deleteList = await twitterClient.lists.listIdDelete(       //The ID of the List to delete       1441162269824405510,     );     console.dir(deleteList, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  //The ID of the List to delete String id = "1441162269824405510";   try {     ListDeleteResponse result = apiInstance.lists().listIdDelete(id);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling ListsApi#listIdDelete");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`