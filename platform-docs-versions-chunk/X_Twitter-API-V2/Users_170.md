platform: X
topic: Twitter-API-V2
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/users/mutes/api-reference/delete-users-user_id-muting


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const unmuteUser = await twitterClient.users.usersIdUnmute(       //The ID of the user that is requesting to unmute the target user       "2244994945",        //The ID of the user that the source user is requesting to unmute       "6253282"     );     console.dir(unmuteUser, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String | The ID of the user that is requesting to unmute the target user String sourceUserId = "2244994945";  // String | The ID of the user that the source user is requesting to unmute String targetUserId = "6253282";  try {     UsersMutingMutationResponse result = apiInstance.users().usersIdUnmute(sourceUserId, targetUserId);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsersApi#usersIdUnmute");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`