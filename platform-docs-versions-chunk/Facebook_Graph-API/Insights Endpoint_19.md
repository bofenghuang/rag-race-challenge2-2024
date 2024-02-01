platform: Facebook
topic: Graph-API
subtopic: Insights Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Insights Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/insights


### Stories

Page and Post Stories and "People talking about this".

| Metric Name | Description | Values for \`period\` |
| --- | --- | --- |
| `page_content_activity_by_action_type_unique` | The number of people talking about your Page's stories, by Page story type. (See [possible types](#page-story-types)) | day, week, days\_28 |
| `page_content_activity_by_age_gender_unique` | The number of People Talking About the Page by user age and gender. This number is an estimate. | day, week, days\_28 |
| `page_content_activity_by_city_unique` | The number of People Talking About the Page by user city. | day, week, days\_28 |
| `page_content_activity_by_country_unique` | The number of people, aggregated per country, that are talking about your Page. Only the 45 countries with the most people talking about your page are included. | day, week, days\_28 |
| `page_content_activity_by_locale_unique` | The number of People Talking About the Page by user language. | day, week, days\_28 |
| `page_content_activity` | The number of stories created about your Page (Stories). | day, week, days\_28 |
| `page_content_activity_by_action_type` | The number of stories about your Page's stories, by Page story type. (See [possible types](#page-story-types)) | day, week, days\_28 |
| `post_activity*` | The number of stories generated about your Page post ('Stories'). | lifetime |
| `post_activity_unique*` | The number of people who created a story about your Page post ('People Talking About This' / PTAT). | lifetime |
| `post_activity_by_action_type*` | The number of stories created about your Page post, by action type. | lifetime |
| `post_activity_by_action_type_unique*` | The number of people who created a story about your Page post, by action type. | lifetime |

#### Page Story Types

Page story types for `page_content_activity_by_action_type_unique` and `page_content_activity_by_action_type`.

| Name | Description |
| --- | --- |
| `checkin` | Page checkins |
| `coupon` | Offer claims |
| `event` | RSVPing to event |
| `fan` | Page likes |
| `mention` | Page mentions |
| `page post` | Posts by a Page |
| `question` | Question answers |
| `user post` | Posts by people on a Page |
| `other` | Other types |