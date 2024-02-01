platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/api-reference/post-tweets


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (text with poll option)](#tab0)
* [Java (text with poll option)](#tab1)

TypeScript (text with poll option)

Java (text with poll option)

      `(async () => {   try {     const postTweet = await twitterClient.tweets.createTweet({       // The text of the Tweet       text: "Are you excited for the weekend?",        // Options for a Tweet with a poll       poll: {         options: ["Yes", "Maybe", "No"],         duration_minutes: 120,       },     });     console.dir(postTweet, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  CreateTweetRequest createTweetRequest = new CreateTweetRequest(); CreateTweetRequestPoll createTweetRequestPoll = new CreateTweetRequestPoll();  // The text of the Tweet createTweetRequest.text("Are you excited for the weekend?");  // Options for a Tweet with a poll List<String> pollOptions = Arrays.asList("Yes", "Maybe", "No"); createTweetRequestPoll.options(pollOptions);  // Duration of the poll in minutes createTweetRequestPoll.durationMinutes(120);  createTweetRequest.poll(createTweetRequestPoll);  try {     TweetCreateResponse result = apiInstance.tweets().createTweet(createTweetRequest);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling TweetsApi#createTweet");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`