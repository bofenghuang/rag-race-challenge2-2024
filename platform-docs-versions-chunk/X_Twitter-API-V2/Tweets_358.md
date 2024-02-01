platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/retweets/api-reference/post-users-id-retweets


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const createRetweet = await twitterClient.tweets.usersIdRetweets(       //The ID of the user that is requesting to retweet the tweet       "2244994945",       {         //The ID of the tweet the user is requesting to retweet         tweet_id: "1228393702244134912",       }     );     console.dir(createRetweet, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// String | The ID of the tweet the user is requesting to retweet String tweetId = "1228393702244134912" UsersRetweetsCreateRequest usersRetweetsCreateRequest = new UsersRetweetsCreateRequest(); usersRetweetsCreateRequest.tweetId(tweetId);  // String | The ID of the user that is requesting to retweet the tweet String id = "2244994945"; try {     UsersRetweetsCreateResponse result = apiInstance.tweets().usersIdRetweets(usersRetweetsCreateRequest, id);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling TweetsApi#usersIdRetweets");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`