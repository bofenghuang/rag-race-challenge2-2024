platform: Facebook
topic: Graph-API
subtopic: Permissions Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Permissions Reference.md
url: https://developers.facebook.com/docs/permissions


## Permission Dependencies

To use certain permissions when your app goes live, your app must also be approved for additional permissions. These dependent permissions must have been approved either during the same app review submission or a in previous submission.

| Permission | Dependent on |
| --- | --- |
| `ads_management` | `pages_read_engagement`<br><br>  <br><br>`pages_show_list` |
| `instagram_basic` | `pages_read_engagement`<br><br>  <br><br>`pages_show_list` |
| `leads_retrieval` | `pages_manage_ads`<br><br>  <br><br>`pages_read_engagement`<br><br>  <br><br>`pages_show_list` |
| `pages_manage_ads` | `pages_show_list` |
| `pages_manage_engagement` | `pages_read_user_content`<br><br>  <br><br>`pages_show_list` |
| `pages_manage_metadata` | `pages_show_list` |
| `pages_manage_posts` | `pages_read_engagement`<br><br>  <br><br>`pages_show_list` |
| `pages_messaging` | `pages_manage_metadata`<br><br>  <br><br>`pages_show_list` |
| `pages_read_engagement` | `pages_show_list` |
| `pages_read_user_content` | `pages_show_list` |