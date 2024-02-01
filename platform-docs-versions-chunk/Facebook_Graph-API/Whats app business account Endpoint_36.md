platform: Facebook
topic: Graph-API
subtopic: Whats app business account Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Whats app business account Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/message_templates/

## Deleting

You can dissociate a [WhatsAppMessageTemplate](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-hsm/) from a [WhatsAppBusinessAccount](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/) by making a DELETE request to [`/{whats_app_business_account_id}/message_templates`](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/message_templates/).

### Requirements

| Type | Description |
| --- | --- |
| Access Tokens | [User](https://developers.facebook.com/docs/whatsapp/business-management-api/get-started#user-access-tokens) or [System User](https://developers.facebook.com/docs/whatsapp/business-management-api/get-started#system-user-access-tokens) |
| Permissions | [whatsapp\_business\_management](https://developers.facebook.com/docs/permissions/reference/whatsapp_business_management) |

### Request Syntax

DELETE /<WHATSAPP\_BUSINESS\_ACCOUNT\_ID>/message\_templates