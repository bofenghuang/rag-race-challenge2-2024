platform: Facebook
topic: Graph-API
subtopic: Whats app business account Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Whats app business account Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/message_templates/

### Request Syntax

GET /<WHATSAPP\_BUSINESS\_ACCOUNT\_ID>/message\_templates
  ?category=<CATEGORY>,
  &content=<CONTENT>,
  &language=<LANGUAGE>,
  &name=<NAME>,
  &name\_or\_content=<NAME\_OR\_CONTENT>,
  &quality\_score=<QUALITY\_SCORE>,
  &status=<STATUS>

### Path Parameters

| Placeholder | Value |
| --- | --- |
| `<WHATSAPP_BUSINESS_ACCOUNT_ID>` | WhatsApp Business Account ID. |

### Response

A list of [WhatsApp Message Template](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-hsm/) nodes.

### Sample Request

curl 'https://graph.facebook.com/v16.0/102290129340398/message\_templates?category=utility' \\
-H 'Authorization: Bearer EAAJB...'