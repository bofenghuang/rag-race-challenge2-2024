platform: Facebook
topic: Graph-API
subtopic: Whats app business account Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Whats app business account Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/phone_numbers/

### Requirements

| Type | Description |
| --- | --- |
| Access Tokens | [User](https://developers.facebook.com/docs/whatsapp/business-management-api/get-started#user-access-tokens) or [System User](https://developers.facebook.com/docs/whatsapp/business-management-api/get-started#system-user-access-tokens) |
| Permissions | [whatsapp\_business\_management](https://developers.facebook.com/docs/permissions/reference/whatsapp_business_management)  <br>[whatsapp\_business\_messaging](https://developers.facebook.com/docs/permissions/reference/whatsapp_business_messaging) |

### Request Syntax

GET https://graph.facebook.com/<API\_VERSION>/<WABA\_ID>/phone\_numbers

### Response

A list of [WhatsApp Business Phone Number](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account-to-number-current-status/) nodes and their default fields.

### Sample Request

curl \\
'https://graph.facebook.com/v15.0/102289599326934/phone\_numbers' \\
-H 'Authorization: Bearer EAAJi...'