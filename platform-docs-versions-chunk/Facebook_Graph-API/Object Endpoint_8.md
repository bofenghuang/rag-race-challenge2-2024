platform: Facebook
topic: Graph-API
subtopic: Object Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Object Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/object/comments

## Publishing

Publish new comments to any object.

### New Page Experience

The following objects `/comments` endpoint are supported for New Page Experience:

|     |     |
| --- | --- |
| * Comments<br>* PagePosts<br>* Photo<br>* Post | * PostComment<br>* Video |

### Permissions

* A Page access token requested by a person who can perform the `MODERATE` task on the Page
    
* The `pages_manage_engagement` permission
    

Note, the `can_comment` field on individual [comment objects](https://developers.facebook.com/docs/graph-api/reference/comment/) indicates whether it is possible to reply to that comment.