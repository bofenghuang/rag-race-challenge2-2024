platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-users-search

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| q   | required | The search query to run against people search. |     | _Twitter%20API_ |
| page | optional | Specifies the page of results to retrieve. |     | _3_ |
| count | optional | The number of potential user results to retrieve per page. This value has a maximum of 20. |     | _5_ |
| include\_entities | optional | The _entities_ node will not be included in embedded Tweet objects when set to _false_ . |     | _false_ |