platform: Facebook
topic: Graph-API
subtopic: Insights Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Insights Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/insights


### Page Content

Most of the metrics below can be retrieved using `post_activity_by_action_type`, `post_clicks_by_type`, and `page_consumptions_by_consumption_type`.

| Metric Name | Description | Values for \`period\` |
| --- | --- | --- |
| `page_tab_views_login_top_unique` | The number of users logged in to Facebook who saw tabs on your Page. (See [possible types](#tab-types)) | day, week |
| `page_tab_views_login_top` | The number of times users logged into Facebook saw tabs on your Page. (See [possible types](#tab-types)) | day, week |
| `page_tab_views_logout_top` | The number of times users not logged in to Facebook saw tabs on your Page. (See [possible types](#tab-types)) | day |

#### Tab Types

Tab types for Page content metrics.

| Name | Description |
| --- | --- |
| `allactivity` | Administrative tab |
| `app` | Custom created tab |
| `info` | About tab view |
| `insights` | Insights tab |
| `likes` | Likes tab |
| `locations` | Map tab |
| `photos` | Photos tab |
| `photos_albums` | Photos tab |
| `photos_stream` | Photos tab |
| `profile` | Pages timeline |
| `profile_info` | Info tab |
| `profile_likes` | Likes tab |
| `profile_photos` | Photos tab |
| `timeline` | Pages timeline |
| `events` | Events tab |
| `videos` | Videos tab |
| `wall` | Timeline |