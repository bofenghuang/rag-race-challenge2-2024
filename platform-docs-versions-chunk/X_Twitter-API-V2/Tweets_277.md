platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/post-tweets-search-stream-rules


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const addOrDelete = await twitterClient.tweets.addOrDeleteRules(       {         add: [           {             //The value of the rule text             value: "cat has:media",             //A tag meant for the labeling of user provided rules.             tag: "cats with media",           },           {             value: "cat has:media -grumpy",             tag: "happy cats with media",           },         ],          //To delete rules comment out the add section and uncomment out the delete code         /*         delete: {           //IDs of all deleted user-specified stream filtering rules.           ids: ["1165037377523306498", "1165037377523306499"],         },         */       },       //Optional - Dry Run can be used with both the add and delete action, with the expected result given, but without actually taking any action in the system (meaning the end state will always be as it was when the request was submitted). This is particularly useful to validate rule changes.       { dry_run: true }     );     console.dir(addOrDelete, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  AddOrDeleteRulesRequest addOrDeleteRulesRequest = new AddOrDeleteRulesRequest();   //To delete rule, uncomment out the block of code below /* List<String> ids = Arrays.asList("1165037377523306498","1165037377523306499"); // List<String> | IDs of all deleted user-specified stream filtering rules. DeleteRulesRequest deleteRulesRequest = new DeleteRulesRequest(); DeleteRulesRequestDelete deleteRules = new DeleteRulesRequestDelete();  deleteRules.ids(ids); deleteRulesRequest.delete(deleteRules);  addOrDeleteRulesRequest.setActualInstance(deleteRulesRequest); */  // AddRulesRequest addRuleRequest = new AddRulesRequest(); RuleNoId newRule = new RuleNoId();  newRule.value("cat has:media"); newRule.tag("cats with media");  addRuleRequest.addAddItem(newRule); addOrDeleteRulesRequest.setActualInstance(addRuleRequest);  // Boolean | Dry Run can be used with both the add and delete action, with the expected result given, but without actually taking any action in the system (meaning the end state will always be as it was when the request was submitted). This is particularly useful to validate rule changes. Boolean dryRun = true;  try {     AddOrDeleteRulesResponse result = apiInstance.tweets().addOrDeleteRules(addOrDeleteRulesRequest, dryRun);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling TweetsApi#addOrDeleteRules");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`