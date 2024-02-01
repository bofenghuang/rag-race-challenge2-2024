platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/methods?context=linkedin%2Fcontext

## BATCH\_CREATE

The BATCH\_CREATE method indicates to a service that it should use the information provided in the request body to create multiple new entities. This method uses the traditional HTTP POST method.

    POST https://api.linkedin.com/v2/{service}/{Request Body}
    

## UPDATE

The UPDATE method indicates to a service that it should use the information provided in the request body to overwrite the entire definition of an existing entity. This method uses the traditional HTTP PUT method.

    PUT https://api.linkedin.com/v2/{service}/{Request Body}
    

## BATCH\_UPDATE

The BATCH\_UPDATE method indicates to a service that it should use the information provided in the request body to overwrite the entire definitions of multiple existing entities. This method uses the traditional HTTP `PUT` method.

    PUT https://api.linkedin.com/v2/{service}/{Request Body}