platform: Facebook
topic: Graph-API
subtopic: Post Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Post Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/post/

### Permissions

* A page access token can read all posts posted to or posted by that Page.
    
* A page access token with the [`pages_manage_posts` permission](https://developers.facebook.com/docs/pages/overview/permissions-features) and [Page Public Content Access Feature](https://developers.facebook.com/docs/apps/review/feature/#reference-PAGES_ACCESS) are required to read publicly shared Page posts. The person requesting the access token must be an admin of the Page.
    
* A user access token can read any post your application created on behalf of that user.
    
* A user's post can be read if the owner has granted the `user_posts` permission.
    
* A user access token may read a post that user is tagged in if they have granted the `user_posts` permission. However, in some cases the post's owner's privacy settings may not allow your application to access it.