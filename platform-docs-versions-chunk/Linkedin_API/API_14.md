platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?context=linkedin%2Fcontext&tabs=HTTPS1

## Authorization Code Flow

1. Configure your application in the Developer Portal to obtain _Client ID_ and _Client Secret_.
2. Your application directs the browser to LinkedIn's OAuth 2.0 authorization page where the member authenticates.
3. After authentication, LinkedIn's authorization server passes an authorization code to your application.
4. Your application sends this code to LinkedIn and LinkedIn returns an access token.
5. Your application uses this token to make API calls on behalf of the member.

## How to Implement 3-legged OAuth

Follow the steps given below to implement the 3-legged OAuth for LinkedIn APIs: