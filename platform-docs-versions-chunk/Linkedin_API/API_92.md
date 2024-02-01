platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/webhook-validation?context=linkedin%2Fcontext


### Validating the Webhook Endpoint

LinkedIn validates the ownership of a webhook URL before it can be registered by an application. The validation flow leverages the application's `clientSecret` as the secret key along with the universally-known HMACSHA256 algorithm to generate and validate the application's response to a challenge code.

1. Before initiating the validation flow, LinkedIn will generate a string that will act as the `challengeCode`.
2. LinkedIn will use the `challengeCode` as a query parameter to make an HTTP GET to your webhook endpoint. Integrations using parent-child applications will also receive an `applicationId` query parameter.

    GET https://webhooks.example.com/linkedin?challengeCode=890e4665-4dfe-4ab1-b689-ed553bceeed0
    

3. Your application must compute the challengeResponse (Hex-encoded HMACSHA256 signature for the challengeCode) using its clientSecret as the secret key. If you received an applicationId query parameter in the previous step, use the clientSecret associated with the challenged application. Return both the challengeCode and challengeResponse in a JSON payload with a 200 OK status within 3 seconds. See the example below. The response should have header "content-type" value set to "application/json".

    challengeResponse = Hex-encoded(HMACSHA256(challengeCode, clientSecret))
    

    {
     "challengeCode" : "890e4665-4dfe-4ab1-b689-ed553bceeed0",
     "challengeResponse" : "27b1d19678542072a7f1d0ce845d0c78cec22567f413697e25648f44fa3d1514"
    }
    

4. On receiving the validation response, LinkedIn will verify by computing the challenge response and comparing it with the `challengeResponse` returned by the app.
5. If the `challengeResponse` is successfully verified, then the webhook is ready to be used in subscriptions. If the verification fails, an error will be thrown with the message: `This URL did not pass the security challenge check`.