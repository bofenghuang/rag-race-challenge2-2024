platform: Pinterest
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Pinterest_API/API.md
url: https://developers.pinterest.com/docs/api/v5/


## [](#operation/analytics/create_report)Create async request for an account analytics report

This returns a token that you can use to download the report when it is ready. Note that this endpoint requires the parameters to be passed as JSON-formatted in the request body. This endpoint does not support URL query parameters.

* The token's user\_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts): Admin, Analyst, Campaign Manager.
* If granularity is not HOUR, the furthest back you can are allowed to pull data is 914 days before the current date in UTC time and the max time range supported is 186 days.
* If granularity is HOUR, the furthest back you can are allowed to pull data is 8 days before the current date in UTC time and the max time range supported is 3 days.
* If level is PRODUCT\_ITEM, the furthest back you can are allowed to pull data is 92 days before the current date in UTC time and the max time range supported is 31 days.
* If level is PRODUCT\_ITEM, ad\_ids and ad\_statuses parameters are not allowed. Any columns related to pin promotion and ad is not allowed either.

ratelimit-category: ads\_analytics

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

|     |     |
| --- | --- |
| start\_date<br><br>required | string^(\\d{4})-(\\d{2})-(\\d{2})$<br><br>Metric report start date (UTC). Format: YYYY-MM-DD |
| end\_date<br><br>required | string^(\\d{4})-(\\d{2})-(\\d{2})$<br><br>Metric report end date (UTC). Format: YYYY-MM-DD |
| granularity<br><br>required | string<br><br>Enum: "TOTAL" "DAY" "HOUR" "WEEK" "MONTH"<br><br>TOTAL - metrics are aggregated over the specified date range.  <br>DAY - metrics are broken down daily.  <br>HOUR - metrics are broken down hourly.  <br>WEEKLY - metrics are broken down weekly.  <br>MONTHLY - metrics are broken down monthly |
| click\_window\_days | integer<br><br>Default: 30<br><br>Enum: 0 1 7 14 30 60<br><br>Number of days to use as the conversion attribution window for a pin click action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days. |
| engagement\_window\_days | integer<br><br>Default: 30<br><br>Enum: 0 1 7 14 30 60<br><br>Number of days to use as the conversion attribution window for an engagement action. Engagements include saves, closeups, link clicks, and carousel card swipes. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days. |
| view\_window\_days | integer<br><br>Default: 1<br><br>Enum: 0 1 7 14 30 60<br><br>Number of days to use as the conversion attribution window for a view action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `1` day. |
| conversion\_report\_time | string<br><br>Default: "TIME\_OF\_AD\_ACTION"<br><br>Enum: "TIME\_OF\_AD\_ACTION" "TIME\_OF\_CONVERSION"<br><br>The date by which the conversion metrics returned from this endpoint will be reported. There are two dates associated with a conversion event: the date that the user interacted with the ad, and the date that the user completed a conversion event. |
| attribution\_types | Array of strings (ConversionReportAttributionType)<br><br>Items Enum: "INDIVIDUAL" "HOUSEHOLD"<br><br>List of types of attribution for the conversion report |
| campaign\_ids | Array of strings \[ 1 .. 500 \] items<br><br>List of campaign ids |
| campaign\_statuses | Array of strings (CampaignSummaryStatus) \[ 1 .. 6 \] items<br><br>Items Enum: "RUNNING" "PAUSED" "NOT\_STARTED" "COMPLETED" "ADVERTISER\_DISABLED" "ARCHIVED" "DRAFT" "DELETED\_DRAFT"<br><br>List of status values for filtering |
| campaign\_objective\_types | Array of strings (ObjectiveType) \[ 1 .. 6 \] items<br><br>Items Enum: "AWARENESS" "CONSIDERATION" "VIDEO\_VIEW" "WEB\_CONVERSION" "CATALOG\_SALES" "WEB\_SESSIONS"<br><br>List of values for filtering. \["WEB\_SESSIONS"\] in BETA. |
| ad\_group\_ids | Array of strings \[ 1 .. 500 \] items<br><br>List of ad group ids |
| ad\_group\_statuses | Array of strings (AdGroupSummaryStatus) \[ 1 .. 6 \] items<br><br>Items Enum: "RUNNING" "PAUSED" "NOT\_STARTED" "COMPLETED" "ADVERTISER\_DISABLED" "ARCHIVED" "DRAFT" "DELETED\_DRAFT"<br><br>List of values for filtering |
| ad\_ids | Array of strings \[ 1 .. 500 \] items<br><br>List of ad ids \[This parameter is no supported for Product Item Level Reports\] |
| ad\_statuses | Array of strings (PinPromotionSummaryStatus) \[ 1 .. 6 \] items<br><br>Items Enum: "APPROVED" "PAUSED" "PENDING" "REJECTED" "ADVERTISER\_DISABLED" "ARCHIVED" "DRAFT" "DELETED\_DRAFT"<br><br>List of values for filtering \[This parameter is not supported for Product Item Level Reports\] |
| product\_group\_ids | Array of strings \[ 1 .. 500 \] items<br><br>List of product group ids |
| product\_group\_statuses | Array of strings (ProductGroupSummaryStatus) \[ 1 .. 6 \] items<br><br>Items Enum: "RUNNING" "PAUSED" "EXCLUDED" "ARCHIVED"<br><br>List of values for filtering |
| product\_item\_ids | Array of strings \[ 1 .. 500 \] items<br><br>List of product item ids |
| targeting\_types | Array of strings (AdsAnalyticsTargetingType) \[ 1 .. 5 \] items<br><br>Items Enum: "KEYWORD" "APPTYPE" "GENDER" "LOCATION" "PLACEMENT" "COUNTRY" "TARGETED\_INTEREST" "PINNER\_INTEREST" "AUDIENCE\_INCLUDE" "GEO" "AGE\_BUCKET" "REGION"<br><br>List of targeting types. Requires `level` to be a value ending in `_TARGETING`. |
| metrics\_filters | Array of objects (AdsAnalyticsMetricsFilter) non-empty<br><br>List of metrics filters |
| columns<br><br>required | Array of strings (ReportingColumnAsync)<br><br>Items Enum: "SPEND\_IN\_MICRO\_DOLLAR" "PAID\_IMPRESSION" "SPEND\_IN\_DOLLAR" "CPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_DOLLAR" "CTR" "ECTR" "OUTBOUND\_CTR" "COST\_PER\_OUTBOUND\_CLICK" "CAMPAIGN\_NAME" "CAMPAIGN\_STATUS" "PIN\_PROMOTION\_STATUS" "AD\_STATUS" "PIN\_ID" "TOTAL\_ENGAGEMENT" "ENGAGEMENT\_1" "ENGAGEMENT\_2" "ECPE\_IN\_DOLLAR" "ENGAGEMENT\_RATE" … 541 more<br><br>Metric and entity columns. Pin promotion and ad related columns are not supported for the Product Item level reports. |
| level<br><br>required | string<br><br>Enum: "ADVERTISER" "ADVERTISER\_TARGETING" "CAMPAIGN" "CAMPAIGN\_TARGETING" "AD\_GROUP" "AD\_GROUP\_TARGETING" "PIN\_PROMOTION" "PIN\_PROMOTION\_TARGETING" "KEYWORD" "PRODUCT\_GROUP" "PRODUCT\_GROUP\_TARGETING" "PRODUCT\_ITEM"<br><br>Level of the report |
| report\_format | string<br><br>Default: "JSON"<br><br>Enum: "JSON" "CSV"<br><br>Specification for formatting the report data. Reports in JSON will not zero-fill metrics, whereas reports in CSV will. Both report formats will omit rows where all the columns are equal to 0. |