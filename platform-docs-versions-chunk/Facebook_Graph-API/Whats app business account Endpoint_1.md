platform: Facebook
topic: Graph-API
subtopic: Whats app business account Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Whats app business account Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/

# WhatsApp Business Account

Represents a specific [WhatsApp Business Account (WABA)](https://www.facebook.com/business/help/1499554293524119). Make the API call to the WABA ID.

  

To find the ID of a WhatsApp Business Account, go to [**Business Manager**](https://business.facebook.com/) > **Business Settings** > **Accounts** > **WhatsApp Business Accounts**. Find the account you want to use and click on it. A panel opens, with information about the account, including the ID.

  

For more information on how to use the API, see [WhatsApp Business Management API](https://developers.facebook.com/docs/whatsapp/business-account-management-api).

The following API calls are subject to [Business Use Case Rate Limits](https://developers.facebook.com/docs/graph-api/overview/rate-limiting/#wa-biz-api):

* `GET`, `POST`, and `DELETE` calls to `/{whats-app-business-account-id}/assigned_users`
* `GET` calls to `/{whats-app-business-account-id}`