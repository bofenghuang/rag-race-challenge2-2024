platform: Pinterest
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Pinterest_API/API.md
url: https://developers.pinterest.com/docs/api/v5/

### Responses

**200**

Success

**400**

Invalid ad account ads analytics template parameters.

**default**

Unexpected error

post/ad\_accounts/{ad\_account\_id}/templates/{template\_id}/reports

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/templates/{template\_id}/reports

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "report_status": "FINISHED",      * "token": "string",      * "message": "string"       }`

# [](#tag/ad_groups)ad\_groups

View, create or update ad groups.