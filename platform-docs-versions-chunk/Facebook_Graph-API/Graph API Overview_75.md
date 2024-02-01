platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/guides/explorer

### Permissions

Whenever you request a User access token, only one permission is given by default, `public_profile`. The Permission dropdown menu allows you to select User Data Permissions, such as `email` and `user_photos`, Events, Groups, and Pages Permissions, such as `manage_pages` and `ads_management`, and Other permissions, such as `instagram_basic` and `publish_video` permissions. This allows the current app User (which is you) to grant the app specific permissions. Only grant permissions that your app actually needs.

If your app is in development, you can grant your app any permission and your queries respect them for data owned by people with a role on your app. If your app is live, however, granting a permission that your app has not been approved for by the [App Review](https://developers.facebook.com/docs/apps/review) process causes your query to fail whenever you submit it.