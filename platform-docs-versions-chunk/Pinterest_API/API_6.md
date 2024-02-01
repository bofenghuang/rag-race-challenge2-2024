platform: Pinterest
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Pinterest_API/API.md
url: https://developers.pinterest.com/docs/api/v5/

## [](#operation/ad_accounts/get)Get ad account

Get an ad account

ratelimit-category: ads\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

### Responses

**200**

Success

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "id": "string",      * "name": "string",      * "owner": {          * "username": "string",              * "id": "string"                   },      * "country": "US",      * "currency": "USD",      * "permissions": [          * "ADMIN"                   ],      * "created_time": 1451431341,      * "updated_time": 1451431341       }`