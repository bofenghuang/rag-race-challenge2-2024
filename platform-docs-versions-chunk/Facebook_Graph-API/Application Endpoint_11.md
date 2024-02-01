platform: Facebook
topic: Graph-API
subtopic: Application Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Application Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/application/

### Return Type

Struct {

`num_updated`: int32,

`num_invalid`: int32,

}

### Error Codes

| Error | Description |
| --- | --- |
| 105 | The number of parameters exceeded the maximum for this operation |

You can make a POST request to `page_activities` edge from the following paths:

* [`/{application_id}/page_activities`](https://developers.facebook.com/docs/graph-api/reference/application/page_activities/)

When posting to this edge, an [Application](https://developers.facebook.com/docs/graph-api/reference/application/) will be created.