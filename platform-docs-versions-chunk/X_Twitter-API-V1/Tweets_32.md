platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-show-id


## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id  | required | The numerical ID of the desired Tweet. |     | _123_ |
| trim\_user | optional | When set to either _true_ , _t_ or _1_ , each Tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object. |     | _true_ |
| include\_my\_retweet | optional | When set to either _true_ , _t_ or _1_ , any Tweets returned that have been retweeted by the authenticating user will include an additional _current\_user\_retweet_ node, containing the ID of the source status for the retweet. |     | _true_ |
| include\_entities | optional | The _entities_ node will not be included when set to _false_. |     | _false_ |
| include\_ext\_alt\_text | optional | If alt text has been added to any attached media entities, this parameter will return an _ext\_alt\_text_ value in the top-level key for the media entity. If no value has been set, this will be returned as `null` |     | _true_ |
| include\_card\_uri | optional | When set to either _true_ , _t_ or _1_ , the retrieved Tweet will include a _card\_uri_ attribute when there is an ads card attached to the Tweet and when that card was attached using the _card\_uri_ value. |     | _true_ |
| include\_ext\_edit\_control | optional | Must be set to true in order to return edited Tweet metadata as part of the Tweet object.<br><br>`include_ext_edit_control=true`<br><br>Note that historical Tweets may not contain edited Tweet metadata. |     | _true_ |