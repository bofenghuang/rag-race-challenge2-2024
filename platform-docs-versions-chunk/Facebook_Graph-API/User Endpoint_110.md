platform: Facebook
topic: Graph-API
subtopic: User Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/User Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/user/notifications/


### Parameters

| Parameter | Description |
| --- | --- |
| `bot_message_payload_elements`<br><br>string | Optional bot message payload used for sending a customizable generic template XMA to the recipient if a bot message is sent. If not specified, then a standard generic template XMA will be sent using just the message title and body. |
| `filtering`<br><br>list<enum{groups, groups\_social, ema}> | Notification filters to apply. |
| `href` | The relative path and GET params used in the a2u target url. |
| `label`<br><br>string | Optional label to group similar updates. |
| `message`<br><br>JSON object | Contains the title, main message body, and media image for the notification. |
| `title`<br><br>string | title<br><br>Required |
| `body`<br><br>string | body<br><br>Required |
| `media_url`<br><br>URI | media\_url |
| `notif_ids`<br><br>list<string> | The notification ids to act on. |
| `payload`<br><br>string | Optional custom payload that will be added to the URL encoding of the game that is generated when the notification is clicked. |
| `read`<br><br>boolean | Indicates that the provided notification ids should be marked as read |
| `ref`<br><br>string | A reference param used for logging |
| `schedule_interval`<br><br>int64 | Time from now (in seconds) that the notification will be sent |
| `seen`<br><br>boolean | Indicates that the provided notification ids should be marked as seen |
| `template` | Used for creating a2u notifications.<br><br>Supports Emoji |
| `type`<br><br>enum{generic, content\_update} | Notification type |