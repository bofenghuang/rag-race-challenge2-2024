platform: Pinterest
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Pinterest_API/API.md
url: https://developers.pinterest.com/docs/api/v5/

### Responses

**200**

Success

**default**

Unexpected error

post/ad\_accounts

https://api.pinterest.com/v5/ad\_accounts

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`{  * "country": "US",      * "owner_user_id": "383791336903426391",      * "name": "ACME Tools"       }`

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "id": "string",      * "name": "string",      * "owner": {          * "username": "string",              * "id": "string"                   },      * "country": "US",      * "currency": "USD",      * "permissions": [          * "ADMIN"                   ],      * "created_time": 1451431341,      * "updated_time": 1451431341       }`