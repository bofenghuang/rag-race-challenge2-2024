platform: Facebook
topic: Graph-API
subtopic: Test user Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Test user Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/test-user

### Permissions

* An app access token for an associated app or the test user's own access token must be used to delete that test user.
    
* The test user must have been disassociated from all but a single app. You can disassociate test users using the [`/{app-id}/accounts/test-users` edge](https://developers.facebook.com/docs/graph-api/reference/app/accounts/test-users#delete).
    

### Fields

No fields are required to delete.

### Response

If delete is successful, `true`, otherwise an error message.

## Edges

| Name | Description |
| --- | --- |
| [`/friends`](https://developers.facebook.com/docs/graph-api/reference/test-user/friends) | The friends of the test user - this edge can be used to friend two test users. |

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)