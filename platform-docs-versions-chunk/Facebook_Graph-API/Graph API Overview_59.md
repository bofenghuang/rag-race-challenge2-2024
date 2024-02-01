platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/guides/versioning

### Graph API

Whether core or extended, almost all Graph API endpoints are available through a versioned path. We've a [full guide to using versions with the Graph API](https://developers.facebook.com/docs/graph-api/quickstart#versions) in our [Graph API quickstart guide](https://developers.facebook.com/docs/graph-api/quickstart).

### Dialogs

Versioned paths aren't just true for API endpoints, they're also true for dialogs and social plugins. For example, if you want to generate the Facebook Login dialog for a web app, you can prepend a version number to the endpoint that generates the dialog:

https://www.facebook.com/`v19.0`/dialog/oauth?
  client\_id={app-id}
  &redirect\_uri={redirect-uri}