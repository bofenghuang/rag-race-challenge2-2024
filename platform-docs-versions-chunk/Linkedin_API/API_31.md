platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/postman-getting-started


### Step 5 - Headers

Each collection in each workspace will have its OAuth 2.0 Authorization settings pre-populated with the correct URLs, environment variables, and scopes to be able to successfully run the requests within the corresponding Use Cases folder. Click on a collection title to open it's Authorization tab. Ensure that the correct environment is selected and click "Get new access token":

* Grant Type: Authorization Code (3-legged token) or Client Credentials (2-legged token)
* Callback (Redirect) URL: `https://oauth.pstmn.io/v1/browser-callback`
    * Note the Callback URL should be `https://oauth.pstmn.io/v1/callback` with the "Authorize using browser" box checked if you are using the Postman Desktop app
* Auth URL: `https://www.linkedin.com/oauth/v2/authorization`
* Access Token URL: `https://www.linkedin.com/oauth/v2/accessToken`
* Client ID: {using the client\_id from the environment variables}
* Client Secret: {using the client\_secret from the environment variables}
* Scope: Differs per collection but an example is {`rw_ads,r_basicprofile,w_organization_social,w_member_social,rw_organization_admin`}
* Client Authentication: `Send client credentials in body` when the Grant Type is Authorization Code. `Send as Basic Auth header` when the Grant Type is Client Credentials.