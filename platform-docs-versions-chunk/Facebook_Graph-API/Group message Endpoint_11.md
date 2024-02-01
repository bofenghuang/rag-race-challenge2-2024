platform: Facebook
topic: Graph-API
subtopic: Group message Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Group message Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/group-message/insights/

### Parameters

| Parameter | Description |
| --- | --- |
| `date_preset`<br><br>enum{today, yesterday, this\_month, last\_month, this\_quarter, maximum, data\_maximum, last\_3d, last\_7d, last\_14d, last\_28d, last\_30d, last\_90d, last\_week\_mon\_sun, last\_week\_sun\_sat, last\_quarter, last\_year, this\_week\_mon\_today, this\_week\_sun\_today, this\_year} | date\_preset |
| `metric`<br><br>list<A valid metric for an insights endpoint> | metric |
| `period`<br><br>enum{day, week, days\_28, month, lifetime, total\_over\_range} | period |
| `since`<br><br>datetime | since |
| `until`<br><br>datetime | until |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [InsightsResult](https://developers.facebook.com/docs/graph-api/reference/insights-result/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).