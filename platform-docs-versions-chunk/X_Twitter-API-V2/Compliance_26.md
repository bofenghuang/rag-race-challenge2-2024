platform: X
topic: Twitter-API-V2
subtopic: Compliance
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Compliance.md
url: https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance/api-reference/post-compliance-jobs


### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [TypeScript](#tab0)
* [Java](#tab1)

TypeScript

Java

      `(async () => {   try {     const createComplianceJob =       await twitterClient.compliance.createBatchComplianceJob({         type: "tweets", // Type of compliance job to create - value can be "tweets" or "users"         resumable: true, //Optional - Specifies whether to enable the upload URL with support for resumable uploads. If true, this endpoint will return a pre-signed URL with resumable uploads enabled.         name: "Job name", //Optional - A name for this job, useful to identify multiple jobs using a label you define.       });     console.dir(createComplianceJob, {       depth: null,     });   } catch (error) {     console.log(error);   } })();`
    

      `// Set the params values  CreateBatchComplianceJobRequest createBatchComplianceJobRequest = new CreateBatchComplianceJobRequest();  //ComplianceJobType | Type of compliance job to create ComplianceJobType jobType = ComplianceJobType.fromValue("tweets");  createBatchComplianceJobRequest.type(jobType);  //Optional - A name for this job, useful to identify multiple jobs using a label you define. createBatchComplianceJobRequest.name("job name");  //Optional - Specifies whether to enable the upload URL with support for resumable uploads. If true, this endpoint will return a pre-signed URL with resumable uploads enabled. createBatchComplianceJobRequest.resumable(true);  try {     SingleComplianceJobResponse result = apiInstance.compliance().createBatchComplianceJob(createBatchComplianceJobRequest);     System.out.println(result); } catch (ApiException e) {     System.err.println("Exception when calling ComplianceApi#createBatchComplianceJob");     System.err.println("Status code: " + e.getCode());     System.err.println("Reason: " + e.getResponseBody());     System.err.println("Response headers: " + e.getResponseHeaders());     e.printStackTrace(); }`