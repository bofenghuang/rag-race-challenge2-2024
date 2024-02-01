platform: Facebook
topic: Graph-API
subtopic: Insights Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Insights Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/insights


### Page Post Engagement

| Metric Name | Description | Values for \`period\` |
| --- | --- | --- |
| `post_engaged_users*` | The number of people who clicked anywhere in your posts. | lifetime |
| `post_negative_feedback*` | The number of times people took a negative action in your post (e.g. hid it). | lifetime |
| `post_negative_feedback_unique*` | The number of people who took a negative action in your post (e.g., hid it). | lifetime |
| `post_negative_feedback_by_type*` | The number of times people took a negative action in your post broken down by type. | lifetime |
| `post_negative_feedback_by_type_unique*` | The number of people who took a negative action in your post broken down by type. | lifetime |
| `post_engaged_fan` | People who have liked your Page and engaged with your post. | lifetime |
| `post_clicks*` | The number of times people clicked on anywhere in your posts without generating a story. | lifetime |
| `post_clicks_unique*` | The number of people who clicked anywhere in your post without generating a story. | lifetime |
| `post_clicks_by_type*` | The number of times people clicked on anywhere in your posts without generating a story, by consumption type. | lifetime |
| `post_clicks_by_type_unique*` | The number of people who clicked anywhere in your post without generating a story, by consumption type. | lifetime |

#### Negative Feedback Types

Negative feedback types for `page_negative_feedback_by_type` metrics.

| Name | Description |
| --- | --- |
| `hide_clicks` | Hide this story |
| `hide_all_clicks` | Hide all posts from this page |
| `report_spam_clicks` | Report an object as a spam |
| `unlike_page_clicks` | Unlike a page |

#### Positive Feedback Types

Positive feedback types for `page_positive_feedback_by_type` metrics.

| Name | Description |
| --- | --- |
| `answer` | Answer a question |
| `claim` | Claim an offer |
| `comment` | Comment on a story |
| `like` | Like a story |
| `link` | Share a story |
| `other` | Other types, such as checkins |
| `rsvp` | Respond to an event |