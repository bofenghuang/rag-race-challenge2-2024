platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/error-handling?context=linkedin%2Fcontext

# Error Handling

HTTP requests can fail for a variety of reasons. LinkedIn provides standard HTTP status codes and clear and concise messages to help you easily understand these errors.

#### Sample Response

    {
        "message": "Empty oauth2_access_token",
        "serviceErrorCode": 401,
        "status": 401
    }
    

Error responses have the following details:

* `message` - A description of the error.
* `serviceErrorCode` - A subcode that further classifies the error.
* `status` - The type of error (status code).