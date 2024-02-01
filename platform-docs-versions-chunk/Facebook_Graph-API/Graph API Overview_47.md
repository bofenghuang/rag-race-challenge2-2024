platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/overview/rate-limiting

### Spark AR Commerce Effect Management

Requests made by your app to any Commerce endpoints are counted against the app’s call count. An app’s call count is the number of calls it can make during a rolling one hour window and is calculated as follows:

`Calls within one hour = 200 + 40 * Number of Catalogs`

The Number of Catalogs is the total number of catalogs across all commerce accounts managed by your app.