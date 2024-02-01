platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/client-credentials-flow?context=linkedin%2Fcontext

## Step 2: Generate an Access Token

To generate an access token, issue a HTTP POST against `accessToken` with a `Content-Type` header of `x-www-form-urlencoded` and the following parameters in the request body:

    https://www.linkedin.com/oauth/v2/accessToken
    

| Parameter | Description | Required |
| --- | --- | --- |
| grant\_type | The value of this field should always be `client_credentials` | Yes |
| client\_id | The _Client ID_ value generated when you registered your application | Yes |
| client\_secret | The _Client Secret_ value generated when you registered your application | Yes |

* View the [Best Practices for Secure Applications](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/best-practices/secure-applications?context=linkedin/context) page for more security info.