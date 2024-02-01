platform: Facebook
topic: Graph-API
subtopic: Page post Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Page post Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/page-post/

# Page Post

A Post that was published on a Facebook Page.

## Reading

A Post that has been published or is scheduled to be published on a Facebook Page.

### Permissions

The `source` field will not be returned for Page-owned videos unless the User making the request is an admin of the owning Page.

### Limitations

* If a Post has expired, you will no longer be able to view the content using the Graph API.
    
* This endpoint does not return Reels. To get a list of Reels published to your Page, use the [Page VideoReels edge](https://developers.facebook.com/docs/graph-api/reference/page/video_reels).
    

### New Page Experience

This endpoint is supported for [New Page Experience](https://developers.facebook.com/docs/pages/new-pages-experience/).

### Feature Permissions

| Name | Description |
| --- | --- |
| Page Public Content Access | This [feature permission](https://developers.facebook.com/docs/apps/review/feature/) may be required. |