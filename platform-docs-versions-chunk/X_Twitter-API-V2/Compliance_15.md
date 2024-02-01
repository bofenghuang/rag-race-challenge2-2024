platform: X
topic: Twitter-API-V2
subtopic: Compliance
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Compliance.md
url: https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance/api-reference/get-compliance-jobs-id


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const getComplianceJob =       await twitterClient.compliance.getBatchComplianceJob(         //ID of the compliance job to retrieve         1382081613278814209       );     console.dir(getComplianceJob, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // String | ID of the compliance job to retrieve. String id = "1382081613278814209";  try {     SingleComplianceJobResponse result = apiInstance.compliance().getBatchComplianceJob(id);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling ComplianceApi#getBatchComplianceJob");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`