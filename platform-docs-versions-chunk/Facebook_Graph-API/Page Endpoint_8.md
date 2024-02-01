platform: Facebook
topic: Graph-API
subtopic: Page Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Page Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/page/

### Parameters

| Parameter | Description |
| --- | --- |
| `metadata`<br><br>string | Additional information about the conversation |
| `recipient`<br><br>Object | The PSID for the customer who sent the message to your business<br><br>Required |
| `id`<br><br>numeric string |     |
| `phone_number`<br><br>string |     |
| `name`<br><br>Object |     |
| `first_name`<br><br>string |     |
| `last_name`<br><br>string |     |
| `user_ref`<br><br>string |     |
| `comment_id` |     |
| `post_id`<br><br>string |     |
| `player_id`<br><br>player ID |     |
| `one_time_notif_token`<br><br>string |     |
| `notification_messages_token`<br><br>string |     |
| `login_id`<br><br>string |     |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`success`: bool,

}