platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/methods?context=linkedin%2Fcontext

# Request Methods

LinkedIn's APIs have an expressive set of methods for interacting.

## GET

The GET method requests a single, specific entity/object from a service. This method leverages the traditional HTTP GET method.

    GET https://api.linkedin.com/v2/{service}/{resourceIdentifier}
    

## GET\_ALL

The GET\_ALL method requests all entities/objects from a service. GET\_ALL requests never provide resource identifiers to a service. This method uses the traditional HTTP GET method.

    GET https://api.linkedin.com/v2/{service}
    

## BATCH\_GET

The BATCH\_GET method requests more than one specific entity/object from a service. This method uses the traditional HTTP GET method.

    GET https://api.linkedin.com/v2/{service}?ids=List(resourceIdentifier_1,...,resourceIdentifier_n)