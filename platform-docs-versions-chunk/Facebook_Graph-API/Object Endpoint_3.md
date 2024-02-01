platform: Facebook
topic: Graph-API
subtopic: Object Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Object Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/object/comments

## Reading

Returns a comment on an object.

The `id` field for the `/PAGEPOST-ID/comments` endpoint will no longer be returned for apps using the [Page Public Content Access feature](https://developers.facebook.com/docs/pages/overview/permissions-features#features). To access the comment IDs for a Page post you must be able to perform the [MODERATE task](https://developers.facebook.com/docs/pages/overview/permissions-features#tasks) on the Page being queried. This change is in effect for v11.0+ and will be implement for all versions on September, 7, 2021.

### New Page Experience

The following objects `/comments` endpoint are supported for New Page Experience:

|     |     |
| --- | --- |
| * Album<br>* Comment<br>* Link<br>* Page | * PagePost<br>* Photo<br>* Post<br>* PostComment |

### Permissions

* The same permissions required to view the parent object are required to view comments on that object.