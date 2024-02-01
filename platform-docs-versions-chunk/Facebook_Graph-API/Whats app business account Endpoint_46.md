platform: Facebook
topic: Graph-API
subtopic: Whats app business account Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Whats app business account Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/subscribed_apps/

## Creating

You can make a POST request to `subscribed_apps` edge from the following paths:

* [`/{whats_app_business_account_id}/subscribed_apps`](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/subscribed_apps/)

When posting to this edge, a [WhatsAppApplication](https://developers.facebook.com/docs/graph-api/reference/whats-app-application/) will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `override_callback_uri`<br><br>URI | **Required if overriding the callback URL.**<br><br>  <br>New callback URL. See [Overriding the Callback URL](https://developers.facebook.com/docs/whatsapp/embedded-signup/webhooks#overriding-the-callback-url). |
| `verify_token`<br><br>string | **Required if overriding the callback URL.**<br><br>  <br>Callback verification token. See [Overriding the Callback URL](https://developers.facebook.com/docs/whatsapp/embedded-signup/webhooks#overriding-the-callback-url). |