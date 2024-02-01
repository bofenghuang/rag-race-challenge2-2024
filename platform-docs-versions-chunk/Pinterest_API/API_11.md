platform: Pinterest
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Pinterest_API/API.md
url: https://developers.pinterest.com/docs/api/v5/


## [](#operation/analytics/create_mmm_report)Create a request for a Marketing Mix Modeling (MMM) report

This creates an asynchronous mmm report based on the given request. It returns a token that you can use to download the report when it is ready. NOTE: An additional limit of 5 queries per minute per advertiser applies to this endpoint while it's in beta release.

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
| report\_name<br><br>required | string (report\_name)<br><br>Name of the Marketing Mix Modeling (MMM) report |
| start\_date<br><br>required | string^(\\d{4})-(\\d{2})-(\\d{2})$<br><br>Metric report start date (UTC). Format: YYYY-MM-DD |
| end\_date<br><br>required | string^(\\d{4})-(\\d{2})-(\\d{2})$<br><br>Metric report end date (UTC). Format: YYYY-MM-DD |
| granularity<br><br>required | string<br><br>Enum: "DAY" "WEEK"<br><br>DAY - metrics are broken down daily.  <br>WEEK - metrics are broken down weekly. |
| level<br><br>required | string<br><br>Enum: "CAMPAIGN\_TARGETING" "AD\_GROUP\_TARGETING"<br><br>Level of the report |
| targeting\_types<br><br>required | Array of strings (targeting\_types) \[ 1 .. 5 \] items<br><br>Items Enum: "APPTYPE" "COUNTRY" "CREATIVE\_TYPE" "GENDER" "LOCATION"<br><br>List of targeting types |
| columns<br><br>required | Array of strings (MMMReportingColumn)<br><br>Items Enum: "SPEND\_IN\_DOLLAR" "SPEND\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_DOLLAR" "ECTR" "CAMPAIGN\_NAME" "TOTAL\_ENGAGEMENT" "EENGAGEMENT\_RATE" "ECPM\_IN\_DOLLAR" "CAMPAIGN\_ID" "ADVERTISER\_ID" "AD\_GROUP\_ID" "AD\_GROUP\_NAME" "CLICKTHROUGH\_1" "IMPRESSION\_1" "CLICKTHROUGH\_2" "IMPRESSION\_2" "TOTAL\_CLICKTHROUGH" "TOTAL\_IMPRESSION" "ADVERTISER\_NAME" "SPEND\_ORDER\_LINE\_PAID\_TYPE"<br><br>Metric and entity columns |
| countries | Array of strings (TargetingAdvertiserCountry)<br><br>Items Enum: "US" "GB" "CA" "IE" "AU" "NZ" "FR" "SE" "IL" "DE" "AT" "IT" "ES" "NL" "BE" "PT" "CH" "HK" "JP" "KR" … 18 more<br><br>A List of countries for filtering |