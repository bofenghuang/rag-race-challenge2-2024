platform: Facebook
topic: Graph-API
subtopic: Test user Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Test user Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/test-user

### Permissions

* An app access token is required to update these fields for any test users associated with that app.
    

### Fields

| Name | Description | Type |
| --- | --- | --- |
| `name` | New name for the test user. | `string` |
| `password` | A new password for the test user. | `string` |

### Response

If update is successful, `true`, otherwise an error message.