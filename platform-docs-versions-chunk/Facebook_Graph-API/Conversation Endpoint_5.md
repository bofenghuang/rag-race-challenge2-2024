platform: Facebook
topic: Graph-API
subtopic: Conversation Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Conversation Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/conversation

### Fields

| Name | Description |
| --- | --- |
| `id`<br><br>_string_ | The ID for the conversation |
| `messages`<br><br>_string_ | Messages within the conversation |
| `participants`<br><br>_object_<br><br>`id`<br><br>  <br><br>`email`<br><br>_Page messaging only_<br><br>`name`<br><br>_Page messaging only_<br><br>`username`<br><br>_Instagram Messaging only_ | Participants in the conversation<br><br>  <br><br>Instagram-Scoped ID or Page-scoped ID for a person or Instagram ID for your Instagram Professional account or the Page ID.<br><br>Email for the person or Page<br><br>  <br><br>Name for the person or Page<br><br>  <br><br>Instagram username for a person or your Instagram Profession account |
| `updated_time`<br><br>_datetime_ | The time when the last message was added to the conversation |

To get information about a specific message within a conversation, send a request to the [Message endpoint](https://developers.facebook.com/docs/graph-api/reference/message).