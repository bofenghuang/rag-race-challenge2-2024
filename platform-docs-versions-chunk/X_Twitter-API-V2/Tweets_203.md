platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/counts/migrate/enterprise-to-twitter-api-v2


### Differences

#### Endpoint URLs

* Enterprise endpoints:
    * 30 day - `http://gnip-api.twitter.com/search/30day/accounts/:account_name/:label/counts.json`
    * Full-archive - `http://gnip-api.twitter.com/search/fullarchive/accounts/:account_name/:label/counts.json`
* Twitter API v2 endpoints
    * Recent (7 day) - `https://api.twitter.com/2/tweets/counts/recent`
    * Full-archive - `https://api.twitter.com/2/tweets/counts/all`

####   
App and Project requirement

The Twitter API v2 endpoints require that you use credentials from a [developer App](https://developer.twitter.com/content/developer-twitter/en/docs/apps) that is associated with a [Project](https://developer.twitter.com/content/developer-twitter/en/docs/projects) when authenticating your requests. All Twitter API v1.1 endpoints can use credentials from standalone Apps or Apps associated with a Project.  
 

#### Available time periods

Both the enterprise API and Twitter API v2 offer endpoints that allow you to retrieve Tweet volume data for the full-archive of Tweets.

However, the Twitter API v2 does not offer a 30 day time period endpoint like the enterprise API does. Instead it offers the aforementioned full-archive, or a 7 day time period, which align with the [v2 Search Tweets endpoints](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/tweets/search).  
 

#### Response data format

There are some slight differences in the data format that you will receive via enterprise and Twitter API v2:

* Enterprise’s counts data is located within a `results` object, while the v2 counts data is located within a data object.
* Enterprise’s counts fields are called `timePeriod` (start time) and `count`, while v2 breaks out the time period into a `start` and `end` field (which use a different date/time format from enterprise explained in request time formats), and renamed the count field to `tweet_count`.
* The enterprise metadata includes `totalCount`, `next`, and the `requestParameters` object at the root level. Instead,v2 doesn’t include the requestParameters object, and moves/renames the following into a `meta` object that lives at the root level: `total_tweet_count` & `next_token`.  
     

#### HTTP methods

The enterprise version of the API allows you to pass the request as either a POST HTTP method with a JSON body, or a GET HTTP method with a query string.

V2 only allows you to use the GET HTTP method with a query string.  
 

#### Request time formats

The enterprise version of this endpoint uses the following date/time format in both the pagination parameters and the `timePeriod` response field: `YYYYMMDDHHmm`

The v2 endpoint uses ISO 8601/RFC 3339 date/time format in both the pagination parameters and the `start` and `end` response fields: `YYYY-MM-DDTHH:mm:ssZ`

####   
Request parameters

The following is a table of the request parameters for enterprise and Twitter API v2:

| Enterprise | Search Tweets v2 |
| --- | --- |
| query | query |
| bucket | granularity |
| fromDate (YYMMDDHHmm) | start\_time (YYYY-MM-DDTHH:mm:ssZ) |
| toDate (YYMMDDHHmm) | end\_time (YYYY-MM-DDTHH:mm:ssZ) |
|     | since\_id |
|     | until\_id |
| next | next\_token and pagination\_token |

####   
Filtering operators

While the operators between enterprise and Twitter API v2 are mostly the same, there are some differences in operator availability and some new operators that were introduced to just the Twitter API v2 version.

To see a full table of the operators that are available for Twitter API v2, enterprise, and even premium, please visit the [Tweet counts migration landing page](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/tweets/counts/migrate).