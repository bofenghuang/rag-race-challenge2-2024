platform: Pinterest
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Pinterest_API/API.md
url: https://developers.pinterest.com/docs/api/v5/


## [](#operation/templates/list)List templates

Gets all Templates associated with an ad account ID.

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
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |
| order | string<br><br>Enum: "ASCENDING" "DESCENDING"<br><br>Example: order=ASCENDING<br><br>The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID. Note that higher-value IDs are associated with more-recently added items. |
| bookmark | string<br><br>Cursor used to fetch the next page of items |