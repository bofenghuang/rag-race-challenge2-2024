platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/api-reference/get-search-tweets


## Parameters[¶](#parameters "Permalink to this headline")

| Name | Required | Description | Default Value | Example |
| --- | --- | --- | --- | --- |
| q   | required | A UTF-8, URL-encoded search query of 500 characters maximum, including operators. Queries may additionally be limited by complexity. |     | `@noradio` |
| include\_ext\_edit\_control | optional | Must be set to true in order to return edited Tweet metadata as part of the Tweet object.<br><br>`include_ext_edit_control=true`<br><br>Note that historical Tweets may not contain edited Tweet metadata.<br><br>To learn more about how edited Tweets are supported, see the [Edit Tweets fundamentals](https://developer.twitter.com/en/docs/twitter-api/v1/edit-tweets) page. |     | `true` |
| geocode | optional | Returns tweets by users located within a given radius of the given latitude/longitude. The location is preferentially taking from the Geotagging API, but will fall back to their Twitter profile. The parameter value is specified by " `latitude,longitude,radius` ", where radius units must be specified as either " `mi` " (miles) or " `km` " (kilometers). Note that you cannot use the near operator via the API to geocode arbitrary locations; however you can use this `geocode` parameter to search near geocodes directly. A maximum of 1,000 distinct "sub-regions" will be considered when using the radius modifier. |     | `37.781157 -122.398720 1mi` |
| lang | optional | Restricts tweets to the given language, given by an [ISO 639-1](http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) code. Language detection is best-effort. |     | `eu` |
| locale | optional | Specify the language of the query you are sending (only `ja` is currently effective). This is intended for language-specific consumers and the default should work in the majority of cases. |     | `ja` |
| result\_type | optional | Optional. Specifies what type of search results you would prefer to receive. The current default is "mixed." Valid values include:<br><br>\* `mixed` : Include both popular and real time results in the response.<br><br>\* `recent` : return only the most recent results in the response<br><br>\* `popular` : return only the most popular results in the response. |     | `mixed` `recent` `popular` |
| count | optional | The number of tweets to return per page, up to a maximum of 100. Defaults to 15. This was formerly the "rpp" parameter in the old Search API. |     | `100` |
| until | optional | Returns tweets created before the given date. Date should be formatted as YYYY-MM-DD. Keep in mind that the search index has a 7-day limit. In other words, no tweets will be found for a date older than one week. |     | `2015-07-19` |
| since\_id | optional | Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occured since the since\_id, the since\_id will be forced to the oldest ID available. |     | `12345` |
| max\_id | optional | Returns results with an ID less than (that is, older than) or equal to the specified ID. |     | `54321` |
| include\_entities | optional | The `entities` node will not be included when set to `false`. |     | `false` |