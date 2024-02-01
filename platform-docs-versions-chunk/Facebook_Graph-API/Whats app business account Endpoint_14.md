platform: Facebook
topic: Graph-API
subtopic: Whats app business account Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Whats app business account Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/assigned_users/

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |

## Creating

You can't perform this operation on this endpoint.

## Updating

You can update a [WhatsAppBusinessAccount](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/) by making a POST request to [`/{whats_app_business_account_id}/assigned_users`](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/assigned_users/).

### Parameters

| Parameter | Description |
| --- | --- |
| `tasks`<br><br>array<enum {MANAGE, DEVELOP, MANAGE\_TEMPLATES, MANAGE\_PHONE, VIEW\_COST, MANAGE\_EXTENSIONS, VIEW\_PHONE\_ASSETS, MANAGE\_PHONE\_ASSETS, VIEW\_TEMPLATES}> | Permissions on WhatsApp Business Account<br><br>Required |
| `user`<br><br>UID | Business user ID<br><br>Required |