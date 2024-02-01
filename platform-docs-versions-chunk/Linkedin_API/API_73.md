platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/methods?context=linkedin%2Fcontext

## BATCH\_DELETE

The BATCH\_DELETE method indicates to a service that it should delete multiple identified objects/entities. This method uses the traditional HTTP DELETE method.

    DELETE https://api.linkedin.com/v2/{service}?ids=List({resourceIdentifier_1},...,{resourceIdentifier_n})