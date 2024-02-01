platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/counts/api-reference/get-tweets-counts-recent


### Query parameters

| Name | Type | Description |
| --- | --- | --- |
| `query`  <br> Required | string | One query for matching Tweets. You can learn how to build this query by reading our [build a query guide](https://developer.twitter.com/en/docs/twitter-api/tweets/counts/integrate/build-a-query).  <br>  <br>If you have Essential or Elevated access, you can use the Basic operators when building your query and can make queries up to 512 characters long. If you have been approved for Academic Research access, you can use all available operators and can make queries up to 1,024 characters long.  <br>  <br>Learn more about our access levels on the about Twitter API page. |
| `end_time`  <br> Optional | date (ISO 8601) | YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339). The newest, most recent UTC timestamp to which the Tweet counts will be provided. Timestamp is in second granularity and is exclusive (for example, 12:00:01 excludes the first second of the minute). By default, a request will return Tweet counts from as recent as 30 seconds ago if you do not include this parameter. |
| `granularity`  <br> Optional | string | This is the granularity that you want the timeseries count data to be grouped by. You can requeset `minute`, `hour`, or `day` granularity. The default granularity, if not specified is `hour`. |
| `since_id`  <br> Optional | string | Returns results with a Tweet ID greater than (that is, more recent than) the specified ID. The ID specified is exclusive and responses will not include it. If included with the same request as a `start_time` parameter, only `since_id` will be used. |
| `start_time`  <br> Optional | date (ISO 8601) | YYYY-MM-DDTHH:mm:ssZ (ISO 8601/RFC 3339). The oldest UTC timestamp (from most recent seven days) from which the Tweet counts will be provided. Timestamp is in second granularity and is inclusive (for example, 12:00:01 includes the first second of the minute). If included with the same request as a `since_id` parameter, only `since_id` will be used. By default, a request will return Tweet counts from up to seven days ago if you do not include this parameter. |
| `until_id`  <br> Optional | string | Returns results with a Tweet ID less than (that is, older than) the specified ID. The ID specified is exclusive and responses will not include it. |