platform: X
topic: Twitter-API-Enterprise
subtopic: Compliance Firehose API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Compliance Firehose API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/compliance-firehose-api/api-reference/compliance-firehose


## Response Codes [¶](#response-codes- "Permalink to this headline")

The following responses may be returned by the API for these requests. Most error codes are returned with a string with additional details in the body. For non-200 responses, clients should attempt to reconnect.

| Status | Text | Definition |
| --- | --- | --- |
| 200 | Success | The connection was successfully opened, and new activities will be sent through as they arrive. |
| 401 | Unauthorized | HTTP authentication failed due to invalid credentials. Log in to console.gnip.com with your credentials to ensure you are using them correctly with your request. |
| 406 | Not Acceptable | Generally, this occurs where your client fails to properly include the headers to accept gzip encoding from the stream, but can occur in other circumstances as well. Will contain a JSON message similar to "This connection requires compression. To enable compression, send an 'Accept-Encoding: gzip' header in your request and be ready to uncompress the stream as it is read on the client end." |
| 429 | Rate Limited | Your app has exceeded the limit on connection requests. |
| 503 | Service Unavailable | Twitter server issue. Reconnect using an exponential backoff pattern. If no notice about this issue has been posted on the [Twitter API Status Page](https://api.twitterstat.us/), contact support. |