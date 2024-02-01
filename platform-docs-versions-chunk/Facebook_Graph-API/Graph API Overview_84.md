platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/batch-requests

## Timeouts

Large or complex batches may timeout if it takes too long to complete all the requests within the batch. In such a circumstance, the result is a partially-completed batch. In a partially-completed batch, requests that are completed successful will return the normal output with the `200` status code. Responses for requests that are not successful will be `null`. You can retry any unsuccessful request.

## Batch calls with JSONP

The Batch API supports JSONP, just like the rest of the Graph API - the JSONP callback function is specified using the `callback` query string or form post parameter.