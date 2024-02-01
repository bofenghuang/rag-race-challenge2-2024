platform: Facebook
topic: Graph-API
subtopic: Whats app business account Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Whats app business account Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/message_templates/


### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {},
    "`summary`": {}
}

#### `data`

A list of [WhatsAppBusinessHSM](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-hsm/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

#### `summary`

Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=total_count`).

| Field | Description |
| --- | --- |
| `total_count`<br><br>unsigned int32 | The total number of message templates that belong to a WhatsApp Business Account |
| `message_template_count`<br><br>int32 | The current number of message templates that belong to the WhatsApp Business Account |
| `message_template_limit`<br><br>int32 | The maximum number of message templates that can belong to a WhatsApp Business Account |
| `are_translations_complete`<br><br>bool | The status for template translations |