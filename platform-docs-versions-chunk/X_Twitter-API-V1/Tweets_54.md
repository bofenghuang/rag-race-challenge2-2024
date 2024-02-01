platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-retweets-id

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id  | required | The numerical ID of the desired status. |     | _123_ |
| count | optional | Specifies the number of records to retrieve. Must be less than or equal to 100. |     | _5_ |
| trim\_user | optional | When set to either _true_ , _t_ or _1_ , each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object. |     | _true_ |
| include\_ext\_edit\_control | optional | Must be set to true in order to return edited Tweet metadata as part of the Tweet object.<br><br>`include_ext_edit_control=true`<br><br>Note that historical Tweets may not contain edited Tweet metadata. |     | _true_ |