platform: Pinterest
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Pinterest_API/API.md
url: https://developers.pinterest.com/docs/api/v5/


## [](#operation/ad_groups/audience_sizing)Get audience sizing

Get potential audience size for an ad group with given targeting criteria. Potential audience size estimates the number of people you may be able to reach per month with your campaign. It is based on historical advertising data and the targeting criteria you select. It does not guarantee results or take into account factors such as bid, budget, schedule, seasonality or product experiments.

ratelimit-category: ads\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

|     |     |
| --- | --- |
| auto\_targeting\_enabled | boolean<br><br>Default: true<br><br>Enable auto-targeting for ad group. Also known as ["expanded targeting"](https://help.pinterest.com/en/business/article/expanded-targeting). |
| placement\_group | string<br><br>Default: "ALL"<br><br>Enum: "ALL" "SEARCH" "BROWSE" "OTHER"<br><br>[Placement group](https://developers.pinterest.com/docs/redoc/#section/Placement-group). |
| creative\_types | Array of strings Nullable<br><br>Items Enum: "REGULAR" "VIDEO" "SHOPPING" "CAROUSEL" "MAX\_VIDEO" "SHOP\_THE\_PIN" "COLLECTION" "IDEA"<br><br>Pin creative types filter.<br><br>**Note:** SHOP\_THE\_PIN has been deprecated. Please use COLLECTION instead. |
| targeting\_spec | object (TargetingSpec)<br><br>Ad group targeting specification defining the ad group target audience. For example, {"APPTYPE":\["iphone"\], "GENDER":\["male"\], "LOCALE":\["en-US"\], "LOCATION":\["501"\], "AGE\_BUCKET":\["25-34"\]} |
| product\_group\_ids | Array of strings Nullable<br><br>Targeted product group IDs.<br><br>**Note:** This can only be combined with shopping/catalog sales campaigns. For more information, [click here](https://help.pinterest.com/en/business/article/shopping-ads#section-14571). SHOPPING\_RETARGETING must be included in targeting\_spec object or this field will be ignored. |
| keywords | Array of objects Nullable<br><br>Array of keyword objects. If the keywords field is missing, all keywords will be targeted. |