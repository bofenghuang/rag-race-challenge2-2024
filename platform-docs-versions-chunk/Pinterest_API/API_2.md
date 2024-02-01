platform: Pinterest
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Pinterest_API/API.md
url: https://developers.pinterest.com/docs/api/v5/

## [](#operation/ad_accounts/list)List ad accounts

Get a list of the ad\_accounts that the "operation user\_account" has access to.

* This includes ad\_accounts they own and ad\_accounts that are owned by others who have granted them [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts).

ratelimit-category: ads\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### query Parameters

|     |     |
| --- | --- |
| bookmark | string<br><br>Cursor used to fetch the next page of items |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |
| include\_shared\_accounts | boolean<br><br>Default: true<br><br>Include shared ad accounts |