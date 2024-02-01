platform: Pinterest
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Pinterest_API/API.md
url: https://developers.pinterest.com/docs/api/v5/

## [](#operation/analytics/get_mmm_report)Get advertiser Marketing Mix Modeling (MMM) report.

Get an mmm report for an ad account. This returns a URL to an mmm metrics report given a token returned from the create mmm report endpoint.

ratelimit-category: ads\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| token<br><br>required | string<br><br>Token returned from the post request creation call |

### Responses

**200**

Success

**400**

Invalid ad account ads analytics parameters.

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/mmm\_reports

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/mmm\_reports