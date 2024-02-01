platform: Facebook
topic: Graph-API
subtopic: Video Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Video Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/video/polls/

### Parameters

| Parameter | Description |
| --- | --- |
| `correct_option`<br><br>int64 | Number of the correct option (in order, starting from 1) |
| `options`<br><br>array<string> | Text options for users to select in order<br><br>Required |
| `question`<br><br>string | Question text<br><br>Required |
| `show_results`<br><br>boolean | True to show the results after voting, otherwise false |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node represented by `id` in the return type.

Struct {

`id`: numeric string,

`option_ids`: List \[

numeric string

\],

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

## Updating

You can't perform this operation on this endpoint.