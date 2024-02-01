platform: Pinterest
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Pinterest_API/API.md
url: https://developers.pinterest.com/docs/api/v5/


### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "id": "6739202847590",                      * "ad_account_id": "547664674848",                      * "ad_account_ids": [                          * "547664674848"                                           ],                      * "user_id": "784762938748396",                      * "name": "Week over week spend",                      * "report_start_relative_days_in_past": 7,                      * "report_end_relative_days_in_past": 7,                      * "date_range": {                          * "dynamic_date_range": {                                  * "range": "YEAR_TO_DATE",                                      * "type": "dynamic"                                                       },                              * "relative_date_range": {                                  * "end_days_in_past": 7,                                      * "type": "relative",                                      * "start_days_in_past": 14                                                       },                              * "absolute_date_range": {                                  * "end_date": 6.027456183070403,                                      * "type": "absolute",                                      * "start_date": 0.8008281904610115                                                       }                                           },                      * "report_level": "CAMPAIGN",                      * "report_format": "JSON",                      * "columns": [                          * "SPEND_IN_DOLLAR"                                           ],                      * "granularity": "TOTAL",                      * "view_window_days": 7,                      * "click_window_days": 7,                      * "engagement_window_days": 7,                      * "conversion_report_time_type": "TIME_OF_AD_ACTION",                      * "filters_json": "[{\"field\": \"SPEND_IN_DOLLAR\", \"operator\": \"=\", \"value\": 100}]",                      * "is_owned_by_user": true,                      * "is_scheduled": true,                      * "creation_source": "ADS_MANAGER_REPORT_BUILDER",                      * "is_deleted": false,                      * "updated_time": 1432744744,                      * "custom_column_ids": [                          * "1597252063"                                           ],                      * "type": "BULK",                      * "ingestion_sources": [                          * "CONVERSIONS_API"                                           ]                               }                   ],      * "bookmark": "string"       }`