platform: X
topic: Twitter-API-V2
subtopic: Lists
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Lists.md
url: https://developer.twitter.com/en/docs/twitter-api/lists/manage-lists/api-reference/post-lists


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const createList = await twitterClient.lists.listIdCreate({       name: "test v2 create list",       description: "example create",       private: false,     });     console.dir(createList, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  ListCreateRequest listCreateRequest = new ListCreateRequest(); listCreateRequest.name("test v2 create list"); listCreateRequest.description("example create"); listCreateRequest._private(false);  try {     ListCreateResponse result = apiInstance.lists().listIdCreate(listCreateRequest);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling ListsApi#listIdCreate");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`