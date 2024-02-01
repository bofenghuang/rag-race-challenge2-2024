platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?context=linkedin%2Fcontext&tabs=HTTPS1


## API Error Details

Following are the API errors and its resolution for 3-legged OAuth. If you wish to view the standard HTTP status codes and its meaning, see [Error Handling](https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/error-handling) page.

#### /oauth/v2/authorization

| HTTP STATUS CODE | ERROR MESSAGE | ERROR DESCRIPTION | RESOLUTION |
| --- | --- | --- | --- |
| 401 | Redirect\_uri doesn’t match | Redirect URI passed in the request does not match the redirect URI added to the developer application. | Ensure that the redirect URI passed in the request match the redirect URI added in the developer application under the Authorization tab. |
| 401 | Client\_id doesn’t match | Client ID passed in the request does not match the client ID of the developer application. | Ensure that the client ID passed is in match with the developer application. |
| 401 | Invalid scope | Permissions passed in the request is invalid | Ensure that the permissions sent in scope parameter is assigned to the developer application in the developer portal. |

#### /oauth/v2/accessToken

| HTTP STATUS CODE | ERROR MESSAGE | ERROR DESCRIPTION | RESOLUTION |
| --- | --- | --- | --- |
| 401 | invalid\_request "Unable to retrieve access token: authorization code not found" | Authorization code sent is invalid or not found. | Check whether the sent authorization code is valid. |
| 400 | invalid\_request "A required parameter "redirect\_uri" is missing" | Redirect\_uri in the request is missing. It is mandatory parameter. | Pass the redirect\_uri in the request to route user back to correct landing page. |
| 400 | invalid\_request "A required parameter "code" is missing" | Authorization code in the request is missing. It is mandatory parameter. | Pass the Authorization code received as part of authorization API call. |
| 400 | invalid\_request "A required parameter "grant\_type" is missing" | Grant type in the request is missing. It is mandatory parameter. | Add grant\_type as "authorization\_code" in the request. |
| 400 | invalid\_request "A required parameter "client\_id" is missing" | Client ID in the request is missing. It is mandatory parameter. | Pass the client id of the app in request. |
| 400 | invalid\_request "A required parameter "client\_secret" is missing" | Client Secret in the request is missing. It is mandatory parameter. | Pass the client secret of the app in request. |
| 400 | invalid\_redirect\_uri "Unable to retrieve access token: appid/redirect uri/code verifier does not match authorization code. Or authorization code expired. Or external member binding exists" | Invalid redirect uri is passed in the request. | Pass the right redirect uri tagged to the developer application. |
| 400 | invalid\_redirect\_uri "Unable to retrieve access token: appid/redirect uri/code verifier does not match authorization code. Or authorization code expired. Or external member binding exists | Invalid Authorization code is sent as part of the request" | Authorization code expired and re-authenticate member to generate new authorization code and pass the fresh authorization code to exchange for access token. |