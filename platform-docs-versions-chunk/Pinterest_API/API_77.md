platform: Pinterest
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Pinterest_API/API.md
url: https://developers.pinterest.com/docs/api/v5/


## [](#operation/audience_insights/get)Get audience insights

Get Audience Insights for an ad account. The response will return insights for 3 types of audiences: the ad account's engaged audience on Pinterest, the ad account's total audience on Pinterest and Pinterest's total audience.

[Learn more about Audience Insights](https://help.pinterest.com/en/business/article/audience-insights).

ratelimit-category: ads\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| audience\_insight\_type<br><br>required | string (AudienceInsightType)<br><br>Default: "YOUR\_TOTAL\_AUDIENCE"<br><br>Enum: "YOUR\_TOTAL\_AUDIENCE" "YOUR\_ENGAGED\_AUDIENCE" "PINTEREST\_TOTAL\_AUDIENCE"<br><br>Example: audience\_insight\_type=YOUR\_TOTAL\_AUDIENCE<br><br>Type of audience insights. |