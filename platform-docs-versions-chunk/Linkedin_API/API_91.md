platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/webhook-validation?context=linkedin%2Fcontext

### Fields

| Field Name | Description | Required |
| --- | --- | --- |
| applicationId | ID of the Developer Application being validated. Only sent for integrations with parent-child applications such as [Apply Connect](https://learn.microsoft.com/en-us/linkedin/talent/apply-connect). Indicates which application's `clientSecret` to use for generating the challenge response. | False |
| challengeCode | Randomly generated type-4 UUID string created by LinkedIn. | True |
| challengeResponse | Hex-encoded HMACSHA256 signature for the `challengeCode` using its `clientSecret` as the secret key. `challengeResponse = Hex-encoded(HMACSHA256(challengeCode, clientSecret))` | True |