platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/bookmarks/api-reference/delete-users-id-bookmarks-tweet_id


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const removeBookmark =       await twitterClient.bookmarks.usersIdBookmarksDelete(         //The ID of the user whose bookmark is to be removed.         "2244994945",          //The ID of the tweet that the user is removing from bookmarks         "1228393702244134912"       );     console.dir(removeBookmark, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// String | The ID of the user whose bookmark is to be removed. String id = "2244994945";  // String | The ID of the tweet that the user is removing from bookmarks String tweetId = "1228393702244134912";  try {       BookmarkMutationResponse result = apiInstance.bookmarks().usersIdBookmarksDelete(id, tweetId);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling BookmarksApi#usersIdBookmarksDelete");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace();   }`