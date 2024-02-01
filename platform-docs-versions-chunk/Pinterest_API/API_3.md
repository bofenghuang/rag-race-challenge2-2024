platform: Pinterest
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Pinterest_API/API.md
url: https://developers.pinterest.com/docs/api/v5/

### Responses

**200**

response

**default**

Unexpected error

get/ad\_accounts

https://api.pinterest.com/v5/ad\_accounts

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "id": "string",                      * "name": "string",                      * "owner": {                          * "username": "string",                              * "id": "string"                                           },                      * "country": "US",                      * "currency": "USD",                      * "permissions": [                          * "ADMIN"                                           ],                      * "created_time": 1451431341,                      * "updated_time": 1451431341                               }                   ],      * "bookmark": "string"       }`