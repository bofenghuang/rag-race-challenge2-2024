platform: Pinterest
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Pinterest_API/API.md
url: https://developers.pinterest.com/docs/api/v5/


## [](#operation/ads/list)List ads

List ads that meet the filters provided:

* Listed campaign ids or ad group ids or ad ids
* Listed entity statuses
    
    If no filter is provided, all ads in the ad account are returned.
    
    **Note:**
    
    Provide only campaign\_id or ad\_group\_id or ad\_id. Do not provide more than one type.
    
    Review status is provided for each ad; if review\_status is REJECTED, the rejected\_reasons field will contain additional information. For more, see [Pinterest advertising standards](https://policy.pinterest.com/en/advertising-guidelines).
    

ratelimit-category: ads\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| campaign\_ids | Array of strings \[ 1 .. 100 \] items<br><br>List of Campaign Ids to use to filter the results. |
| ad\_group\_ids | Array of strings \[ 1 .. 100 \] items<br><br>List of Ad group Ids to use to filter the results. |
| ad\_ids | Array of strings \[ 1 .. 100 \] items<br><br>List of Ad Ids to use to filter the results. |
| entity\_statuses | Array of strings<br><br>Default: \["ACTIVE","PAUSED"\]<br><br>Items Enum: "ACTIVE" "PAUSED" "ARCHIVED"<br><br>Example: entity\_statuses=ACTIVE<br><br>Entity status |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |
| order | string<br><br>Enum: "ASCENDING" "DESCENDING"<br><br>Example: order=ASCENDING<br><br>The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID. Note that higher-value IDs are associated with more-recently added items. |
| bookmark | string<br><br>Cursor used to fetch the next page of items |