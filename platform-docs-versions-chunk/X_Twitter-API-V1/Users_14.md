platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/manage-account-settings/api-reference/post-account-settings


## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |
| --- | --- | --- | --- |
| Name | Required | Description | Example |
| sleep\_time\_enabled | optional | When set to _true_ , _t_ or _1_ , will enable sleep time for the user. Sleep time is the time when push or SMS notifications should not be sent to the user. | _true_ |
| start\_sleep\_time | optional | The hour that sleep time should begin if it is enabled. The value for this parameter should be provided in [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format (i.e. 00-23). The time is considered to be in the same timezone as the user's _time\_zone_ setting. | _13_ |
| end\_sleep\_time | optional | The hour that sleep time should end if it is enabled. The value for this parameter should be provided in [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format (i.e. 00-23). The time is considered to be in the same timezone as the user's _time\_zone_ setting. | _13_ |
| time\_zone | optional | The timezone dates and times should be displayed in for the user. The timezone must be one of the [Rails TimeZone](http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html) names. | _Europe/Copenhagen_ _Pacific/Tongatapu_ |
| trend\_location\_woeid | optional | The Yahoo! Where On Earth ID to use as the user's default trend location. Global information is available by using 1 as the WOEID. The WOEID must be one of the locations returned by [GET trends/available](https://developer.twitter.com/en/docs/trends/locations-with-trending-topics/api-reference/get-trends-available) . | _1_ |
| lang | optional | The language which Twitter should render in for this user. The language must be specified by the appropriate two letter ISO 639-1 representation. Currently supported languages are provided by [this endpoint](https://developer.twitter.com/en/docs/developer-utilities/supported-languages/api-reference/get-help-languages) . | _it_ _en_ _es_ |