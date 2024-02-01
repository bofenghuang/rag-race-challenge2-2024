platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/overview/rate-limiting


### WhatsApp Business Management API

Requests made by your app to the [WhatsApp Business Management API](https://developers.facebook.com/docs/whatsapp/business-management-api) are counted against your app’s count. An app’s call count is the number of calls it can make during a rolling one hour. For the following WhatsApp Business Management API, your app can make 200 calls per hour, per app, per WhatsApp Business Account (WABA) by default. For active WABAs with at least one registered phone number, your app can make 5000 calls per hour, per app, per active WABA.

| Type of Call | Endpoint |
| --- | --- |
| `GET` | `/{whatsapp-business-account-id}` |
| `GET`, `POST`, and `DELETE` | `/{whatsapp-business-account-id}/assigned_users` |
| `GET` | `/{whatsapp-business-account-id}/phone_numbers` |
| `GET`, `POST`, and `DELETE` | `/{whatsapp-business-account-id}/message_templates` |
| `GET`, `POST`, and `DELETE` | `/{whatsapp-business-account-id}/subscribed_apps` |
| `GET` | `/{whatsapp-business-account-to-number-current-status-id}` |

For the following [Credit Line APIs](https://developers.facebook.com/docs/whatsapp/embedded-signup/manage-accounts/share-and-revoke-credit-lines), your app can make 5000 calls per hour, per app.

| Type of Call | Endpoint |
| --- | --- |
| `GET` | `/{business-id}/extendedcredits` |
| `POST` | `/{extended-credit-id}/whatsapp_credit_sharing_and_attach` |
| `GET` and `DELETE` | `/{allocation-config-id}` |
| `GET` | `/{extended-credit-id}/owning_credit_allocation_configs` |

To avoid hitting rate limits, we recommend using [webhooks](https://developers.facebook.com/docs/graph-api/webhooks/getting-started/webhooks-for-whatsapp#setup) to keep track of status updates for message templates, phone numbers, and WABAs.  
  
For more information on how to get your current rate usage, see [Headers](https://developers.facebook.com/docs/graph-api/overview/rate-limiting/#headers).