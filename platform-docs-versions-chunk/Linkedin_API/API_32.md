platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/postman-getting-started

### Step 6 - Identity Authentication

If the Grant Type in Step 5 was Authorization Code then Postman will take you to the LinkedIn authorization page, where you may be prompted to log into LinkedIn. Click "Allow" to authorize the request. The prompt on the authorization page is dictated by the requested scopes in the previous step.

### Step 7 - Use Token

Postman will then display your access token to be used for testing. Choose the 'Use Token' button to set this as the currently used token. The token will automatically be propagated to all requests within the corresponding collection. The video below shows an example of requesting a 3-legged token via the Authorization Code Grant Type.