platform: Facebook
topic: Graph-API
subtopic: Photo Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Photo Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/photo/insights/

### Parameters

| Parameter | Description |
| --- | --- |
| `date_preset`<br><br>enum{today, yesterday, this\_month, last\_month, this\_quarter, maximum, data\_maximum, last\_3d, last\_7d, last\_14d, last\_28d, last\_30d, last\_90d, last\_week\_mon\_sun, last\_week\_sun\_sat, last\_quarter, last\_year, this\_week\_mon\_today, this\_week\_sun\_today, this\_year} | Preset a date range, like lastweek, yesterday. If since or until presents, it does not work. |
| `metric`<br><br>list<A valid metric for an insights endpoint> | The list of metrics that needs to be fetched |
| `period`<br><br>enum{day, week, days\_28, month, lifetime, total\_over\_range} | The aggregation period |
| `since`<br><br>datetime | Lower bound of the time range to consider |
| `until`<br><br>datetime | Upper bound of the time range to consider |