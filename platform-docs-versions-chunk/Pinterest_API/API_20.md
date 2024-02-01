platform: Pinterest
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Pinterest_API/API.md
url: https://developers.pinterest.com/docs/api/v5/

## [](#operation/sandbox/delete)Delete ads data for ad account in API Sandbox

Delete an ad account and all the ads data associated with that account. A string message is returned indicating the status of the delete operation.

Note: This endpoint is only allowed in the Pinterest API Sandbox ([https://api-sandbox.pinterest.com/v5](https://api-sandbox.pinterest.com/v5)). Go to [https://developers.pinterest.com/docs/dev-tools/sandbox/](https://developers.pinterest.com/docs/dev-tools/sandbox/) for more information.

ratelimit-category: ads\_write

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |