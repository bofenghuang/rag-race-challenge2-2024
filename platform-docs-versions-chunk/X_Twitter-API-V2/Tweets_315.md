platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/volume-streams/api-reference/get-tweets-sample10-stream


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const sample10Stream = await twitterClient.tweets.sample10Stream();     console.dir(sampleStream10, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const sample10Stream = await twitterClient.tweets.sample10Stream({       //A comma separated list of fields to expand       expansions: ["author_id"],        //The number of minutes of backfill requested       backfill_minutes: 5,        //A comma separated list of Tweet fields to display.       "tweet.fields": ["created_at", "conversation_id"],     });     console.dir(sample10Stream, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `try {     InputStream result = apiInstance.tweets().sample10Stream(null, null, null, null, null, null, null);     try{         JSON json = new JSON();         Type localVarReturnType = new TypeToken<StreamingTweet>(){}.getType();         BufferedReader reader = new BufferedReader(new InputStreamReader(result));         String line = reader.readLine();         while (line != null) {           System.out.println(json.getGson().fromJson(line, localVarReturnType).toString());           line = reader.readLine();         }     } catch (Exception e) {       e.printStackTrace();       System.out.println(e);     } } catch (ApiException e) {     System.err.println("Exception when calling TweetsApi#sampleStream");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

      `// Set the params values // For full list of params visit - https://github.com/twitterdev/twitter-api-java-sdk/blob/main/docs/TweetsApi.md#sample10Stream  // Set<String> | A comma separated list of fields to expand Set<String> expansions = new HashSet<>(Arrays.asList("author_id"));  // Set<String> | A comma separated list of Tweet fields to display Set<String> tweetFields = new HashSet<>(Arrays.asList("created_at", "conversation_id"));  // Integer | The number of minutes of backfill requested Integer backfillMinutes = 5;  try {     InputStream result = apiInstance.tweets().sample10Stream(expansions, tweetFields, null, null, null, null, backfillMinutes);     try{         JSON json = new JSON();         Type localVarReturnType = new TypeToken<StreamingTweet>(){}.getType();         BufferedReader reader = new BufferedReader(new InputStreamReader(result));         String line = reader.readLine();         while (line != null) {           System.out.println(json.getGson().fromJson(line, localVarReturnType).toString());           line = reader.readLine();         }     } catch (Exception e) {       e.printStackTrace();       System.out.println(e);     } } catch (ApiException e) {     System.err.println("Exception when calling TweetsApi#sample10Stream");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`