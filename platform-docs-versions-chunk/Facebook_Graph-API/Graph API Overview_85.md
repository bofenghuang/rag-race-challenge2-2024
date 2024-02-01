platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/batch-requests

## Using Multiple Access Tokens

Individual requests of a single batch request can specify its own access tokens as a query string or form post parameter. In that case the top level access token is considered a fallback token and is used if an individual request has not explicitly specified an access token.

This may be useful when you want to query the API using several different User or Page access tokens, or if some of your calls need to be made using an app access token.

You must include an access token as a top level parameter, even when all individual requests contain their own tokens.