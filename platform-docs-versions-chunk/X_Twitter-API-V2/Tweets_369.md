platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/retweets/api-reference/get-tweets-id-retweets


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [Java (Default fields)](#tab1)

TypeScript (Default fields)

Java (Default fields)

      `(async () => {   try {     const lookupretweetsById = await twitterClient.tweets.findRetweetById(       //The ID of the Tweet       "1460323737035677698"     );     console.dir(lookupretweetsById, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `//The ID of the Tweet   String id = "1460323737035677698"  try {       RetweetLookupResponse result = apiInstance.tweets().findRetweetById(ids);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling TweetsApi#findRetweetById");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace();   }    }`