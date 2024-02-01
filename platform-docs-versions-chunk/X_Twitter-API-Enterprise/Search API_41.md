platform: X
topic: Twitter-API-Enterprise
subtopic: Search API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Search API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/api-reference/enterprise-search


### Counts request parameters [¶](#counts-request-parameters- "Permalink to this headline")

| Parameters | Description | Required | Sample Value |
| --- | --- | --- | --- |
| query | The equivalent of one PowerTrack rule, with up to 2,048 characters (and no limits on the number of positive and negative clauses).  <br>  <br>This parameter should include ALL portions of the PowerTrack rule, including all operators, and portions of the rule should not be separated into other parameters of the query.  <br>  <br>**Note:** Not all PowerTrack operators are supported. Refer to [Available operators](https://developer.twitter.com/en/docs/tweets/search/overview/enterprise#AvailableOperators) for a list of supported operators. | Yes | (snow OR cold OR blizzard) weather |
| fromDate | The oldest UTC timestamp (back to 3/21/2006) from which the Tweets will be provided. Timestamp is in minute granularity and is inclusive (i.e. 12:00 includes the 00 minute).  <br>  <br>_Specified:_ Using only the fromDate with no toDate parameter, the API will deliver counts (data volumes) data for the query going back in time from now until the fromDate. If the fromDate is older than 31 days from now( ), you will receive a next token to page through your request.  <br>  <br>_Not Specified:_ If a fromDate is not specified, the API will deliver counts (data volumes) for 30 days prior to now( ) or the toDate (if specified).  <br>  <br>If neither the fromDate or toDate parameter is used, the API will deliver counts (data volumes) for the most recent 30 days, starting at the time of the request, going backwards. | No  | 201207220000 |
| toDate | The latest, most recent UTC timestamp to which the Tweets will be provided. Timestamp is in minute granularity and is not inclusive (i.e. 11:59 does not include the 59th minute of the hour).  <br>  <br>_Specified:_ Using only the toDate with no fromDate parameter will deliver the most recent counts (data volumes) for 30 days prior to the toDate.  <br>  <br>_Not Specified:_ If a toDate is not specified, the API will deliver counts (data volumes) for the query going back in time to the fromDate. If the fromDate is more than 31 days from now( ), you will receive a next token to page through your request.  <br>  <br>If neither the fromDate or toDate parameter is used, the API will deliver counts (data volumes) for the most recent 30 days, starting at the time of the request, going backwards. | No  | 201208220000 |
| bucket | The unit of time for which count data will be provided. Count data can be returned for every day, hour or minute in the requested timeframe. By default, hourly counts will be provided. Options: 'day', 'hour', 'minute' | No  | minute |
| next | This parameter is used to get the next 'page' of results as described [HERE](#Pagination). The value used with the parameter is pulled directly from the response provided by the API, and should not be modified. | No  | NTcxODIyMDMyODMwMjU1MTA0 |

#### Additional details

|     |     |
| --- | --- |
| **Available Timeframe** | 30-Day: last 31 days  <br>Full-Archive: March 21, 2006 - Present |
| **Query Format** | The equivalent of one PowerTrack rule, with up to 2,048 characters.  <br>  <br>**Note:** Not all PowerTrack operators are supported. Refer to [Available operators](https://developer.twitter.com/en/docs/tweets/search/overview/enterprise#AvailableOperators) for a list of supported operators. |
| **Rate Limit** | Partners will be rate limited at both minute and second granularity. The per minute rate limit will vary by partner as specified in your contract. However, these per-minute rate limits are not intended to be used in a single burst. Regardless of your per minute rate limit, all partners will be limited to a maximum of 20 requests per second, aggregated across all requests for data and/or counts. |
| **Count Precision** | The counts delivered through this endpoint reflect the number of Tweets that occurred and do not reflect any later compliance events (deletions, scrub geos). Some Tweets counted may not be available via data endpoint due to user compliance actions. |