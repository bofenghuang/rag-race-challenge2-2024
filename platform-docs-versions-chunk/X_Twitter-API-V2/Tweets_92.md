platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/migrate/standard-to-twitter-api-v2


### Differences

#### **Authentication**

#### The v1.1 statuses/mentions\_timeline endpoint only supports  [OAuth 1.0a User Context](https://developer-staging.twitter.com/en/docs/authentication/oauth-1-0a).  The Twitter API v2 user mention timeline endpoint supports both [OAuth 1.0a User Context](https://developer-staging.twitter.com/en/docs/authentication/oauth-1-0a), [OAuth 2.0 App-Only](https://developer-staging.twitter.com/en/docs/authentication/oauth-2-0), and [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code "This method allows an authorized app to act on behalf of the user, as the user. It is typically used to access or post public information for a specific user, and it us useful when your app needs to be aware of the relationship between a user and what this endpoint returns. Click to learn how to authenticate with OAuth 2.0 Authorization Code with PKCE.")   

If you would like to take advantage of the ability to access private or promoted metrics using the Twitter API v2 user Tweet timeline endpoint, you will need to use OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE, and pass the user access tokens related to the user who posted the Tweet for which you would like to access metrics.  
 

#### Endpoint URLs

Note that the Twitter API v2 timelines endpoints require a path parameter of :id for the user ID.

* Standard v1.1 endpoints:
    * https://api.twitter.com/1.1/statuses/home\_timeline
    * https://api.twitter.com/1.1/statuses/user\_timeline
    * https://api.twitter.com/1.1/statuses/mention\_timeline
* Twitter API v2 endpoint:
    * https://api.twitter.com/2/users/:id/timelines/reverse\_chronological
    * https://api.twitter.com/2/users/:id/tweets
    * https://api.twitter.com/2/users/:id/mentions

####   
App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a [developer App](https://developer-staging.twitter.com/en/docs/apps) that is associated to a [Project](https://developer-staging.twitter.com/en/docs/projects) when authenticating your requests. All Twitter API v1.1 endpoints can use credentials from standalone Apps or Apps associated with a project.   
 

#### Rate Limits

|     |     |
| --- | --- |
| **mentions\_timeline:**<br><br>75 requests per 15 min with OAuth 1.0a User Context | **user mention timeline:** <br><br>180 requests per 15-minute window with OAuth 1.0a User Context  <br>450 requests per 15-minute window with OAuth 2.0 Bearer Token |
| **home\_timelime:**<br><br>15 requests per 15 minutes  <br><br>Up to 800 Tweets are obtainable on the home timeline | **reverse chronological home timeline:**<br><br>180 requests per 15 minutes<br><br>You can return every Tweet created on a timeline over the last 7 days as well as the most recent 800 regardless of creation date. |

#### Request limits

|     |     |
| --- | --- |
| **Standard timelines v1.1** | **timelines v2** |
| Daily request limit<br><br>* 100,000 request cap within a 24 hour period. | No daily request limits, only limited by consumption volume. |

#### Consumption volume limits

|     |     |
| --- | --- |
| **Standard timelines v1.1** | **timelines v2** |
| Consumption limited only by request limits<br><br>* 100,000 request cap within a 24 hour period. | Consumption limited by only Project-level monthly [Tweet cap](https://developer.twitter.com/en/docs/twitter-api/tweet-caps) (across multiple v2 endpoints) based on [access level](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level).<br><br>* 500,000 Tweets per month with Essential access.<br>* 2 million Tweets per month with Elevated access<br>* 10 million Tweets per month with Academic Research access <br><br>Reverse chronological home timeline is not subject to the monthly Tweet cap. |

#### Request parameters

|     |     |
| --- | --- |
| **Standard timelines v1.1** | **timelines v2** |
| Required: user\_id or screen\_name | Required: The specific user ID is specified in the path parameter |
| Optional:<br><br>count - sets the maximum results returned per request<br><br>exclude\_replies - removes replies from the results<br><br>Include\_rts - when set to 0 removes retweets from the results<br><br>trim\_user - removes rehydrated user objects from the results<br><br>tweet\_mode - sets the data format returned for the results, set to extended for Tweets longer than 140<br><br>since\_id - sets the earliest Tweet ID in result (exclusive)<br><br>max\_id - sets the latest Tweet ID in result (inclusive) | Optional:<br><br>max\_results - sets the maximum results returned per request<br><br>exclude=retweets,replies - removes Retweets or replies from the results<br><br>tweet.fields - sets the Tweet object fields to return<br><br>user.fields - sets the User object fields to return<br><br>place.fields - sets the place object fields to return<br><br>media.fields - sets the media object fields to return<br><br>poll.fields - sets the poll object fields to return<br><br>expansions - sets the expanded fields and data to return<br><br>start\_time - sets the earliest created\_at time for the results<br><br>end\_time - sets the latest created\_at time for the results<br><br>since\_id - sets the earliest Tweet ID for the  results (exclusive)<br><br>until\_id - sets the latest Tweet ID in result (exclusive) |

**Response data format**

|     |     |
| --- | --- |
| **Standard search v1.1** | **Search Tweets v2** |
| \[<br>    {tweet object},<br>    {tweet object}<br>  \] | {<br>  "data": \[{id,text},{id,text}\],<br>  "meta": {<br>    "oldest\_id": "1337085692623646724",<br>    "newest\_id": "1334183616172019713",<br>    "previous\_token": "77qpymm88g5h9vqkluldpw91lr0qzfz1sqydh841iz48k",<br>    "result\_count": 10,<br>    "next\_token": "7140dibdnow9c7btw3w29gqolns6a1ipl3kzeae41vsxk"<br>  }<br>} |

#### Twitter API v2 JSON format

Twitter API v2 is introducing new JSON designs for the objects returned by the APIs, including [Tweet](https://developer-staging.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) and [user](https://developer-staging.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) objects. You can learn more about the Twitter API v2 format, how to use fields and expansions by visiting our [guide](https://developer-staging.twitter.com/en/docs/twitter-api/data-dictionary/using-fields-and-expansions), and by reading through our broader [data dictionary](https://developer-staging.twitter.com/en/docs/twitter-api/data-dictionary)

* At the JSON root level, the standard endpoints return Tweet objects in a statuses array, while Twitter API v2 returns a data array. 
* Instead of referring to Retweeted and Quoted "statuses", Twitter API v2 JSON refers to Retweeted and Quoted Tweets. Many legacy and deprecated fields, such as contributors and user.translator\_type are being removed. 
* Instead of using both favorites (in Tweet object) and favorites (in user object), Twitter API v2 uses the term like. 
* Twitter is adopting the convention that JSON values with no value (for example, null) are not written to the payload. Tweet and user attributes are only included if they have a non-null value.  
     

One of the biggest differences between standard v1.1 and Twitter API v2 endpoint versions is how you select which fields return in your payload. For the standard endpoints, there are several parameters that you could use to identify which fields or sets of fields would return in the payload, while the Twitter API v2 version simplifies these different parameters into [fields](https://developer-staging.twitter.com/content/developer-twitter/en/docs/twitter-api/fields) and [expansions](https://developer-staging.twitter.com/content/developer-twitter/en/docs/twitter-api/expansions). 

* fields: Twitter API v2 endpoints enable you to select which fields are provided in your payload. For example, Tweet, user, Media, Place, and Poll objects all have a list of fields that can be returned (or not). 
* expansions: Used to expand the complementary objects referenced in Tweet JSON payloads. For example, all Retweets and Replies reference other Tweets. By setting expansions=referenced\_tweets.id, these other Tweet objects are expanded according to the tweet.fields setting.  Other objects such as users, polls, and media can be expanded. 

* conversation\_id
* Two new [annotations](https://developer-staging.twitter.com/en/docs/twitter-api/annotations) fields, including context and entities
* Several new [metrics](https://developer-staging.twitter.com/en/docs/twitter-api/metrics) fields   
     

We have put together a [data format migration guide](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats/standard-v1-1-to-v2) which can help you map standard v1.1 fields to the newer v2 fields. This guide will also provide you the specific expansion and field parameter that you will need to pass with your v2 request to return specific fields.