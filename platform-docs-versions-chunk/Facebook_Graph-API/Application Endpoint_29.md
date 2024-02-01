platform: Facebook
topic: Graph-API
subtopic: Application Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Application Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/application/accounts/

### Requirements

| Type | Requirement |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens/) | [App](https://developers.facebook.com/docs/facebook-login/access-tokens/#apptokens) |
| [Permissions](https://developers.facebook.com/docs/permissions/reference) | None |

### Limitations

At least one test user must be associated with an app. Attempting to perform this operation on an app's sole test user will result in error code `2902`.

### Parameters

| Parameter | Description |
| --- | --- |
| `type`<br><br>enum {TEST\_USERS} | Account type |
| `uid`<br><br>UID | Account UID<br><br>Required |

### Return Type

Struct {

`success`: bool,

}