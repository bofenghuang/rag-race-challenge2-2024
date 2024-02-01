platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/methods?context=linkedin%2Fcontext

## ACTION {actionName}

The ACTION method is a flexible method that does not specify any type of standard behavior. It uses the HTTP POST method, with a special `action={actionName}` request parameter, which identifies the specific type of action to take.

    POST https://api.linkedin.com/v2/{service}?action={actionName}