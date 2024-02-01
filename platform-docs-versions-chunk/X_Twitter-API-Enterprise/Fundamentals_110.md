platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/expanded-and-enhanced-urls


### HTTP Status Codes

The expanded URL enrichment also provides the HTTP status code for the final URL we are attempting to unwind. In normal cases, this will be a 200 value. Other 400-series values indicate problems with resolving the URL.

Various status codes may be returned when attempting to unwind a URL. During the process of unwinding a URL, if we get a redirect, we will follow them indefinitely until we either:

* Hit a 200 series code (success)
* Hit a non-redirect series code (failures)
* Timeout because the final URL could not be resolved in a reasonable amount of time (returns a 408 - timeout)
* Hit an exception of some sort  
     

If an exception is hit, we use the following mapping between reasons and status codes returned:

| Reason | Status Code Returned |
| --- | --- |
| SSL Exceptions | 403 (Forbidden) |
| Unwinding not allowed by URL | 405 |
| Socket Timeout | 408 (Timeout) |
| Unknown Host Exception | 404 (Not Found) |
| Unsupported Operation | 404 (Not Found) |
| Connect Exception | 404 (Not Found) |
| Illegal Argument | 400 (Bad Request) |
| Everything else | 400 (Bad Request) |