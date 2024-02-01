platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/insights


### Metrics

#### Interaction Metrics

  

| Metric | Period | Timeframe | Breakdown | Metric Type | Description |
| --- | --- | --- | --- | --- | --- |
| `impressions` | `day` | n/a | n/a | `total_value`, `time_series` | The number of times your posts, stories, reels, videos and live videos were on screen, including in ads. |
| `reach` | `day` | n/a | `media_product_type`, `follow_type` | `total_value`, `time_series` | The number of unique accounts that have seen your content, at least once, including in ads. Content includes posts, stories, reels, videos and live videos. Reach is different from impressions, which may include multiple views of your content by the same accounts.<br><br>  <br><br>This metric is estimated and [in development](https://business.facebook.com/business/help/metrics-labeling). |
| `total_interactions` | `day` | n/a | `media_product_type` | `total_value` | The total number of post interactions, story interactions, reels interactions, video interactions and live video interactions, including any interactions on boosted content. |
| `accounts_engaged` | `day` | n/a | n/a | `total_value` | The number of accounts that have interacted with your content, including in ads. Content includes posts, stories, reels, videos and live videos. Interactions can include actions such as likes, saves, comments, shares or replies.<br><br>  <br><br>This metric is estimated and [in development](https://business.facebook.com/business/help/metrics-labeling). |
| `likes` | `day` | n/a | `media_product_type` | `total_value` | The number of likes on your posts, reels, and videos. |
| `comments` | `day` | n/a | `media_product_type` | `total_value` | The number of comments on your posts, reels, videos and live videos.<br><br>  <br><br>This metric is [in development](https://business.facebook.com/business/help/metrics-labeling). |
| `saved` | `day` | n/a | `media_product_type` | `total_value` | The number of saves of your posts, reels, and videos. |
| `shares` | `day` | n/a | `media_product_type` | `total_value` | The number of shares of your posts, stories, reels, videos and live videos. |
| `replies` | `day` | n/a | n/a | `total_value` | The number of replies you received from your story, including text replies and quick reaction replies. |
| `follows_and_unfollows` | `day` | n/a | `follow_type` | `total_value` | The number of accounts that followed you and the number of accounts that unfollowed you or left Instagram in the selected time period.<br><br>  <br><br>Not returned if the IG User has less than 100 followers. |
| `profile_links_taps` | `day` | n/a | `contact_button_type` | `total_value` | The number of taps on your business address, call button, email button and text button. |
| `website_clicks` | `day` | n/a | n/a | `total_value` | The number of times the link to your website was tapped. |
| `profile_views` | `day` | n/a | n/a | `total_value` | The number of times your profile was visited. |

#### Demographic Metrics

  

| Metric | Period | Timeframe | Breakdown | Metric Type | Description |
| --- | --- | --- | --- | --- | --- |
| `engaged_audience_demographics` | `lifetime` | One of:<br><br>  <br><br>`last_14_days`, `last_30_days`, `last_90_days`, `prev_month`, `this_month`, `this_week` | `age`,  <br>`city`,  <br>`country`,  <br>`gender` | `total_value` | The demographic characteristics of the engaged audience, including countries, cities and gender distribution.<br><br>  <br><br>Does not support `since` or `until`. See [Range](#range-2) for more information.<br><br>  <br><br>Not returned if the IG User has less than 100 followers. |
| `reached_audience_demographics` | `lifetime` | One of:<br><br>  <br><br>`last_14_days`, `last_30_days`, `last_90_days`, `prev_month`, `this_month`, `this_week` | `age`,  <br>`city`,  <br>`country`,  <br>`gender` | `total_value` | The demographic characteristics of the reached audience, including countries, cities and gender distribution.<br><br>  <br><br>Does not support `since` or `until`. See [Range](#range-2) for more information.<br><br>  <br><br>Not returned if the IG User has less than 100 followers. |
| `follower_demographics` | `lifetime` | One of:<br><br>  <br><br>`last_14_days`, `last_30_days`, `last_90_days`, `prev_month`, `this_month`, `this_week` | `age`,  <br>`city`,  <br>`country`,  <br>`gender` | `total_value` | The demographic characteristics of followers, including countries, cities and gender distribution.<br><br>  <br><br>Does not support `since` or `until`. See [Range](#range-2) for more information.<br><br>  <br><br>Not returned if the IG User has less than 100 followers. |