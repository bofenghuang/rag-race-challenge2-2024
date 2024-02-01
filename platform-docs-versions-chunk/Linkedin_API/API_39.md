platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/developer-portal-tools?context=linkedin/context

## Generate a Token in the Developer Portal

Once a token is generated, users are redirected to the token information page which includes details like OAuth scopes and token time to live (TTL) for reference during development activities.

1. Visit the [LinkedIn Developer Portal Token Generator](https://www.linkedin.com/developers/tools/oauth/token-generator) tool.
    
2. Select the app you'd like to generate a token for.
    
3. Select OAuth flow and permission scopes.
    
4. Member approval
    

The authenticated member will receive a request for your app to access to their profile.

5. Token Generation

Once the token is generated, the "Token Details" will be shown along with the token. Click "Copy token" to paste it into your application code.

Should you wish to verify this an existing token, the [Token Inspector tool](https://www.linkedin.com/developers/tools/oauth/token-inspector) is available on the same page as the token generator.