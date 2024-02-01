platform: Pinterest
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Pinterest_API/API.md
url: https://developers.pinterest.com/docs/api/v5/

## [](#operation/ads/get)Get ad

Get a specific ad given the ad ID. If your pin is rejected, rejected\_reasons will contain additional information from the Ad Review process. For more information about our policies and rejection reasons see the [Pinterest advertising standards](https://www.pinterest.com/_/_/policy/advertising-guidelines/).

ratelimit-category: ads\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |
| ad\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad. |

### Responses

**200**

Success

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/ads/{ad\_id}

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ads/{ad\_id}