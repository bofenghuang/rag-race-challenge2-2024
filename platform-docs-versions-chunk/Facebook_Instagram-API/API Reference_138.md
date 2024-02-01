platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/insights


### Response Contents

| Property | Value Type | Description |
| --- | --- | --- |
| `breakdowns` | Array | An array of objects describing the [breakdowns](#breakdown) requested and their results.<br><br>  <br><br>Only returned if `metric_type=total_values` is requested. |
| `data` | Array | An array of objects describing your results. |
| `description` | String | [Metric](#metrics) description. |
| `dimension_keys` | Array | An array of strings describing [breakdowns](#breakdown) requested in the query. Can be used as keys corresponding to values in individual breakdown sets.<br><br>  <br><br>Only returned if `metric_type=total_values` is requested. |
| `dimension_values` | Array | An array of strings describing [breakdown](#breakdown) set values. Values can be mapped to `dimension_keys`.<br><br>  <br><br>Only returned if `metric_type=total_values` is requested. |
| `end_time` | String | ISO 8601 timestamp with time and offset. For example: `2022-08-01T07:00:00+0000` |
| `id` | String | A string describing the query's path parameters. |
| `name` | String | [Metric](#metrics) requested. |
| `next` | String | URL to retrieve the next page of results. See [Paginated Results](https://developers.facebook.com/docs/graph-api/results) for more information. |
| `paging` | Object | An object containing URLs used to request the next set of results. See [Paginated Results](https://developers.facebook.com/docs/graph-api/results) for more information. |
| `period` | String | [Period](#period) requested. |
| `previous` | String | URL to retrieve the previous page of results. See [Paginated Results](https://developers.facebook.com/docs/graph-api/results) for more information. |
| `results` | Array | An array of objects describing each [breakdown](#breakdown) set.<br><br>  <br><br>Only returned if `metric_type=total_values` is requested. |
| `title` | String | [Metric](#metrics) title. |
| `total_value` | Object | Object describing requested [breakdown](#breakdown) values (if breakdowns were requested). |
| `value` | Integer | For `data.total_value.value`, sum of requested [metric](#metrics) values.<br><br>  <br><br>For `data.total_value.breakdowns.results.value`, sum of [breakdown](#breakdown) set values. Only returned if `metric_type=total_values` is requested. |