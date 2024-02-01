platform: Pinterest
topic: API
subtopic: API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Pinterest_API/API.md
url: https://developers.pinterest.com/docs/api/v5/

# Pinterest REST API (5.12.0)

URL: [https://developers.pinterest.com/](https://developers.pinterest.com/) License: [MIT](https://spdx.org/licenses/MIT) [Terms of Service](https://developers.pinterest.com/terms/)

Pinterest's REST API

# [](#tag/ad_accounts)ad\_accounts

View analytical information about advertising.

Note: If the current operation\_user\_account (defined by the access token) has access to another user's Ad Accounts via [Pinterest Business Access](https://developers.pinterest.com/docs/reference/business-access/), you can modify your request to use the current operation\_user\_account's permissions to those Ad Accounts by including the ad\_account\_id in the path parameters for the request (e.g. .../?ad\_account\_id=12345&...).