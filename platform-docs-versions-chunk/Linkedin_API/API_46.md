platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/error-handling?context=linkedin%2Fcontext

## HTTP Status Codes and Error Types

LinkedIn uses [standard HTTP status codes](https://tools.ietf.org/html/rfc2616#section-10) for each API’s response.

Status codes are divided into the following five categories:

* 1xx: Informational - Communicates transfer protocol-level information.
* 2xx: Success - The request was successful.
* 3xx: Redirection - The client must take some additional action to complete the request.
* 4xx: Client Error - Failed request due to client error.
* 5xx: Server Error - Failed request due to server error.

## 400 Bad Request

A `400 Bad Request` error means that the server was unable to proceed with the request. The most common cause of the error is bad syntax in the request URL or body. To fix a `400 Bad Request` error, do the following:

* Check if an invalid character is included in the [URL](https://www.w3.org/TR/url/#canonicalize-a-url).
* Check API examples.
* Ask your colleagues for help.
* Talk to the [rubber duck](https://en.wikipedia.org/wiki/Rubber_duck_debugging).