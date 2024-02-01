platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-lookup


## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id  | required | A comma separated list of Tweet IDs, up to 100 are allowed in a single request. |     | _20_ _1050118621198921728_ |
| include\_entities | optional | The _entities_ node that may appear within embedded statuses will not be included when set to _false_. |     | _false_ |
| trim\_user | optional | When set to either _true_ , _t_ or _1_ , each Tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object. |     | _true_ |
| map | optional | When using the _map_ parameter, Tweets that do not exist or cannot be viewed by the current user will still have their key represented but with an explicitly _null_ value paired with it |     | _true_ |
| include\_ext\_alt\_text | optional | If alt text has been added to any attached media entities, this parameter will return an _ext\_alt\_text_ value in the top-level key for the media entity. If no value has been set, this will be returned as `null` |     | _true_ |
| include\_card\_uri | optional | When set to either _true_ , _t_ or _1_ , each Tweet returned will include a _card\_uri_ attribute when there is an ads card attached to the Tweet and when that card was attached using the _card\_uri_ value. |     | _true_ |
| include\_ext\_edit\_control | optional | Must be set to true in order to return edited Tweet metadata as part of the Tweet object.<br><br>`include_ext_edit_control=true`<br><br>Note that historical Tweets may not contain edited Tweet metadata. |     | _true_ |