platform: Facebook
topic: Graph-API
subtopic: Application Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Application Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/application/accounts/


### Parameters

| Parameter | Description |
| --- | --- |
| `installed`<br><br>boolean | Automatically installs the app for the test user once it is created or associated |
| `minor`<br><br>boolean | Is this test user a minor |
| `name`<br><br>string | The name for the test user. When left blank, a random name will be automatically generated |
| `owner_access_token`<br><br>string | When associating existing test users with other apps, this is the app access token of any app that is already associated with the test user. The `{app-id}` in the publishing request in this case should be the app that will is the target to associate with the test user. The API request should also be signed with the app access token of that target app. Required when associating test users, but should not be used when creating new test users |
| `permissions`<br><br>List<Permission> | Default value: `Set`<br><br>List of permissions that are automatically granted for the app when it is created or associated |
| `type`<br><br>enum{test-users} | Type |
| `uid`<br><br>int | ID of an existing test user to associate with another app. Required when associating test users, but should not be used when creating new test users |