platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/client-credentials-flow?context=linkedin%2Fcontext


## API Error Details

| HTTP STATUS CODE | ERROR MESSAGE | DESCRIPTION | RESOLUTION |
| --- | --- | --- | --- |
| 401 | invalid\_client\_id "Client authentication failed" | Client Authentication failed due to bad client credentials passed as part of the request. | Check whether the right **Client ID**, **Client Secret** are passed as part of the request. |
| 401 | access\_denied "This application is not allowed to create application tokens" | The developer application doesn’t have enough permission to generate 2L application token. | Reach out to the LinkedIn Relationship Manager or Business Development team to get the necessary access. |
| 400 | invalid\_request "A required parameter "grant\_type" is missing" | Grant type in the request is missing. It is a mandatory parameter. | Add grant\_type as `client_credentials` in the request. |
| 400 | invalid\_request "A required parameter "client\_id" is missing" | Client ID in the request is missing. It is a mandatory parameter. | Pass the Client ID of the developer application in request. |
| 400 | invalid\_request "A required parameter "client\_secret" is missing" | Client Secret in the request is missing. It is a mandatory parameter. | Pass the Client Secret of the developer application in the request. |
| 400 | invalid\_client\_id "The passed in client\_id is invalid "abcdefghijk"" | Invalid client ID is passed in the request. | Pass the right client ID from the developer application. |