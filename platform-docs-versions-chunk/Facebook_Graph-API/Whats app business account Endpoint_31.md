platform: Facebook
topic: Graph-API
subtopic: Whats app business account Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Whats app business account Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/message_templates/

### Requirements

| Type | Description |
| --- | --- |
| Access Tokens | [User](https://developers.facebook.com/docs/whatsapp/business-management-api/get-started#user-access-tokens) or [System User](https://developers.facebook.com/docs/whatsapp/business-management-api/get-started#system-user-access-tokens) |
| Permissions | [whatsapp\_business\_management](https://developers.facebook.com/docs/permissions/reference/whatsapp_business_management) |

### Request Syntax

POST /<WHATSAPP\_BUSINESS\_ACCOUNT\_ID>/message\_templates

### Path Parameters

| Placeholder | Value |
| --- | --- |
| `<WHATSAPP_BUSINESS_ACCOUNT_ID>` | ID of the WhatsApp Business Account to create the template on. |

### Post Body

See [Parameters](#parameters-2) for property descriptions.

{
  "allow\_category\_change": <ALLOW\_CATEGORY\_CHANGE>,
  "name": "<NAME>",
  "language": "<LANGUAGE>",
  "category": "<CATEGORY>",
  "components": \[<COMPONENTS>\]
}

### Response

See [Return Type](#return-type).