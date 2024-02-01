platform: X
topic: Twitter-API-V2
subtopic: Lists
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Lists.md
url: https://developer.twitter.com/en/docs/twitter-api/lists/list-members/api-reference/delete-lists-id-members-user_id


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const removeMember = await twitterClient.lists.listRemoveMember(       //The ID of the List to remove a member       1441162269824405510,        //The ID of user that will be removed from the List       2244994945     );     console.dir(removeMember, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String |The ID of the List to remove a member String id = "1441162269824405510";   // String | The ID of user that will be removed from the List String userId = "2244994945"; try {     ListMemberResponse result = apiInstance.lists().listRemoveMember(id, userId);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling ListsApi#listRemoveMember");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`