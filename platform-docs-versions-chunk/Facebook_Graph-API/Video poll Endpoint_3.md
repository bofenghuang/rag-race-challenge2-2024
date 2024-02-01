platform: Facebook
topic: Graph-API
subtopic: Video poll Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Video poll Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/video-poll/

### Parameters

This endpoint doesn't have any parameters.

### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | The poll ID<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended)[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `question`<br><br>string | The poll question text |
| `show_results`<br><br>bool | True if this is a Live poll and voting is open and the results show after voting |
| `status`<br><br>enum {closed, voting\_open, results\_open} | Live poll status |

### Edges

| Edge | Description |
| --- | --- |
| [`poll_options`](https://developers.facebook.com/docs/graph-api/reference/video-poll/poll_options/) | Options available on this poll |

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |