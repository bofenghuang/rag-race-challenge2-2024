platform: Pinterest
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Pinterest_API/API.md
url: https://developers.pinterest.com/docs/api/v5/

### Responses

**200**

Success

**400**

Invalid ad account ads analytics mmm parameters

**default**

Unexpected error

post/ad\_accounts/{ad\_account\_id}/mmm\_reports

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/mmm\_reports

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`{  * "report_name": "string",      * "start_date": "2020-12-20",      * "end_date": "2020-12-20",      * "granularity": "DAY",      * "level": "CAMPAIGN_TARGETING",      * "targeting_types": [          * "GENDER"                   ],      * "columns": [          * "SPEND_IN_DOLLAR"                   ],      * "countries": [          * "US"                   ]       }`