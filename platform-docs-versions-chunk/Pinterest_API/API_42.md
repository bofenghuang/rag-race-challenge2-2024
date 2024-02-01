platform: Pinterest
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Pinterest_API/API.md
url: https://developers.pinterest.com/docs/api/v5/

### Responses

**200**

Success

**400**

Invalid ad account group analytics parameters.

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/ad\_groups/analytics

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ad\_groups/analytics

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`[  * {          * "DATE": "2021-04-01",              * "AD_GROUP_ID": "547602124502",              * "SPEND_IN_DOLLAR": 30,              * "TOTAL_CLICKTHROUGH": 216                   }       ]`