platform: X
topic: Twitter-API-Enterprise
subtopic: Search API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Search API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/api-reference/enterprise-search


### Example counts requests and responses [¶](#example-counts-requests-and-responses- "Permalink to this headline")

#### Example POST request

* Request parameters in a POST request are sent via a JSON-formatted body, as shown below.
* All portions of the PowerTrack rule being queried for (e.g. keywords, other operators like bounding\_box:) should be placed in the 'query' parameter.
* Do not split portions of the rule out as separate parameters in the query URL.

Here is an example POST (using cURL) command for making an initial counts request:

    curl -X POST -u<username> "https://gnip-api.twitter.com/search/:product/accounts/:account_name/:label/counts.json" -d '{"query":"TwitterDev","fromDate":"yyyymmddhhmm","toDate":"yyyymmddhhmm","bucket":"day"}'

If the API counts response includes a 'next' token, below is a subsequent request that consists of the original request, with the 'next' parameter set to the provided token:

    curl -X POST -u<username> "https://gnip-api.twitter.com/search/:product/accounts/:account_name/:label/counts.json" -d '{"query":"TwitterDev","fromDate":"yyyymmddhhmm","toDate":"yyyymmddhhmm","bucket":"day",
    "next":"YUcxO87yMDMyODMwMjU1MTA0"}'

#### Example GET request

* Request parameters in a GET request are encoded into the URL, using standard URL encoding
* All portions of the PowerTrack rule being queried for (e.g. keywords, other operators like bounding\_box:) should be placed in the 'query' parameter
* Do not split portions of the rule out as separate parameters in the query URL

Here is an example GET (using cURL) command for making an initial counts request:

    curl -u<username> "http://gnip-api.twitter.com/search/fullarchive/accounts/:account_name/:label/counts.json?query=TwitterDev&bucket=day&fromDate=yyyymmddhhmm&toDate=yyyymmddhhmm"

#### Example counts responses

Below is an example response to a counts (data volume) query. This example response includes a 'next' token, meaning the counts request was for more than 31 days, or that the submitted query had a large enough volume associated with it to trigger a partial response.

The value of the 'next' element will change with each query and should be treated as an opaque string. The 'next' element will look like the following in the response body:

    {
      "results": [
        { "timePeriod": "201101010000", "count": 32 },
        { "timePeriod": "201101020000", "count": 45 },
        { "timePeriod": "201101030000", "count": 57 },
        { "timePeriod": "201101040000", "count": 123 },
        { "timePeriod": "201101050000", "count": 134 },
        { "timePeriod": "201101060000", "count": 120 },
        { "timePeriod": "201101070000", "count": 43 },
        { "timePeriod": "201101080000", "count": 65 },
        { "timePeriod": "201101090000", "count": 85 },
        { "timePeriod": "201101100000", "count": 32 },
        { "timePeriod": "201101110000", "count": 23 },
        { "timePeriod": "201101120000", "count": 85 },
        { "timePeriod": "201101130000", "count": 32 },
        { "timePeriod": "201101140000", "count": 95 },
        { "timePeriod": "201101150000", "count": 109 },
        { "timePeriod": "201101160000", "count": 34 },
        { "timePeriod": "201101170000", "count": 74 },
        { "timePeriod": "201101180000", "count": 24 },
        { "timePeriod": "201101190000", "count": 90 },
        { "timePeriod": "201101200000", "count": 85 },
        { "timePeriod": "201101210000", "count": 93 },
        { "timePeriod": "201101220000", "count": 48 },
        { "timePeriod": "201101230000", "count": 37 },
        { "timePeriod": "201101240000", "count": 54 },
        { "timePeriod": "201101250000", "count": 52 },
        { "timePeriod": "201101260000", "count": 84 },
        { "timePeriod": "201101270000", "count": 120 },
        { "timePeriod": "201101280000", "count": 34 },
        { "timePeriod": "201101290000", "count": 83 },
        { "timePeriod": "201101300000", "count": 23 },
        { "timePeriod": "201101310000", "count": 12 }
       ],
      "totalCount":2027,
      "next":"NTcxODIyMDMyODMwMjU1MTA0",
      "requestParameters":
        {
          "bucket":"day",
          "fromDate":"201101010000",
          "toDate":"201201010000"
        }
    }

The response to a subsequent request might look like the following (note the new counts timeline and different 'next' value):

    {
      "results": [
        { "timePeriod": "201102010000", "count": 45 },
        { "timePeriod": "201102020000", "count": 76 },
         ....
        { "timePeriod": "201103030000", "count": 13 }
     ],
     "totalCount":3288,
     "next":"WE79fnakFanyMDMyODMwMjU1MTA0",
     "requestParameters":
        {
          "bucket":"day",
          "fromDate":"201101010000",
          "toDate":"201201010000"
        }
    }
    

You can continue to pass in the 'next' element from your previous query until you have received all counts from the query time period. When you receive a response that does not include a 'next' element, it means that you have reached the last page and no additional counts are available in your time range.