platform: Facebook
topic: Graph-API
subtopic: Page Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Page Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/page/


### Error Codes

| Error | Description |
| --- | --- |
| 413 | Invalid password |
| 200 | Permissions error |
| 3982 | You do not have sufficient permissions to import this asset into the given Business Manager. |
| 3944 | Your Business Manager already has access to this object. |
| 100 | Invalid parameter |
| 457 | The session has an invalid origin |
| 42000 | This Page can't be added because it's already linked to an Instagram business profile. To add this Page to Business Manager, go to Instagram and convert to a personal account or change the Page linked to your business profile. |
| 3977 | To claim a Page in Business Manager, you must already be an Admin of the Page. |
| 3948 | Please assign someone as a manager to this Page before removing it from your Business Manager. |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |

You can make a POST request to `feed` edge from the following paths:

* [`/{page_id}/feed`](https://developers.facebook.com/docs/graph-api/reference/page/feed/)

When posting to this edge, a [Page](https://developers.facebook.com/docs/graph-api/reference/page/) will be created.