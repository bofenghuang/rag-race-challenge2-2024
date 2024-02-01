platform: X
topic: Twitter-API-V2
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference/post-users-source_user_id-following


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const followUser = await twitterClient.users.usersIdFollow(       //The ID of the user that is requesting to follow the target user       "6253282",       {         //The ID of the user that the source user is requesting to follow         target_user_id: "2244994945",       }     );     console.dir(followUser, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  UsersIdFollowRequest usersIdFollowRequest = new UsersIdFollowRequest();  //The ID of the user that the source user is requesting to follow usersIdFollowRequest.targetUserId("2244994945");  // String | The ID of the user that is requesting to follow the target user String id = "6253282";  try {     UsersFollowingCreateResponse result = apiInstance.users().usersIdFollow(usersIdFollowRequest, id);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsersApi#usersIdFollow");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`