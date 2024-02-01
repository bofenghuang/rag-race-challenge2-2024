platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/manage-account-settings/api-reference/post-account-update_profile

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| name | optional | Full name associated with the profile. |     | _Marcel Molina_ |
| url | optional | URL associated with the profile. Will be prepended with `http://` if not present. |     | `http://project.ioni.st` |
| location | optional | The city or country describing where the user of the account is located. The contents are not normalized or geocoded in any way. |     | _San Francisco CA_ |
| description | optional | A description of the user owning the account. |     | _Flipped my wig at age 22 and it never grew back. Also: I work at Twitter._ |
| include\_entities | optional | The _entities_ node will not be included when set to _false_ . |     | _false_ |
| skip\_status | optional | When set to either _true_ , _t_ or _1_ statuses will not be included in the returned user object. |     |     |