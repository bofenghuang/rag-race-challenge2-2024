platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/error-handling?context=linkedin%2Fcontext

## 403 Access Denied

When your application makes an API call with a member’s access token, LinkedIn checks if the access token has permission to access the API. If the access token does not have the correct permissions, a `403 Access Denied` error is returned. When this happens, check the following:

* Does your application have permissions to make the API call?
* Does your application ask the user to enable these permissions?
* Did your application [change the scope](https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?context=linkedin/context) while requesting an access token?  
    

If you continue to see the error, reach out to your partner technical support channel or [https://developer.linkedin.com/support](https://developer.linkedin.com/support).