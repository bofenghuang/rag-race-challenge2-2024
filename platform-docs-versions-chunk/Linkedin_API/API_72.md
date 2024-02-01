platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/methods?context=linkedin%2Fcontext

## BATCH\_PARTIAL\_UPDATE

The BATCH\_PARTIAL\_UPDATE method indicates to a service that it should use the multiple pieces of information provided in the request body to update specific portions of multiple specified entities, rather than overwriting them entirely. This method uses the traditional HTTP POST method.

Note

For the server to differentiate between a `BATCH_PARTIAL_UPDATE` and a `BATCH_UPDATE`, you must include `X-Restli-Method: BATCH_PARTIAL_UPDATE` as the header value in your request.

    POST https://api.linkedin.com/v2/{service}/{Request Body}
    

## DELETE

The DELETE method indicates to a service that it should delete an identified object/entity. This method uses the traditional HTTP DELETE method.

    DELETE https://api.linkedin.com/v2/{service}/{resourceIdentifier}