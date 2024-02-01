platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/client-credentials-flow?context=linkedin%2Fcontext

### Sample Request (Secure Approach)

    POST https://www.linkedin.com/oauth/v2/accessToken HTTP/1.1
    
    Content-Type: application/x-www-form-urlencoded
    grant_type=client_credentials
    client_id={your_client_id}
    client_secret={your_client_secret}
    

A successful access token request returns a [JSON](http://www.json.org/) object containing the following fields:

* `access_token` — The access token for the application. This token must be kept secure.
* `expires_in` — Seconds until token expiration.
    * The access token has a 30-minute lifespan and must be used immediately. You may request a new token once your current token expires.

### Sample Response

    {
        "access_token": "AQV8...",
        "expires_in": "1800"
    }
    

For error details, refer the [API Error Details](#api-error-details) section.