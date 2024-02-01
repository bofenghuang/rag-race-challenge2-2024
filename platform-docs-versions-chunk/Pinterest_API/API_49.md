platform: Pinterest
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Pinterest_API/API.md
url: https://developers.pinterest.com/docs/api/v5/

### Response samples

* 200
* 400
* 403
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "audience_size_lower_bound": 100000,      * "audience_size_upper_bound": 150000       }`

## [](#operation/ad_groups/get)Get ad group

Get a specific ad given the ad ID. If your pin is rejected, rejected\_reasons will contain additional information from the Ad Review process. For more information about our policies and rejection reasons see the [Pinterest advertising standards](https://www.pinterest.com/_/_/policy/advertising-guidelines/).

ratelimit-category: ads\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |
| ad\_group\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad group. |