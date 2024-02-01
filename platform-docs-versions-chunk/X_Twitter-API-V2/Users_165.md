platform: X
topic: Twitter-API-V2
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/users/mutes/api-reference/post-users-user_id-muting


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const muteUser = await twitterClient.users.usersIdMute(       //The ID of the user that is requesting to mute the target user       "6253282",       {         //The ID of the user that the source user is requesting to mute         target_user_id: "2244994945",       }     );     console.dir(muteUser, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  UsersIdMuteRequest usersIdMuteRequest = new UsersIdMuteRequest();  //The ID of the user that the source user is requesting to mute usersIdMuteRequest.targetUserId("2244994945");  // String | The ID of the user that is requesting to mute the target user String id = "6253282";  try {     UsersMutingMutationResponse result = apiInstance.users().usersIdMute(usersIdMuteRequest, id);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsersApi#usersIdMute");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`