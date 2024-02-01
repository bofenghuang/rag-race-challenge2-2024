platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/methods?context=linkedin%2Fcontext

## BATCH\_FINDER {finderName}

Conceptually, BATCH\_FINDER methods are similar to BATCH\_GET calls. The main difference between these methods is that you use BATCH\_FINDER queries when you don't have identifiers to directly retrieve entities. These methods use the HTTP GET method with a bq={batchFinderName} request parameter which identifies the type of query being made. BATCH\_FINDER methods accept a list of filters set. Instead of calling multiple finders with different filter values, we call one BATCH\_FINDER method with a list of filters. BATCH\_FINDER methods can return zero, one, or more results, depending on the number of entities that match the query input.

    GET https://api.linkedin.com/v2/{service}?bq={batchFinderName}