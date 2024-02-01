platform: Facebook
topic: Graph-API
subtopic: Page upcoming change Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Page upcoming change Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/page-upcoming-change/


### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | The ID of the upcoming change |
| `change_type`<br><br>enum | The type of the upcoming change<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `effective_time`<br><br>datetime | The time when the upcoming change will become effective<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `page`<br><br>[Page](https://developers.facebook.com/docs/graph-api/reference/page/) | The associated page of this upcoming change<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `proposal`<br><br>[PageChangeProposal](https://developers.facebook.com/docs/graph-api/reference/page-change-proposal/) | The proposal associated with the change, only valid when change\_type is knowledge\_proposal<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `timer_status`<br><br>enum | The status of the timer associated with this change<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |