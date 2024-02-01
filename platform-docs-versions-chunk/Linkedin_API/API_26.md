platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/client-credentials-flow?context=linkedin%2Fcontext

## Step 3: Make API Requests

Once you've received an access token, you can make API requests by including an _Authorization_ header with your token in the HTTP call to LinkedIn's API.

### Sample Request

    GET https://api.linkedin.com/v2/jobs HTTP/1.1
    
    Connection: Keep-Alive
    Authorization: Bearer {access_token}