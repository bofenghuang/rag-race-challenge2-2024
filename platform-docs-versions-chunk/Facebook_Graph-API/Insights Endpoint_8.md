platform: Facebook
topic: Graph-API
subtopic: Insights Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Insights Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/insights


### Page Engagement

The "like" reaction counts include both "like" and "care" reactions.

| Metric Name | Description | Values for \`period\` |
| --- | --- | --- |
| `page_engaged_users*` | The number of people who engaged with your Page. Engagement includes any click. | day, week, days\_28 |
| `page_post_engagements*` | The number of times people have engaged with your posts through reactions, comments, shares and more. | day, week, days\_28 |
| `page_consumptions*` | The number of times people clicked on any of your content. | day, week, days\_28 |
| `page_consumptions_unique*` | The number of people who clicked on any of your content. | day, week, days\_28 |
| `page_consumptions_by_consumption_type` | The number of times people clicked on any of your content, by type. Types include [`link_click`, `other_click`, `photo_view`, and `video_view`](https://www.facebook.com/business/help/787506997938504). | day, week, days\_28 |
| `page_consumptions_by_consumption_type_unique` | The number of people who clicked on any of your content, by type. | day, week, days\_28 |
| `page_places_checkin_total*` | The number of times people checked into a place. | day, week, days\_28 |
| `page_places_checkin_total_unique*` | The number of people who checked into a place. | day, week, days\_28 |
| `page_places_checkin_mobile` | The number of times people checked into a place using mobile phones. | day, week, days\_28 |
| `page_places_checkin_mobile_unique` | The number of people who checked into a place using mobile phones. | day, week, days\_28 |
| `page_places_checkins_by_age_gender` | gender and age of people who checked in at your Place. | day |
| `page_places_checkins_by_locale` | top locales of people who checked into your Place. | day |
| `page_places_checkins_by_country` | top countries of people who checked into your Place. | day |
| `page_negative_feedback` | The number of times people took a negative action (e.g., un-liked or hid a post). | day, week, days\_28 |
| `page_negative_feedback_unique` | The number of people who took a negative action (e.g., un-liked or hid a post). | day, week, days\_28 |
| `page_negative_feedback_by_type` | The number of times people took a negative action broken down by type. (See [possible types](#negative-feedback-type)) | day, week, days\_28 |
| `page_negative_feedback_by_type_unique` | The number of people who took a negative action broken down by type. (See [possible types](#negative-feedback-type)) | day, week, days\_28 |
| `page_positive_feedback_by_type` | The number of times people took a positive action broken down by type. (See [possible types](#positive-feedback-types)) | day, week, days\_28 |
| `page_positive_feedback_by_type_unique` | The number of people who took a positive action broken down by type. (See [possible types](#positive-feedback-types)) | day, week, days\_28 |
| `page_fans_online` | The number of your fans who saw any posts on Facebook on a given day, broken down by hour of day in PST/PDT. | day |
| `page_fans_online_per_day` | The number of your fans who saw any posts on Facebook on a given day. | day |
| `page_fan_adds_by_paid_non_paid_unique` | The number of Accounts Center accounts that liked your Page for the first time, broken down based on whether the Page like was attributed to paid or organic content. This metric is [estimated](https://www.facebook.com/business/help/metrics-labeling). | day |