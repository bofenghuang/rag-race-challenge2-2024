platform: Facebook
topic: Graph-API
subtopic: Application Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Application Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/application/da_checks/

### Parameters

| Parameter | Description |
| --- | --- |
| `checks`<br><br>list<string> | Default value: `Vector`<br><br>A list of Dynamic Ads checks that will be run. If not specified, all checks will be run. Valid values are: `app_missing_param_in_events` |
| `connection_method`<br><br>enum{ALL, APP, BROWSER, SERVER} | Connection method of pixel/app event to check. This is optional |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [DACheck](https://developers.facebook.com/docs/marketing-api/reference/da-check/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).