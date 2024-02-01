platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?context=linkedin%2Fcontext&tabs=HTTPS1


## Step 1: Configure Your Application

1. Select your application in the [LinkedIn Developer Portal](https://www.linkedin.com/developers/apps).
2. Click the **Auth** tab to view your application credentials.
3. Add the redirect (callback) URL via `HTTPS` to your server.

Note

LinkedIn servers will only communicate with URLs that you have identified as trusted.

* URLs must be absolute:
    * `https://dev.example.com/auth/linkedin/callback`
    * _not_ `/auth/linkedin/callback`
* parameters are ignored:
    * `https://dev.example.com/auth/linkedin/callback?id=1`
    * _will be_ `https://dev.example.com/auth/linkedin/callback`
* URLs cannot include a #
    * `https://dev.example.com/auth/linkedin/callback#linkedin` is invalid.

If you are using Postman to test this flow, use `https://oauth.pstmn.io/v1/callback` as your redirect URL and enable **Authorize using browser**.

Each application is assigned a unique **Client ID** (Consumer key/API key) and **Client Secret**. Please make a note of these values as they will be integrated into your application. Your **Client Secret** protects your application's security so be sure to keep it secure!

Warning

Do not share your _Client Secret_ value with anyone, and **do not** pass it in the URL when making API calls, or URI query-string parameters, or post in support forums, chat, etc.