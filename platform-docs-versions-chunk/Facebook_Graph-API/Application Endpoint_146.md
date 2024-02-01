platform: Facebook
topic: Graph-API
subtopic: Application Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Application Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/app/subscriptions

### Permissions

* An app access token is required to return subscriptions for that app.
    

### Fields

| Name | Description | Type |
| --- | --- | --- |
| `object` | Indicates the object type that this subscription applies to. | `enum{user, page, permissions, payments}` |
| `callback_url` | The URL that will receive the `POST` request when an update is triggered. | `string` |
| `fields` | The set of [fields](https://developers.facebook.com/docs/graph-api/webhooks/) in this `object` that are subscribed to. | `string[]` |
| `active` | Indicates whether or not the subscription is active. | `bool` |