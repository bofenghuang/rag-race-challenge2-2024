platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?context=linkedin%2Fcontext&tabs=HTTPS1

## Step 4: Make Authenticated Requests

Once you've obtained an access token, you can start making authenticated API requests on behalf of the member by including an `Authorization` header in the HTTP call to LinkedIn's API.

#### Sample Request

    curl -X GET https://api.linkedin.com/v2/me' \
    -H 'Authorization: Bearer {INSERT_TOKEN}'