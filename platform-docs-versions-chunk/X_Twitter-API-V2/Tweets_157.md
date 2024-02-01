platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/search/migrate/enterprise-to-twitter-api-v2


### Differences

#### Endpoint URLs

* Enterprise endpoints:
    * 30 day - `http://gnip-api.twitter.com/search/30day/accounts/:account_name/:label.json`
    * Full-archive - `http://gnip-api.twitter.com/search/fullarchive/accounts/:account_name/:label.json`
* Twitter API v2 endpoints
    * Recent (7 day) - `https://api.twitter.com/2/tweets/search/recent`
    * Full-archive - `https://api.twitter.com/2/tweets/search/all`

#### App and Project requirement

The Twitter API v2 endpoints require that you use credentials from a Project when authenticating your requests. All Twitter API v1.1 endpoints can use credentials from standalone Apps or Apps associated with a Project.  
 

#### Available time periods

Both the enterprise API and Twitter API v2 offer endpoints that allow you to retrieve filtered Tweet data for the full-archive of Tweets.

However, the Twitter API v2 does not offer a 30 day time period endpoint like the enterprise API does. Instead it offers the aforementioned full-archive, or a 7 day time period, which align with the Native Enriched to v2 and [Activity Streams to v2](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats/activity-streams-to-v2) which can help you map enterprise fields to the newer v2 fields. This guide will also provide you the specific expansion and field parameter that you will need to pass with your v2 request to return specific fields.  
 

#### Response data format

One of the biggest differences between the [enterprise response format](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/overview) and [Twitter API v2’s format](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction) is how you select which fields return in your payload.  

For the enterprise Search API, you receive many of the response fields by default, and then have the option to use parameters to identify which fields or sets of fields should return in the payload.

The Twitter API v2 version only delivers the Tweet `id` and `text` fields by default. To request any additional fields or objects, you will need to use the [fields](https://developer.twitter.com/en/docs/twitter-api/fields) and [expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) parameters. Any Tweet fields that you request from these endpoints will return in the primary Tweet object. Any expanded user, media, poll, or place objects and fields will return in an `includes` object within your response. You can then match any expanded objects back to the Tweet object by matching the IDs located in both the Tweet and the expanded object.

We encourage you to read more about these new parameters in their respective guides, or by reading our guide on [how to use fields and expansions](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/using-fields-and-expansions).

In addition to the changes in how you request certain fields, Twitter API v2 is also introducing new JSON designs for the objects returned by the APIs, including [Tweet](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) and [user](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) objects.

* At the JSON root level, the standard endpoints return Tweet objects in a `statuses` array, while Twitter API v2 returns a `data` array.
* Instead of referring to Retweeted and Quoted "statuses", Twitter API v2 JSON refers to Retweeted and Quoted Tweets. Many legacy and deprecated fields, such as `contributors` and `user.translator_type` are being removed.
* Instead of using both `favorites` (in Tweet object) and `favourites` (in user object), Twitter API v2 uses the term like.
* Twitter is adopting the convention that JSON values with no value (for example, `null`) are not written to the payload. Tweet and user attributes are only included if they have non-null values.  
     

We also introduced a new set of fields to the Tweet object including the following:

* A [conversation\_id](https://developer.twitter.com/en/docs/twitter-api/conversation-id) field
* Two new [annotations](https://developer.twitter.com/en/docs/twitter-api/annotations) fields, including context and entities
* Several new [metrics](https://developer.twitter.com/en/docs/twitter-api/metrics) fields
* A new `reply_setting` field, which shows you who can reply to a given Tweet  
     

And one last note. The premium response includes a `requestParameters` object at the root level, which contains the parameters that you included in your request. The v2 version instead contains a `meta` object that lives at the root level which includes the `newest_id`, `oldest_id`, `result_count`, and `next_token` if there is an additional page of results.  

#### HTTP methods

The enterprise version of the API allows you to pass the request as either a POST HTTP method with a JSON body, or a GET HTTP method with a query string.

V2 only allows you to use the GET HTTP method with a query string.  
 

#### Request time formats

The enterprise version of this endpoint uses the following date/time format in both the pagination parameters and the `timePeriod` response field: `YYYYMMDDHHmm`

The v2 endpoint uses ISO 8601/RFC 3339 date/time format in both the pagination parameters and the `start` and `end` response fields: `YYYY-MM-DDTHH:mm:ssZ` 

#### Request parameters

The following is a table of the request parameters for enterprise and Twitter API v2:

| Enterprise | Search Tweets v2 |
| --- | --- |
| query | query |
| maxResults | max\_results |
| fromDate (YYMMDDHHmm) | start\_time (YYYY-MM-DDTHH:mm:ssZ) |
| toDate (YYMMDDHHmm) | end\_time (YYYY-MM-DDTHH:mm:ssZ) |
|     | since\_id |
|     | until\_id |
| next | next\_token or pagination\_token |

#### Filtering operators

While the operators between enterprise and Twitter API v2 are mostly the same, there are some differences in operator availability and some new operators that were introduced to just the Twitter API v2 version.

To see a full table of the operators that are available for Twitter API v2, enterprise, and even premium and standard, please visit the [Search Tweets migration landing page](https://developer.twitter.com/en/docs/twitter-api/tweets/search/migrate).