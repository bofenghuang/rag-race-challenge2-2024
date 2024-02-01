platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/likes/api-reference/post-users-id-likes


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const likeTweet = await twitterClient.tweets.usersIdLike(       // The ID of the user that is requesting to like the tweet       "1324848235714736129",        {         // The ID of the tweet that the user is requesting to like         tweet_id: "1521887626935947265",       }     );     console.dir(likeTweet, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  UsersLikesCreateRequest usersLikesCreateRequest = new UsersLikesCreateRequest();  // String | The ID of the user that is requesting to like the tweet usersLikesCreateRequest.tweetId("1228393702244134912");  // String | The ID of the user that is requesting to like the tweet String id = "2244994945";  try {     UsersLikesCreateResponse result = apiInstance.tweets().usersIdLike(usersLikesCreateRequest, id);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling TweetsApi#usersIdLike");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`