platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-media/insights


### Response Contents

| Property | Value Type | Description |
| --- | --- | --- |
| `data` | Array | An array containing an object describing your request results. |
| `name` | String | [Metric](#metrics) name. |
| `period` | String | Period requested. Period is automatically set to `lifetime` in the request and cannot be changed, so this value will always be `lifetime`. |
| `values` | Array | An array containing an object describing requested [metric](#metrics) values. |
| `value` | Integer | For `data.values.value`, sum of requested [metric](#metrics) values.<br><br>  <br><br>For `data.total_value.value`, sum of requested [breakdown](#breakdown) values.<br><br>  <br><br>For `data.total_value.breakdowns.results.value`, sum of [breakdown](#breakdown) set values. |
| `title` | String | [Metric](#metrics) title. |
| `description` | String | [Metric](#metrics) description. |
| `id` | String | A string describing the query's path parameters. |
| `total_value` | Object | Object describing requested [breakdown](#breakdown) values (if breakdowns were requested). |
| `breakdowns` | Array | An array of objects describing the [breakdowns](#breakdown) requested and their results. |
| `dimension_keys` | Array | Array of strings describing [breakdowns](#breakdown) requested. |
| `results` | Array | An array of objects describing each [breakdown](#breakdown) set. |
| `dimension_values` | String | An array of strings describing [breakdown](#breakdown) set values. Values can be mapped to `dimension_keys`. |
| `paging` | Object | An object containing URLs used to request the next set of results. See [Paginated Results](https://developers.facebook.com/docs/instagram-api/reference/ig-media/docs/graph-api/results) for more information. |
| `previous` | String | URL to retrieve the previous page of results. See [Paginated Results](https://developers.facebook.com/docs/instagram-api/reference/ig-media/docs/graph-api/results) for more information. |
| `next` | String | URL to retrieve the next page of results. See [Paginated Results](https://developers.facebook.com/docs/instagram-api/reference/ig-media/docs/graph-api/results) for more information. |