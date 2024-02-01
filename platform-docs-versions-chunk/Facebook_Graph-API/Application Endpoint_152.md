platform: Facebook
topic: Graph-API
subtopic: Application Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Application Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/app/subscriptions

### Permissions

* An app access token is required to delete subscriptions for that app.
    

### Fields

| Name | Description | Type |
| --- | --- | --- |
| `object` | A specific object type to remove subscriptions for. If this optional field is not included, all subscriptions for this app will be removed. | `enum{user, page, permissions, payments}` |
| `fields` | One or more of the [set of valid fields](https://developers.facebook.com/docs/graph-api/webhooks/) in this `object` to subscribe to. | `string[]` |

### Response

If successful:

{
  "success": true
}

Otherwise a relevant error message will be returned.