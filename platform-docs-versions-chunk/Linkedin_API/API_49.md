platform: Linkedin
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Linkedin_API/API.md
url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/error-handling?context=linkedin%2Fcontext

## 404 Resource Not Found

This error occurs when your application tries to call an API or fetch an entity that does not exist. For example, the API to get a friend’s profile is `/v2/people/id={personId}`, not `/v2/person/id={personId}`. In some cases (Ads, for example), a 404 error is returned when attempting to access a restricted API. See [403 Access Denied](#403-access-denied) and contact your partner technical support channel if you continue to see the error.

## 405 Method Not Allowed

This error indicates that the HTTP protocol methods in your request are not supported. Check the documentation for the API to see supported methods.

## 411 Length Required

This error indicates that the server refuses to accept the request without a defined `Content-Length` header. Please make sure POST requests with an empty body have a `Content-Length` header specified.