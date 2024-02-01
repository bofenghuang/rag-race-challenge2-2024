platform: Facebook
topic: Graph-API
subtopic: Application Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Application Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/app/subscriptions

### Fields

| Name | Description | Type |
| --- | --- | --- |
| `object` | Indicates the object type that this subscription applies to. | `enum{user, page, permissions, payments}` |
| `callback_url` | The URL that will receive the `POST` request when an update is triggered, and a `GET` request when attempting this publish operation. See our [guide to constructing a callback URL page](https://developers.facebook.com/docs/graph-api/webhooks/#setup). | `string` |
| `fields` | One or more of the [set of valid fields](https://developers.facebook.com/docs/graph-api/webhooks/) in this `object` to subscribe to. | `string[]` |
| `include_values` | Indicates if change notifications should include the new values. | `bool` |
| `verify_token` | An arbitrary string that [can be used to confirm](https://developers.facebook.com/docs/graph-api/webhooks/) to your server that the request is valid. | `string` |