platform: X
topic: Twitter-API-Enterprise
subtopic: Engagement API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Engagement API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/engagement-api/api-reference/post-insights-engagement


## Response Codes [¶](#response-codes- "Permalink to this headline")

| Status | Text | Description |
| --- | --- | --- |
| 200 | OK  | The request was successful. |
| 400 | Bad Request | Generally, this response occurs due to the presence of invalid JSON in the request, or where the request failed to send any JSON payload. |
| 401 | Unauthorized | HTTP authentication failed due to invalid credentials. Check your OAuth keys and tokens. |
| 404 | Not Found | The resource was not found at the URL to which the request was sent, likely because an incorrect URL was used. |
| 429 | Too Many Requests | Your app has exceeded the limit on API requests. |
| 500 | Internal Server Error | There was an error on Gnip's side. Retry your request using an exponential backoff pattern. |
| 502 | Proxy Error | There was an error on Gnip's side. Retry your request using an exponential backoff pattern. |
| 503 | Service Unavailable | There was an error on Gnip's side. Retry your request using an exponential backoff pattern. |