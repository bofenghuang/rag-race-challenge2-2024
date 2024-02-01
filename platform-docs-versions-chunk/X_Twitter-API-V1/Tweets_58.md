platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-retweets_of_me


## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| count | optional | Specifies the number of records to retrieve. Must be less than or equal to 100. If omitted, 20 will be assumed. |     | _5_ |
| since\_id | optional | Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occured since the since\_id, the since\_id will be forced to the oldest ID available. |     | _12345_ |
| max\_id | optional | Returns results with an ID less than (that is, older than) or equal to the specified ID. |     | _54321_ |
| trim\_user | optional | When set to either _true_ , _t_ or _1_ , each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object. |     | _true_ |
| include\_entities | optional | The tweet _entities_ node will not be included when set to _false_ . |     | _false_ |
| include\_user\_entities | optional | The user _entities_ node will not be included when set to _false_ . |     | _false_ |
| include\_ext\_edit\_control | optional | Must be set to true in order to return edited Tweet metadata as part of the Tweet object.<br><br>`include_ext_edit_control=true`<br><br>Note that historical Tweets may not contain edited Tweet metadata. |     | _true_ |