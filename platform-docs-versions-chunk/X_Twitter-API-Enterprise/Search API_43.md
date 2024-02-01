platform: X
topic: Twitter-API-Enterprise
subtopic: Search API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Search API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/api-reference/enterprise-search


## HTTP response codes [¶](#http-response-codes- "Permalink to this headline")

| Status | Text | Description |
| --- | --- | --- |
| 200 | OK  | The request was successful. The JSON response will be similar to the following: |
| 400 | Bad Request | Generally, this response occurs due to the presence of invalid JSON in the request, or where the request failed to send any JSON payload. |
| 401 | Unauthorized | HTTP authentication failed due to invalid credentials. Log in to console.gnip.com with your credentials to ensure you are using them correctly with your request. |
| 404 | Not Found | The resource was not found at the URL to which the request was sent, likely because an incorrect URL was used. |
| 422 | Unprocessable Entity | This is returned due to invalid parameters in the query -- e.g. invalid PowerTrack rules. |
| 429 | Unknown Code | Your app has exceeded the limit on connection requests. The corresponding JSON message will look similar to the following: |
| 500 | Internal Server Error | There was an error on the server side. Retry your request using an exponential backoff pattern. |
| 502 | Proxy Error | There was an error on server side. Retry your request using an exponential backoff pattern. |
| 503 | Service Unavailable | There was an error on server side. Retry your request using an exponential backoff pattern. |