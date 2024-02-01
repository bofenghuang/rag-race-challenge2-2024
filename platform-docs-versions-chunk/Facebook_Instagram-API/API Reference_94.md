platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user


### Fields

Public fields can be returned by an edge using field expansion.

| Field Name | Description |
| --- | --- |
| `biography`  <br>Public | Profile bio text. |
| `id`  <br>Public | App-scoped User ID. |
| `ig_id` | Instagram User ID. Used with Legacy Instagram API, now deprecated. Use `id` instead. |
| `followers_count`  <br>Public | Total number of Instagram users following the user. |
| `follows_count` | Total number of Instagram users the user follows. |
| `media_count`  <br>Public | Total number of [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) published on the user. |
| `name` | Profile name. |
| `profile_picture_url` | Profile picture URL. |
| `shopping_product_tag_eligibility` | Returns `true` if the app user has set up an [Instagram Shop](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1187859655048322%2F&h=AT3kvnHBSG0LYl979wHZANBRTb9akLkMVHYaKM9QVLMy20zSG-RV6HmpxCO_w0JeZo0ZbO0yrKOZ3-uZ7FWVsvvmwldG4f05eAv7lFU0ctXPUk-gUucvpZIr4xm1di5Wvmmj9MVJVF88zuic) and is therefore eligible for product tagging, otherwise returns `false`. |
| `username`  <br>Public | Profile username. |
| `website`  <br>Public | Single profile website URL. |