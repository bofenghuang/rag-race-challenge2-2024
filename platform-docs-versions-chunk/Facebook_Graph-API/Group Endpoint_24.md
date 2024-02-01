platform: Facebook
topic: Graph-API
subtopic: Group Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Group Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/group/feed

### Fields

| Name | Type | Description |
| --- | --- | --- |
| `message` | `string` | The main body of the post, otherwise called the status message. Either `link` or `message` must be supplied. |
| `link` | `string` | The URL of a link to attach to the post. Either `link` or `message` must be supplied. Additional fields associated with `link` are shown below. |

### Response

If successful, you will receive a response with the following information. In addition, this endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/overview#read-after-write) and can immediately return any fields returned by [read](https://developers.facebook.com/docs/graph-api/reference/group/feed#read) operations.

| Name | Description | Type |
| --- | --- | --- |
| `id` | The newly created post ID | `string` |

## Updating

This operation is not supported.