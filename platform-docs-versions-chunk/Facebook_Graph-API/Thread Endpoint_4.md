platform: Facebook
topic: Graph-API
subtopic: Thread Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Thread Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/thread

### Fields

| Name | Description | Type |
| --- | --- | --- |
| `id` | The unique ID for this message thread. | `string` |
| `comments` | The messages in this thread. | [`Message[]`](https://developers.facebook.com/docs/graph-api/reference/message/) |
| `to` | Profiles that are subscribed to the thread. | [`Profile[]`](https://developers.facebook.com/docs/graph-api/reference/profile/) |
| `unread` | The amount of messages that are unread by the session profile. | `integer` |
| `unseen` | The amount of messages that are unseen by the session profile. | `integer` |
| `updated_time` | When the thread was last updated. | `datetime` |
| `can_reply` | Can the page reply in the thread. | `boolean` |
| `linked_group` | ID of the Workplace group that the thread is linked to (Workplace only) | `string` |

### Edges

| Name | Description |
| --- | --- |
| `messages` | List of individual messages in the thread. See [Messages](https://developers.facebook.com/docs/graph-api/reference/message) |