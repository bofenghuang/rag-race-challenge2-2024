platform: Facebook
topic: Graph-API
subtopic: User Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/User Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/user/assigned_business_asset_groups/


### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {},
    "`summary`": {}
}

#### `data`

A list of BusinessAssetGroup nodes.

The following fields will be added to each node that is returned:

| Field | Description |
| --- | --- |
| `adaccount_tasks`<br><br>list<string> | Permission tasks for ad accounts contained in business asset group.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `offline_conversion_data_set_tasks`<br><br>list<string> | Permission tasks for offline conversion datasets contained in business asset group.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `page_tasks`<br><br>list<string> | Permission tasks fo pages contained in business asset group.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `pixel_tasks`<br><br>list<string> | Permission tasks for ads pixels contained in business asset group.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

#### `summary`

Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=total_count`).

| Field | Description |
| --- | --- |
| `total_count`<br><br>int32 | Total count of business asset groups<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |