platform: Pinterest
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Pinterest_API/API.md
url: https://developers.pinterest.com/docs/api/v5/


## [](#operation/ad_groups/list)List ad groups

List ad groups based on provided campaign IDs or ad group IDs.(campaign\_ids or ad\_group\_ids).

**Note:**

Provide only campaign\_id or ad\_group\_id. Do not provide both.

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
| entity\_statuses | Array of strings<br><br>Default: \["ACTIVE","PAUSED"\]<br><br>Items Enum: "ACTIVE" "PAUSED" "ARCHIVED"<br><br>Example: entity\_statuses=ACTIVE<br><br>Entity status |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |
| order | string<br><br>Enum: "ASCENDING" "DESCENDING"<br><br>Example: order=ASCENDING<br><br>The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID. Note that higher-value IDs are associated with more-recently added items. |
| bookmark | string<br><br>Cursor used to fetch the next page of items |
| translate\_interests\_to\_names | boolean<br><br>Default: false<br><br>Return interests as text names (if value is true) rather than topic IDs. |