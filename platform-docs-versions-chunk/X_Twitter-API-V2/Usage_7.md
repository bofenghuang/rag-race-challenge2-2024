platform: X
topic: Twitter-API-V2
subtopic: Usage
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Usage.md
url: https://developer.twitter.com/en/docs/twitter-api/usage/tweets/api-reference/get-usage-tweets

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const getUsage =       await twitterClient.usage.getUsage();     console.dir(getUsage, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `try {     UsageResponse result = apiInstance.usage().getUsage();     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsageApi#getUsage");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`