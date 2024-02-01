platform: X
topic: Twitter-API-V2
subtopic: Lists
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Lists.md
url: https://developer.twitter.com/en/docs/twitter-api/lists/list-members/api-reference/post-lists-id-members


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const addMember = await twitterClient.lists.listAddMember(       //The ID of the user to be added as a member of the List       2244994945,        //The ID of the List to add a member       1441162269824405510     );     console.dir(addMember, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String | The ID of the user to be added as a member of the List String usersId = "2244994945" ListAddMemberRequest listAddMemberRequest = new ListAddMemberRequest(); listAddMemberRequest.userId(usersId);  // String | The ID of the List to add a member String id = "1441162269824405510";  try {     ListMemberResponse result = apiInstance.lists().listAddMember(listAddMemberRequest, id);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling ListsApi#listAddMember");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`