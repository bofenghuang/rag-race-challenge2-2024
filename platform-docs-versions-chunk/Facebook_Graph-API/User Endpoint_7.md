platform: Facebook
topic: Graph-API
subtopic: User Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/User Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/user/

## Updating

You can update a [User](https://developers.facebook.com/docs/graph-api/reference/user/) by making a POST request to [`/{user_id}`](https://developers.facebook.com/docs/graph-api/reference/user/).

### Parameters

| Parameter | Description |
| --- | --- |
| `emoji_color_pref`<br><br>int64 | emoji color preference. |
| `firstname`<br><br>string | This person's first name |
| `lastname`<br><br>string | This person's last name |
| `local_news_megaphone_dismiss_status`<br><br>enum {YES, NO} | Dismisses local news megaphone |
| `local_news_subscription_status`<br><br>enum {STATUS\_ON, STATUS\_OFF} | Preference for setting local news notifications |
| `name`<br><br>string | Used for test accounts only. Name for this account |
| `password`<br><br>string | Used for test accounts only. Password for this account |