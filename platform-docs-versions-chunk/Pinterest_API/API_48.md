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

`{  * "auto_targeting_enabled": true,      * "placement_group": "ALL",      * "creative_types": [          * "REGULAR"                   ],      * "targeting_spec": {          * "AGE_BUCKET": [                  * "35-44",                      * "50-54"                               ],              * "APPTYPE": [                  * "ipad",                      * "iphone"                               ],              * "AUDIENCE_EXCLUDE": [                  * "string"                               ],              * "AUDIENCE_INCLUDE'": [                  * "string"                               ],              * "GENDER": [                  * "unknown"                               ],              * "GEO": [                  * "string"                               ],              * "INTEREST": [                  * "string"                               ],              * "LOCALE": [                  * "string"                               ],              * "LOCATION": [                  * "string"                               ],              * "SHOPPING_RETARGETING": [                  * {                          * "lookback_window": 30,                              * "exclusion_window": 14,                              * "tag_types": [                                  * 0,                                      * 6                                                       ]                                           }                               ],              * "TARGETING_STRATEGY": [                  * "CHOOSE_YOUR_OWN"                               ]                   },      * "product_group_ids": [          * "23423422123"                   ],      * "keywords": [          * {                  * "match_type": "BROAD",                      * "value": "string"                               }                   ]       }`