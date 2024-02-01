platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/api-reference/get-statuses-mentions_timeline


## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| count | optional | Specifies the number of Tweets to try and retrieve, up to a maximum of 200. The value of _count_ is best thought of as a limit to the number of tweets to return because suspended or deleted content is removed after the count has been applied. We include retweets in the count, even if _include\_rts_ is not supplied. It is recommended you always send _include\_rts=1_ when using this API method. |     |     |
| since\_id | optional | Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occured since the since\_id, the since\_id will be forced to the oldest ID available. |     | _12345_ |
| max\_id | optional | Returns results with an ID less than (that is, older than) or equal to the specified ID. |     | _54321_ |
| trim\_user | optional | When set to either _true_ , _t_ or _1_ , each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object. |     | _true_ |
| include\_entities | optional | The _entities_ node will not be included when set to _false_. |     | _false_ |
| include\_ext\_edit\_control | optional | Must be set to true in order to return edited Tweet metadata as part of the Tweet object.<br><br>`include_ext_edit_control=true`<br><br>Note that historical Tweets may not contain edited Tweet metadata.<br><br>To learn more about how edited Tweets are supported, see the [Edit Tweets fundamentals](https://developer.twitter.com/en/docs/twitter-api/v1/edit-tweets) page. |     | _true_ |