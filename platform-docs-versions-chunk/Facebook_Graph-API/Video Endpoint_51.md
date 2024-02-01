platform: Facebook
topic: Graph-API
subtopic: Video Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Video Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/video/video_insights/

### Parameters

| Parameter | Description |
| --- | --- |
| `metric`<br><br>list<A valid metric for an insights endpoint> | A list of [available metrics](#metrics) that you want to receive. |
| `period`<br><br>enum{day, week, days\_28, month, lifetime, total\_over\_range} | The aggregation period. |
| `since`<br><br>datetime/timestamp | Lower bound of the time range to consider. |
| `until`<br><br>datetime/timestamp | Upper bound of the time range to consider. |

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