platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/postman-getting-started

### Step 1 - Application

Go to the [LinkedIn Developer Portal](https://www.linkedin.com/developers/apps), select the app you'll be using, click the "Auth" tab, and locate your Client ID and Client Secret. Please note these values for use later during this process.

### Step 2 - Auth Settings

From the same "Auth" tab, scroll to the bottom of the page. Under "OAuth 2.0 Settings", add the Postman callback URLs `https://oauth.pstmn.io/v1/callback` and `https://oauth.pstmn.io/v1/browser-callback` to your Redirect URL list.

Caution

Postman uses the term "Callback URL"  
LinkedIn uses the term "Redirect URL"