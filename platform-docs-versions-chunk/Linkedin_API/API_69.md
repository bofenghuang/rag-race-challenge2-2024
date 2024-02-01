platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/methods?context=linkedin%2Fcontext

## FINDER {finderName}

Conceptually, FINDER methods are similar to GET/BATCH\_GET calls. The main difference between these methods is that you use FINDER queries when you don't have an identifier to directly retrieve an entity. These methods use the HTTP GET method with a `q={finderName}` request parameter which identifies the type of query being made. FINDER methods can return zero, one, or more results, depending on the number of entities that match the query input.

    GET https://api.linkedin.com/v2/{service}?q={finderName}
    

## CREATE

The CREATE method indicates to a service that it should use the information provided in the request body to create a new entity. This method uses the traditional HTTP POST method.

    POST https://api.linkedin.com/v2/{service}/{Request Body}