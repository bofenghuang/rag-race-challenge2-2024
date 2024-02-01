platform: Facebook
topic: Graph-API
subtopic: Application Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Application Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/app/subscriptions

### Limitations

* [Webhooks for Instagram](https://developers.facebook.com/docs/instagram-api/guides/webhooks) is not supported. Instagram webhooks must be configured using the App Dashboard.
* [Webhooks for WhatsApp](https://developers.facebook.com/docs/graph-api/webhooks/getting-started/webhooks-for-whatsapp) is not supported. WhatsApp webhooks must be configured using the App Dashboard.

### Permissions

* An app access token is required to add new subscriptions for that app.
    
* Subscriptions for the object type `user` will only be valid for users who have installed the app.
    
* Subscriptions for the object type `page` will only be valid for Pages that have installed the app. You can install the app for a Page using the [/{page-id}/subscribed\_apps edge](https://developers.facebook.com/docs/graph-api/reference/page/subscribed_apps).
    
* The app used to subscribe should be [set up to receive Webhooks updates](https://developers.facebook.com/docs/graph-api/webhooks/).