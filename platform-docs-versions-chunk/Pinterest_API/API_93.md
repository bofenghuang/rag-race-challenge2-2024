platform: Pinterest
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Pinterest_API/API.md
url: https://developers.pinterest.com/docs/api/v5/

## [](#operation/audiences/get)Get audience

Get a specific audience given the audience ID.

ratelimit-category: ads\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |
| audience\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an audience |

### Responses

**200**

Success

**404**

Audience not found.

**default**

Unexpected error.

get/ad\_accounts/{ad\_account\_id}/audiences/{audience\_id}

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/audiences/{audience\_id}