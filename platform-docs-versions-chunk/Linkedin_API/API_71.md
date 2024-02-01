platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/methods?context=linkedin%2Fcontext

## PARTIAL\_UPDATE

The PARTIAL\_UPDATE method indicates to a service that it should use the information provided in the request body to update only specific portions of an existing entity rather than overwriting the entire definition of the entity. This method uses the traditional HTTP POST method.

Note

For the server to differentiate between a PARTIAL\_UPDATE and an UPDATE, you must include `X-Restli-Method: PARTIAL_UPDATE` as the header value in your request.

    POST https://api.linkedin.com/v2/{service}/{Request Body}