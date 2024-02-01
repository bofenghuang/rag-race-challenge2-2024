platform: X
topic: Twitter-API-V2
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-by


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript (Default fields)](#tab0)
* [TypeScript (Optional fields)](#tab1)
* [Java (Default fields)](#tab2)
* [Java (Optional fields)](#tab3)

TypeScript (Default fields)

TypeScript (Optional fields)

Java (Default fields)

Java (Optional fields)

      `(async () => {   try {     const usernamesLookup = await twitterClient.users.findUsersByUsername({       //A list of usernames, comma-separated. You can specify up to 100 usernames.       usernames: ["TwitterDev", "Twitter"]     });     console.dir(usernamesLookup, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `(async () => {   try {     const usernamesLookup = await twitterClient.users.findUsersByUsername({       //A list of usernames, comma-separated. You can specify up to 100 usernames.       usernames: ["TwitterDev", "Twitter"],        //A comma separated list of User fields to display       "user.fields": ["created_at"],        //A comma separated list of Tweet fields to display.       "tweet.fields": ["created_at"],        //A comma separated list of fields to expand       expansions: ["pinned_tweet_id"],     });     console.dir(usernamesLookup, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // List<String> | Required . A list of usernames, comma-separated. You can specify up to 100 usernames. List<String> usernames = Arrays.asList("TwitterDev", "Twitter");  try {     MultiUserLookupResponse result = apiInstance.users().findUsersByUsername(usernames, null, null, null);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsersApi#findUsersByUsername");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`
    

      `// Set the params values  // List<String> | Required . A list of usernames, comma-separated. You can specify up to 100 usernames. List<String> usernames = Arrays.asList("TwitterDev", "Twitter");  // Set<String> | A comma separated list of fields to expand. Set<String> expansions = new HashSet<>(Arrays.asList("pinned_tweet_id"));  // Set<String> | A comma separated list of Tweet fields to display. Set<String> tweetFields = new HashSet<>(Arrays.asList("created_at"));  // Set<String> | A comma separated list of User fields to display. Set<String> userFields = new HashSet<>(Arrays.asList("created_at"));  try {     MultiUserLookupResponse result = apiInstance.users().findUsersByUsername(usernames, expansions, tweetFields, userFields);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling UsersApi#findUsersByUsername");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`