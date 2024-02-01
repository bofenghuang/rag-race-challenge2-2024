platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/retweets/api-reference/delete-users-id-retweets-tweet_id


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const deleteRetweet = await twitterClient.tweets.usersIdUnretweets(       //The ID of the user that is requesting to unretweet the tweet       "2244994945",        //The ID of the tweet that the user is requesting to unretweet       "1228393702244134912"     );     console.dir(deleteRetweet, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// String | The ID of the user that is requesting to unretweet the tweet String id = "2244994945";  // String | The ID of the tweet that the user is requesting to unretweet String sourceTweetId = "1228393702244134912";  try {       UsersRetweetsDeleteResponse result = apiInstance.tweets().usersIdUnretweets(id, sourceTweetId);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling TweetsApi#usersIdUnretweets");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace();   }`