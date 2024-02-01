platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/api-reference/delete-tweets-id


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   // The ID of the Tweet to be deleted.   const tweetId = "1445880548472328192"   try {               const deleteTweet = await twitterClient.tweets.deleteTweetById();     console.dir(deleteTweet, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String | The ID of the Tweet to be deleted. String id = "1445880548472328192";  try {     TweetDeleteResponse result = apiInstance.tweets().deleteTweetById(id);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling TweetsApi#deleteTweetById");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`