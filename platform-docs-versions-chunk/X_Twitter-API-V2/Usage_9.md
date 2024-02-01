platform: X
topic: Twitter-API-V2
subtopic: Usage
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Usage.md
url: https://developer.twitter.com/en/docs/twitter-api/usage/tweets/api-reference/get-usage-tweets


### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `project_id` | string | The unique identifier for this project. |
| `project_cap` | string | The total number of Tweets that can be read with this project per month. |
| `project_usage` | string | The total number of Tweets that have been read with this project in the current billing cycle. |
| `cap_reset_day` | integer | The day of the month when the Tweet cap is reset. |
| `daily_project_usage` | object | This object and its fields contain daily usage breakdown for a project. |
| `daily_project_usage.project_id` | string | The unique identifier for this project. |
| `daily_project_usage.usage` | array | This array contains the usage information. |
| `daily_project_usage.usage.date` | date (ISO 8601) | The date for which the usage is returned. |
| `daily_project_usage.usage.usage` | string | The project usage for a day. |
| `daily_client_app_usage` | array | This object and its fields contain daily usage breakdown per client app. |
| `daily_client_app_usage.usage` | array | This array contains the usage information. |
| `daily_client_app_usage.usage.date` | date (ISO 8601) | The date for which the usage is returned. |
| `daily_client_app_usage.usage.usage` | string | The project usage for a day. |