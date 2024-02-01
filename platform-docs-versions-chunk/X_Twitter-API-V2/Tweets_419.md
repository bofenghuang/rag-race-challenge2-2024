platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/likes/api-reference/get-tweets-id-liking_users


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const likingUsers = await twitterClient.users.tweetsIdLikingUsers(       // Tweet ID of the Tweet to request liking users of       "1354143047324299264"     );     console.dir(likingUsers, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const likingUsers = await twitterClient.users.tweetsIdLikingUsers(       // Tweet ID of the Tweet to request liking users of       "1354143047324299264",       {         // The maximum number of results         max_results: 5,          // A comma separated list of fields to expand.         expansions: ["pinned_tweet_id"],          // A comma separated list of Tweet fields to display.         "tweet.fields": ["created_at"],          // A comma separated list of User fields to display.         "user.fields": ["created_at"],       }     );     console.dir(likingUsers, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String | The ID of the Tweet for which to return results String id = "1354143047324299264";  try {     GenericMultipleUsersLookupResponse result = apiInstance.users().tweetsIdLikingUsers(id, null, null, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsersApi#tweetsIdLikingUsers");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

      `// Set the params values // For full list of params visit - https://github.com/twitterdev/twitter-api-java-sdk/blob/main/docs/UsersApi.md#tweetsIdLikingUsers  // String | The ID of the Tweet for which to return results String id = "1354143047324299264";  // Integer | The maximum number of results Integer maxResults = 5;  // Set<String> | A comma separated list of fields to expand. Set<String> expansions = new HashSet<>(Arrays.asList("pinned_tweet_id"));  // Set<String> | A comma separated list of Tweet fields to display. Set<String> tweetFields = new HashSet<>(Arrays.asList("created_at"));   // Set<String> | A comma separated list of User fields to display. Set<String> userFields = new HashSet<>(Arrays.asList("created_at"));  try {     GenericMultipleUsersLookupResponse result = apiInstance.users().tweetsIdLikingUsers(id, maxResults, null, userFields, expansions, tweetFields);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsersApi#tweetsIdLikingUsers");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`