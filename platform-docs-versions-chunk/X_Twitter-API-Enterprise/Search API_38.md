platform: X
topic: Twitter-API-Enterprise
subtopic: Search API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Search API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/api-reference/enterprise-search


### Data request parameters [¶](#data-request-parameters- "Permalink to this headline")

| Parameters | Description | Required | Sample Value |
| --- | --- | --- | --- |
| query | The equivalent of one PowerTrack rule, with up to 2,048 characters (and no limits on the number of positive and negative clauses).  <br>  <br>This parameter should include ALL portions of the PowerTrack rule, including all operators, and portions of the rule should not be separated into other parameters of the query.  <br>  <br>**Note:** Not all PowerTrack operators are supported. Supported Operators are listed [HERE](https://developer.twitter.com/en/docs/tweets/search/overview/enterprise#AvailableOperators). | Yes | (snow OR cold OR blizzard) weather |
| tag | Tags can be used to segregate rules and their matching data into different logical groups. If a rule tag is provided the rule tag is included in the 'matching\_rules' attribute.  <br>  <br>It is recommended to assign rule-specific UUIDs to rule tags and maintain desired mappings on the client side. | No  | 8HYG54ZGTU |
| fromDate | The oldest UTC timestamp (back to 3/21/2006 with Full-Archive search) from which the Tweets will be provided. Timestamp is in minute granularity and is inclusive (i.e. 12:00 includes the 00 minute).  <br>  <br>_Specified:_ Using only the fromDate with no toDate parameter will deliver results for the query going back in time from now( ) until the fromDate.  <br>  <br>_Not Specified:_ If a fromDate is not specified, the API will deliver all of the results for 30 days prior to now( ) or the toDate (if specified).  <br>  <br>If neither the fromDate or toDate parameter is used, the API will deliver all results for the most recent 30 days, starting at the time of the request, going backwards. | No  | 201207220000 |
| toDate | The latest, most recent UTC timestamp to which the Tweets will be provided. Timestamp is in minute granularity and is not inclusive (i.e. 11:59 does not include the 59th minute of the hour).  <br>  <br>_Specified:_ Using only the toDate with no fromDate parameter will deliver the most recent 30 days of data prior to the toDate.  <br>  <br>_Not Specified:_ If a toDate is not specified, the API will deliver all of the results from now( ) for the query going back in time to the fromDate.  <br>  <br>If neither the fromDate or toDate parameter is used, the API will deliver all results for the entire 30-day index, starting at the time of the request, going backwards. | No  | 201208220000 |
| maxResults | The maximum number of search results to be returned by a request. A number between 10 and the system limit (currently 500). By default, a request response will return 100 results. | No  | 500 |
| next | This parameter is used to get the next 'page' of results as described [HERE](#Pagination). The value used with the parameter is pulled directly from the response provided by the API, and should not be modified. | No  | NTcxODIyMDMyODMwMjU1MTA0 |

  

#### Additional details 

|     |     |
| --- | --- |
| **Available Timeframe** | 30-Day: last 31 days  <br>Full-Archive: March 21, 2006 - Present |
| **Query Format** | The equivalent of one PowerTrack rule, with up to 2,048 characters (and no limits on the number of positive and negative clauses).  <br>  <br>**Note:** Not all PowerTrack operators are supported. Refer to [Available operators](https://developer.twitter.com/en/docs/tweets/search/overview/enterprise#AvailableOperators) for a list of supported operators. |
| **Rate Limit** | Partners will be rate limited at both minute and second granularity. The per minute rate limit will vary by partner as specified in your contract. However, these per-minute rate limits are not intended to be used in a single burst. Regardless of your per minute rate limit, all partners will be limited to a maximum of 20 requests per second, aggregated across all requests for data and/or counts. |
| **Compliance** | All data delivered via the Full-Archive Search API is compliant at the time of delivery. |
| **Realtime Availability** | Data is available in the index within 30 seconds of generation on the Twitter Platform |