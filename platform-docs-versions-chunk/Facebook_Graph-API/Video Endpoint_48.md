platform: Facebook
topic: Graph-API
subtopic: Video Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Video Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/video/video_insights/

# Video Insights

## Reading

Get aggregated insight metrics for videos on a [Page](https://developers.facebook.com/docs/graph-api/reference/page). You can get metrics for Videos, Reels, and Ad Breaks. For the full list of metrics, see [Available Metrics](#metrics).

### Requirements

* The [pages\_manage\_engagement](https://developers.facebook.com/docs/permissions/reference/pages_manage_engagement) Permission.
* The [read\_insights](https://developers.facebook.com/docs/permissions/reference/read_insights) Permission.
* A Page access token requested by a person who is able to perform `ANALYZE` [Tasks](https://developers.facebook.com/docs/pages/overview#tasks) on a Page.
* Only Page admins can query earnings insights by using the API. Learn about [setting up user roles for a Page.](https://www.facebook.com/help/187316341316631)