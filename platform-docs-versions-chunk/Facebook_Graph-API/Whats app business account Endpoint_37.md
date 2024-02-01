platform: Facebook
topic: Graph-API
subtopic: Whats app business account Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Whats app business account Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/message_templates/

### Path Parameters

| Placeholder | Value |
| --- | --- |
| `<WHATSAPP_BUSINESS_ACCOUNT_ID>` | ID of the WhatsApp Business Account that owns the template. |

### Response

See [Return Type](#return-type-2).

### Sample Request

curl -X DELETE 'https://graph.facebook.com/`v19.0`/102290129340398/message\_templates?name=order\_confirmation' \\
-H 'Authorization: Bearer EAAJB...'

### Sample Response

{
  "success": true
}

### Parameters

| Parameter | Description |
| --- | --- |
| `hsm_id`<br><br>whatsapp business hsm ID | ID of template to be deleted. Required if deleting a template by ID. |
| `name`<br><br>string | Name of template to be deleted.<br><br>Required |

### Return Type

Struct {

`success`: bool,

}