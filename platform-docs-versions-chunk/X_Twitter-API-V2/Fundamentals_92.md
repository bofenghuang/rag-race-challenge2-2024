platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/rate-limits

### HTTP headers and response codes

Use the HTTP headers in order to understand where the application is at for a given rate limit, on the method that was just utilized.  

Note that the HTTP headers are contextual. When using application-only authentication, they indicate the rate limit for the application context. When using user-based authentication, they indicate the rate limit for that user context.  

* x-rate-limit-limit: the rate limit ceiling for that given endpoint
* x-rate-limit-remaining: the number of requests left for the 15-minute window
* x-rate-limit-reset: the remaining window before the rate limit resets, in UTC [epoch seconds](http://en.wikipedia.org/wiki/Unix_time)  
     

When an application exceeds the rate limit for a given Twitter API endpoint, the API will return a [HTTP 429 “Too Many Requests”](http://tools.ietf.org/html/rfc6585) response code, and the following error will be returned in the response body:

{ "errors": \[ { "code": 88, "message": "Rate limit exceeded" } \] }