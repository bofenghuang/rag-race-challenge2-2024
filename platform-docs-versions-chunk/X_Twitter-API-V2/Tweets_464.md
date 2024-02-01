platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/bookmarks/api-reference/post-users-id-bookmarks


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const postBookmark = await twitterClient.bookmarks.postUsersIdBookmarks(       //User ID       "2244994945",       {         tweet_id: "1228393702244134912",       }     );     console.dir(postBookmark, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// String | The ID of the user for whom to add bookmarks String id = "2244994945";  // String | The ID of the tweet that the user is adding to bookmarks String tweetId = "1228393702244134912";  AddBookmarkRequest addBookmarkRequest = new AddBookmarkRequest(); // AddBookmarkRequest |  addBookmarkRequest.tweetId(tweetId);  try {     BookmarkMutationResponse result = apiInstance.bookmarks().postUsersIdBookmarks(addBookmarkRequest, id);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling BookmarksApi#postUsersIdBookmarks");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace();   }`