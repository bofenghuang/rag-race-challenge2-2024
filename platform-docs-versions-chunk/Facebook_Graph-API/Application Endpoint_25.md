platform: Facebook
topic: Graph-API
subtopic: Application Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Application Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/application/accounts/

## Creating

You can make a POST request to `accounts` edge from the following paths:

* [`/{application_id}/accounts`](https://developers.facebook.com/docs/graph-api/reference/application/accounts/)

When posting to this edge, a [TestAccount](https://developers.facebook.com/docs/graph-api/reference/test-account/) will be created.

  

Upon successful creation, a `login_url` and `access_token` will be returned. You can use the login URL to log in as the test user. Login URLs expire once they are used, or after one hour if they are unused. An access token will only be returned if the `installed` parameter was set to `true` at the time of the query.

You can also use this edge to associate an existing test user with a different app by using the `owner_acces_token` parameter.