platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/hide-replies/api-reference/put-tweets-id-hidden


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript - hide reply](#tab0)
* [TypeScript - unhide reply](#tab1)
* [Java - hide reply](#tab2)
* [Java - unhide reply](#tab3)

TypeScript - hide reply

TypeScript - unhide reply

Java - hide reply

Java - unhide reply

      `(async () => {   try {     const hideReply = await twitterClient.tweets.hideReplyById(       // The ID of the reply that you want to hide or unhide.       "1228393702244134912",       {         hidden: true,       }     );     console.dir(hideReply, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const unhideReply = await twitterClient.tweets.hideReplyById(       // The ID of the reply that you want to hide or unhide.       "1228393702244134912",       {         hidden: false,       }     );     console.dir(unhideReply, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `HideReplyByIdRequest hideReplyByIdRequest = new HideReplyByIdRequest(); // HideReplyByIdRequest |  hideReplyByIdRequest.hidden(true)  // String | The ID of the reply that you want to hide or unhide. String id = "1228393702244134912";  try {     HideReplyByIdResponse result = apiInstance.tweets().hideReplyById(hideReplyByIdRequest, id);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling TweetsApi#hideReplyById");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

      `HideReplyByIdRequest hideReplyByIdRequest = new HideReplyByIdRequest();  hideReplyByIdRequest.hidden(false)  // String | The ID of the reply that you want to hide or unhide. String id = "1228393702244134912";  try {     HideReplyByIdResponse result = apiInstance.tweets().hideReplyById(hideReplyByIdRequest, id);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling TweetsApi#hideReplyById");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`