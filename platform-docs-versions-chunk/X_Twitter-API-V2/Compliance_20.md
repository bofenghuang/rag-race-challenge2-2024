platform: X
topic: Twitter-API-V2
subtopic: Compliance
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Compliance.md
url: https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance/api-reference/get-compliance-jobs


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const getListComplianceJobs =       await twitterClient.compliance.listBatchComplianceJobs({         type: "tweets", // type value can be "tweets" or "users"         status: "created", // status values can be "created", "in_progress", "completed" or "failed"       });     console.dir(getListComplianceJobs, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  // ComplianceJobType | Type of compliance job to list ComplianceJobType type = ComplianceJobType.fromValue("tweets");  // ComplianceJobStatus | Status of compliance job to list ComplianceJobStatus status = ComplianceJobStatus.fromValue("created"); try {     MultiComplianceJobResponse result = apiInstance.compliance().listBatchComplianceJobs(type, status);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling ComplianceApi#listBatchComplianceJobs");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`