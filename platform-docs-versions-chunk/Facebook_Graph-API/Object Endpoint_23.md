platform: Facebook
topic: Graph-API
subtopic: Object Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Object Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/object/private_replies

## Permissions

This edge requires a Page access token with the following permissions:

* `pages_messaging`

Apps with Standard Access can only send and receive messages from people who have a role on your app. Additionally Pages in `unpublished` status will only be allowed to message people with a role on the Page.

### Fields

| Parameter | Description | Type |
| --- | --- | --- |
| `id` | The ID of the Page Comment or Visitor Post that you are replying to. | `string` |
| `message` | The text of the reply. **This field is required**. | `string` |

### Response

If successful, you will receive a response with the following fields. In addition, this endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/using-graph-api#read-after-write) and can immediately read the node represented by `id` in the return type.

| Field | Description | Type |
| --- | --- | --- |
| id  | The ID of the newly created Message. | `string` |

## Deleting

You can't delete using this edge.