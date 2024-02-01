platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/counts/api-reference/get-tweets-counts-all


### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `query`  <br> Required | string | One query for matching Tweets. You can learn how to build this query by reading our [build a query guide](https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query).You can use all available operators and can make queries up to 1,024 characters long. |
| `end_time`  <br> Optional | date (ISO 8601) | YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339). Used with `start_time`. The newest, most recent UTC timestamp to which the Tweets will be provided. Timestamp is in second granularity and is exclusive (for example, 12:00:01 excludes the first second of the minute). If used without `start_time`, Tweets from 30 days before `end_time` will be returned by default. If not specified, `end_time` will default to \[now - 30 seconds\]. |
| `granularity`  <br> Optional | string | This is the granularity that you want the timeseries count data to be grouped by. You can requeset `minute`, `hour`, or `day` granularity. The default granularity, if not specified is `hour`. |
| `next_token`  <br> Optional | string | This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, assuming that your request contains more than 31 days-worth of results, and should not be modified. You can learn more by visiting our page on [pagination](https://developer.twitter.com/en/docs/twitter-api/pagination). |
| `since_id`  <br> Optional | string | Returns results with a Tweet ID greater than (for example, more recent than) the specified ID. The ID specified is exclusive and responses will not include it. If included with the same request as a `start_time` parameter, only `since_id` will be used. |
| `start_time`  <br> Optional | date (ISO 8601) | YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339). The oldest UTC timestamp from which the Tweets will be provided. Timestamp is in second granularity and is inclusive (for example, 12:00:01 includes the first second of the minute). By default, a request will return Tweets from up to 30 days ago if you do not include this parameter. |
| `until_id`  <br> Optional | string | Returns results with a Tweet ID less than (that is, older than) the specified ID. Used with `since_id`. The ID specified is exclusive and responses will not include it. |