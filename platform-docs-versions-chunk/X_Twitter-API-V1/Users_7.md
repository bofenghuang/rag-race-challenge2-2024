platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/manage-account-settings/api-reference/get-account-verify_credentials

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |
| --- | --- | --- | --- |
| Name | Required | Description | Example |
| include\_entities | optional | The _entities_ node will not be included when set to _false_ . | _false_ |
| skip\_status | optional | When set to either _true_ , _t_ or _1_ statuses will not be included in the returned user object. | _true_ |
| include\_email | optional | When set to _true_ email will be returned in the user objects as a string. If the user does not have an email address on their account, or if the email address is not verified, null will be returned. | _true_ |

## Example Request[¶](#example-request "Permalink to this headline")

GET [https://api.twitter.com/1.1/account/verify\_credentials.json](https://api.twitter.com/1.1/account/verify_credentials.json)