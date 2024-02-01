platform: Facebook
topic: Graph-API
subtopic: User Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/User Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/user/scores

### Permissions

As of April 24,2018, the `pubish_actions` permission has been removed. Please see the [Breaking Changes Changelog](https://developers.facebook.com/docs/graph-api/changelog/breaking-changes#login-4-24) for more details.

The **Scores API** is available only for apps that are categorized as Games and have already been granted the `publish_actions` permission in the past.

Please note that `publish_actions` will not be granted for new apps with the sole purpose of accessing these APIs.

* A user access token with `publish_actions` permission can be used to delete scores (from this app) for that person.
    
* An app access token can be used if `publish_actions` permission was previously granted.
    

### Fields

No fields are required to delete.

### Response

If successful:

{
  "success": true
}

Otherwise a relevant error message will be returned.