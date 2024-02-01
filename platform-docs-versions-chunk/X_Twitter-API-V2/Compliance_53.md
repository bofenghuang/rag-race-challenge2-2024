platform: X
topic: Twitter-API-V2
subtopic: Compliance
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Compliance.md
url: https://developer.twitter.com/en/docs/twitter-api/compliance/streams/api-reference/get-tweets-compliance-stream


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const tweetComplianceStream = await twitterClient.tweets.complianceStream();     console.dir(tweetComplianceStream, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `try {     InputStream result = apiInstance.tweets().complianceStream(null, null, null, null, null, null, null);     try{         JSON json = new JSON();         Type localVarReturnType = new TypeToken<StreamingTweetCompliance>(){}.getType();         BufferedReader reader = new BufferedReader(new InputStreamReader(result));         String line = reader.readLine();         while (line != null) {           System.out.println(json.getGson().fromJson(line, localVarReturnType).toString());           line = reader.readLine();         }     } catch (Exception e) {       e.printStackTrace();       System.out.println(e);     } } catch (ApiException e) {     System.err.println("Exception when calling TweetsApi#tweetsComplianceStream");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`