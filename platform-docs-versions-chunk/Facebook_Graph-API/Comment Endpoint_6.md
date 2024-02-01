platform: Facebook
topic: Graph-API
subtopic: Comment Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Comment Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/comment

### New Page Experience

This API is supported for New Page Experience.

### Requirements

To delete a comment posted by a Page, you will need:

* A Page access token requested by a person who can perform the \`MODERATE\` task on the Page
    
* The `pages_read_engagement` permission
    
* The `pages_manage_engagement` permission
    

To delete a comment posted by a User or another Page, you will need:

* A Page access token requested by a person who can perform the \`MODERATE\` task on the Page
    
* The `pages_manage_engagement` permission
    
* The `pages_read_user_content` permission
    

#### Limitations

Reviews are not Page posts, so comments on reviews can not be removed by a Page.

### Response

If successful:

{
  "success": true
}

Otherwise a relevant error message will be returned.