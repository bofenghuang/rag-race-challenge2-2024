platform: X
topic: Twitter-API-V2
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference/delete-users-source_id-following


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const unfollowUser = await twitterClient.users.usersIdUnfollow(       //The ID of the user that is requesting to unfollow the target user       "2244994945",        //The ID of the user that the source user is requesting to unfollow       "6253282"     );     console.dir(unfollowUser, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String | The ID of the user that is requesting to unfollow the target user String sourceUserId = "2244994945";  // String | The ID of the user that the source user is requesting to unfollow String targetUserId = "6253282";  try {     UsersFollowingDeleteResponse result = apiInstance.users().usersIdUnfollow(sourceUserId, targetUserId);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsersApi#usersIdUnfollow");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`