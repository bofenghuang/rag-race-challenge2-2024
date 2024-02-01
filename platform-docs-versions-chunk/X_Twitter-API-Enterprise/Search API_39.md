platform: X
topic: Twitter-API-Enterprise
subtopic: Search API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Search API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/api-reference/enterprise-search


### Example data requests and responses [¶](#example-data-requests-and-responses- "Permalink to this headline")

#### Example POST request

* Request parameters in a POST request are sent via a JSON-formatted body, as shown below.
* All portions of the PowerTrack rule being queried for (e.g. keywords, other operators like bounding\_box:) should be placed in the 'query' parameter.
* Do not split portions of the rule out as separate parameters in the query URL.

Here is an example POST (using cURL) command for making an initial data request:

    curl -X POST -u<username> "https://gnip-api.twitter.com/search/:product/accounts/:account_name/:label.json" -d '{"query":"from:twitterDev","maxResults":500,"fromDate":"yyyymmddhhmm","toDate":"yyyymmddhhmm"}'

If the API data response includes a 'next' token, below is a subsequent request that consists of the original request, with the 'next' parameter set to the provided token:

    curl -X POST -u<username> "https://gnip-api.twitter.com/search/:product/accounts/:account_name/:label.json" -d '{"query":"from:twitterDev","maxResults":500,"fromDate":"yyyymmddhhmm","toDate":"yyyymmddhhmm",
    "next":"NTcxODIyMDMyODMwMjU1MTA0"}'

#### Example GET request 

* Request parameters in a GET request are encoded into the URL, using standard URL encoding.
* All portions of the PowerTrack rule being queried for (e.g. keywords, other operators like bounding\_box:) should be placed in the 'query' parameter.
* Do not split portions of the rule out as separate parameters in the query URL.

Here is an example GET (using cURL) command for making an initial data request:

    curl -u<username> "http://gnip-api.twitter.com/search/:product/accounts/:account_name/:label.json?query=from%3Atwitterdev&maxResults=500&fromDate=yyyymmddhhmm&toDate=yyyymmddhhmm"

#### Example data responses 

Note that for Tweets created starting September 29, 2022, Tweet objects will include Tweet edit metadata that describes its edit history. See the ["Edit Tweets"](https://developer.twitter.com/en/docs/twitter-api/enterprise/edit-tweets) fundamentals page for more details.

Below is an example response to a data query. This example assumes that there were more than ‘maxResults’ Tweets available so a 'next' token is provided for subsequent requests. If 'maxResults' or fewer Tweets are associated with your query, no 'next' token would be included in the response.  
The value of the 'next' element will change with each query and should be treated as an opaque string. The 'next' element will look like the following in the response body:  

    {
        "results":
          [
               {--Tweet 1--},
               {--Tweet 2--},
               ...
               {--Tweet 500--}
          ],
        "next":"NTcxODIyMDMyODMwMjU1MTA0",  
        "requestParameters":
          {
            "maxResults":500,
            "fromDate":"201101010000",
            "toDate":"201201010000"
          }
     }

The response to a subsequent request might look like the following (note the new Tweets and different 'next' value):  

    {
          "results":
          [
               {--Tweet 501--},
               {--Tweet 502--},
               ...
               {--Tweet 1000--}
          ],
          "next":"R2hCDbpBFR6eLXGwiRF1cQ",
          "requestParameters":
          {
            "maxResults":500,
            "fromDate":"201101010000",
            "toDate":"201201010000"
          }
     }

You can continue to pass in the 'next' element from your previous query until you have received all Tweets from the time period covered by your query. When you receive a response that does not include a 'next' element, it means that you have reached the last page and no additional data is available in your time range.

* * *