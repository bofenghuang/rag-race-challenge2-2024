platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/results

# Paginated Results

We cover the basics of Graph API terminology and structure in the [Graph API overview](https://developers.facebook.com/docs/graph-api/overview). This document goes into more detail about the results from your API requests.

## Traversing Paged Results

When making an API request to a node or edge, you usually don't receive all of the results of that request in a single response. This is because some responses could contain thousands of objects so most responses are paginated by default.