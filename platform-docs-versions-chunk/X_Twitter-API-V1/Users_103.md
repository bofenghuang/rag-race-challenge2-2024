platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| screen\_name | optional | A comma separated list of screen names, up to 100 are allowed in a single request. You are strongly encouraged to use a POST for larger (up to 100 screen names) requests. |     | _twitterapi twitter_ |
| user\_id | optional | A comma separated list of user IDs, up to 100 are allowed in a single request. You are strongly encouraged to use a POST for larger requests. |     | _783214 6253282_ |
| include\_entities | optional | The _entities_ node that may appear within embedded statuses will not be included when set to _false_. |     | _false_ |
| tweet\_mode | optional | Valid request values are compat and extended, which give compatibility mode and extended mode, respectively for Tweets that contain over 140 characters |     | _false_ |