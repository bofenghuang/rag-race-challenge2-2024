platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?context=linkedin%2Fcontext&tabs=HTTPS1

# Authorization Code Flow (3-legged OAuth)

The Authorization Code Flow is used for applications to request permission from a LinkedIn member to access their account data. The level of access or profile detail is explicitly requested using the `scope` parameter during the [authorization](#step-2-request-an-authorization-code) process outlined below. This workflow will send a consent prompt to a selected member, and once approved your application may begin making API calls on behalf of that member.

This approval process ensures that LinkedIn members are aware of what level of detail an application may access or action it may perform on their behalf.

If multiple scopes are requested, the user must be consent to all of them and may not select individual scopes. For the benefit of your LinkedIn users, please ensure that your application requests the least number of scope permissions.

Note

**Generate a Token Manually Using the Developer Portal**  
The LinkedIn Developer Portal has a token generator for manually creating tokens. Visit the [LinkedIn Developer Portal Token Generator](https://www.linkedin.com/developers/tools/oauth/token-generator) or follow the steps outlined in [Developer Portal Tools.](https://learn.microsoft.com/en-us/linkedin/shared/authentication/developer-portal-tools)