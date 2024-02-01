platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/api-reference/get-users-id-tweets


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const usersTweets = await twitterClient.tweets.usersIdTweets(        //The ID of the User to list Tweets of       2244994945     );     console.dir(usersTweets, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const usersTweets = await twitterClient.tweets.usersIdTweets(       //The ID of the User to list Tweets of       2244994945,       {         //A comma separated list of fields to expand         expansions: ["author_id"],          //A comma separated list of Tweet fields to display         "tweet.fields": [           "created_at",           "author_id",           "conversation_id",           "public_metrics",           "context_annotations",         ],          //A comma separated list of User fields to display         "user.fields": ["username"],          //The maximum number of results         max_results: 5,       }     );     console.dir(usersTweets, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// String | The ID of the User to list Tweets of String id = "2244994945";  try {     GenericTweetsTimelineResponse result = apiInstance.tweets().usersIdTweets(id, null, null, null, null, null, null, null, null, null, null, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling TweetsApi#usersIdTweets");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

      `// Set the params values // For full list of params visit - https://github.com/twitterdev/twitter-api-java-sdk/blob/main/docs/TweetsApi.md#usersIdTweets  // String | The ID of the User to list Tweets of String id = "2244994945";  // Integer | The maximum number of results Integer maxResults = 5;  // Set<String> | A comma separated list of fields to expand Set<String> expansions = new HashSet<>(Arrays.asList("author_id"));  // Set<String> | A comma separated list of Tweet fields to display Set<String> tweetFields = new HashSet<>(Arrays.asList("created_at","author_id","conversation_id","public_metrics","context_annotations"));  // Set<String> | A comma separated list of User fields to display Set<String> userFields = new HashSet<>(Arrays.asList("username"));  try {     GenericTweetsTimelineResponse result = apiInstance.tweets().usersIdTweets(id, null, null, maxResults, null, null, null, null, expansions, tweetFields, userFields, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling TweetsApi#usersIdTweets");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`