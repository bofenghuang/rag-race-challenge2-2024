platform: X
topic: Twitter-API-V2
subtopic: Lists
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Lists.md
url: https://developer.twitter.com/en/docs/twitter-api/lists/list-tweets/api-reference/get-lists-id-tweets


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const getListTweets = await twitterClient.tweets.listsIdTweets(       //The ID of the List to list Tweets of       84839422     );     console.dir(getListTweets, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const getListTweets = await twitterClient.tweets.listsIdTweets(       //The ID of the List to list Tweets of       84839422,       {         //A comma separated list of fields to expand         expansions: ["author_id"],          //A comma separated list of User fields to display         "user.fields": ["verified"],       }     );     console.dir(getListTweets, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String | The ID of the List to list Tweets of String id = "84839422";  try {     ListsIdTweetsResponse result = apiInstance.tweets().listsIdTweets(id, null, null, null, null, null, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling TweetsApi#listsIdTweets");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

      `// Set the params values // For full list of params visit - https://github.com/twitterdev/twitter-api-java-sdk/blob/main/docs/TweetsApi.md#listsIdTweets  // String | The ID of the List to list Tweets of String id = "84839422";  // Set<String> | A comma separated list of fields to expand Set<String> expansions = new HashSet<>(Arrays.asList("author_id"));  // Set<String> | A comma separated list of User fields to display Set<String> userFields = new HashSet<>(Arrays.asList("verified"));  try {     ListsIdTweetsResponse result = apiInstance.tweets().listsIdTweets(id, null, null, expansions, null, userFields, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling TweetsApi#listsIdTweets");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`