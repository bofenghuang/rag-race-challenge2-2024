platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?context=linkedin%2Fcontext&tabs=HTTPS1


## Step 5: Refresh Access Token

Tip

To protect members' data, LinkedIn does not generate long-lived access tokens.

> Make sure your application refreshes access tokens before they expire, to avoid unnecessarily sending your application's users through the authorization process again.

Refreshing an access token is a seamless user experience. To refresh an access token, go through the [authorization process](#step-2-request-an-authorization-code) again to fetch a new token. This time however, in the refresh workflow, the authorization screen is bypassed, and the member is redirected to your redirect URL, provided the following conditions are met:

* The member is still logged into [www.linkedin.com](https://www.linkedin.com/)
* The member's current access token has not expired

If the member is no longer logged in to [www.linkedin.com](https://www.linkedin.com/) or their access token has expired, they are sent through the normal [authorization process](#step-2-request-an-authorization-code).

Programmatic refresh tokens are available for a limited set of partners. If this feature has been enabled for your application, see [Programmatic Refresh Tokens](https://learn.microsoft.com/en-us/linkedin/shared/authentication/programmatic-refresh-tokens?context=linkedin/context) for instructions.