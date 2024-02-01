platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication?context=linkedin%2Fcontext

## Member Authorization (3-legged OAuth Flow)

The Member Authorization grants permissions to your application by a LinkedIn member to access the member’s resources on LinkedIn. Your application has no access to these resources without member approval. The Member Auth uses the 3-legged OAuth code flow. For step-by-step instructions on how to implement 3-legged OAuth, see [**Authorization Code Flow (3-legged OAuth)**](https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow) page.

Tip

**When to use 3-legged OAuth**  
Use this flow if you are requesting access to a member's account to use their data and make requests on their behalf. This is the most commonly used permission type across LinkedIn APIs. Open permissions available to all applications are of this type such as `r_liteprofile`, `r_emailaddress`, and `w_member_social`.