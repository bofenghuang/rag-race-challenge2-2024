platform: Pinterest
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Pinterest_API/API.md
url: https://developers.pinterest.com/docs/api/v5/


### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`{  * "start_date": "2020-12-20",      * "end_date": "2020-12-20",      * "granularity": "TOTAL",      * "click_window_days": 0,      * "engagement_window_days": 0,      * "view_window_days": 0,      * "conversion_report_time": "TIME_OF_AD_ACTION",      * "attribution_types": [          * "INDIVIDUAL"                   ],      * "campaign_ids": [          * "12345678"                   ],      * "campaign_statuses": [          * "RUNNING",              * "PAUSED"                   ],      * "campaign_objective_types": [          * "AWARENESS",              * "VIDEO_VIEW"                   ],      * "ad_group_ids": [          * "12345678"                   ],      * "ad_group_statuses": [          * "RUNNING",              * "PAUSED"                   ],      * "ad_ids": [          * "12345678"                   ],      * "ad_statuses": [          * "APPROVED",              * "PAUSED"                   ],      * "product_group_ids": [          * "12345678"                   ],      * "product_group_statuses": [          * "RUNNING",              * "PAUSED"                   ],      * "product_item_ids": [          * "12345678"                   ],      * "targeting_types": [          * "APPTYPE"                   ],      * "metrics_filters": [          * {                  * "field": "SPEND_IN_DOLLAR",                      * "operator": "LESS_THAN",                      * "values": [                          * 0                                           ]                               }                   ],      * "columns": [          * "SPEND_IN_MICRO_DOLLAR"                   ],      * "level": "CAMPAIGN",      * "report_format": "JSON"       }`