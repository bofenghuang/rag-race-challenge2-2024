platform: Pinterest
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Pinterest_API/API.md
url: https://developers.pinterest.com/docs/api/v5/


## [](#operation/analytics/create_template_report)Create async request for an analytics report using a template

This takes a template ID and an optional custom timeframe and constructs an asynchronous report based on the template. It returns a token that you can use to download the report when it is ready.

ratelimit-category: ads\_analytics

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |
| template\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of a template. |

##### query Parameters

|     |     |
| --- | --- |
| start\_date | string <date><br><br>Metric report start date (UTC). Format: YYYY-MM-DD. Cannot be more than 2.5 years back from today. |
| end\_date | string <date><br><br>Metric report end date (UTC). Format: YYYY-MM-DD. Cannot be more than 2.5 years past start date. |
| granularity | string (Granularity)<br><br>Enum: "TOTAL" "DAY" "HOUR" "WEEK" "MONTH"<br><br>Example: granularity=DAY<br><br>TOTAL - metrics are aggregated over the specified date range.  <br>DAY - metrics are broken down daily.  <br>HOUR - metrics are broken down hourly.  <br>WEEKLY - metrics are broken down weekly.  <br>MONTHLY - metrics are broken down monthly |