platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/get-tweets-search-stream


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const searchFilteredStream = await twitterClient.tweets.searchStream();     console.dir(searchFilteredStream, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const searchFilteredStream = await twitterClient.tweets.searchStream({       //A comma separated list of fields to expand.       expansions: ["author_id"],        //A comma separated list of Tweet fields to display.       "tweet.fields": ["created_at", "conversation_id"],        //The number of minutes of backfill requested       backfill_minutes: 5,     });     console.dir(searchFilteredStream, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `try {     InputStream result = apiInstance.tweets().searchStream(null, null, null, null, null, null, null);     try {         JSON json = new JSON();         Type localVarReturnType = new TypeToken<StreamingTweet>(){}.getType();         BufferedReader reader = new BufferedReader(new InputStreamReader(result));         String line = reader.readLine();         while (line != null) {           System.out.println(json.getGson().fromJson(line, localVarReturnType).toString());           line = reader.readLine();         }     }catch (Exception e) {       e.printStackTrace();       System.out.println(e);     } } catch (ApiException e) {   System.err.println("Exception when calling TweetsApi#searchStream");   System.err.println("Status code: " + e.getCode());   System.err.println("Reason: " + e.getResponseBody());   System.err.println("Response headers: " + e.getResponseHeaders());   e.printStackTrace(); }`
    

      `// Set the (optional) params values  // Set<String> | A comma separated list of fields to expand. Set<String> expansions = new HashSet<>(Arrays.asList(["author_id"]));  // Set<String> | A comma separated list of Tweet fields to display. Set<String> tweetFields = new HashSet<>(Arrays.asList(["created_at", "conversation_id"]));  // Integer | The number of minutes of backfill requested Integer backfillMinutes = 5;  try {     InputStream result = apiInstance.tweets().searchStream(null, null, null, null, null, null, null);     try {         JSON json = new JSON();         Type localVarReturnType = new TypeToken<StreamingTweet>(){}.getType();         BufferedReader reader = new BufferedReader(new InputStreamReader(result));         String line = reader.readLine();         while (line != null) {           System.out.println(json.getGson().fromJson(line, localVarReturnType).toString());           line = reader.readLine();         }     }catch (Exception e) {       e.printStackTrace();       System.out.println(e);     } } catch (ApiException e) {   System.err.println("Exception when calling TweetsApi#searchStream");   System.err.println("Status code: " + e.getCode());   System.err.println("Reason: " + e.getResponseBody());   System.err.println("Response headers: " + e.getResponseHeaders());   e.printStackTrace(); }`