platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/migrate/powertrack-api-migration-to-twitter-api-v2


### Differences

#### Rule length  

Rule length is measured the same way (by character count) for both PowerTrack and filtered stream rules, however the maximum length for PowerTrack rules is 2048 characters and the maximum rule length for rules on Twitter API v2 filtered stream varies by [access level](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level). 

Essential and Elevated access - 512 characters  
Academic Research access - 1024 characters  
Enterprise access - 2048 characters 

#### Rule volume

The PowerTrack maximum rule volume per stream is defined within the enterprise account contract.  Twitter API v2 filtered stream rule volume varies by [access level](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level).

Essential access - 5 rules  
Elevated access - 25 rules  
Academic research access - 1000 rules  
Enterprise access - 2500+ rules  
 

#### Endpoint URLs

* PowerTrack endpoints:
    * https://gnip-stream.twitter.com/stream/powertrack/accounts/{account\_name}/publishers/twitter/{stream\_label}.json
    * https://gnip-api.twitter.com/rules/powertrack/accounts/{account\_name}/publishers/twitter/{stream\_label}.json
    * https://gnip-api.twitter.com/rules/powertrack/accounts/{account\_name}/publishers/twitter/{stream\_label}/validation.json
* Twitter API v2 endpoint:
    * https://api.twitter.com/2/tweets/search/stream
    * https://api.twitter.com/2/tweets/search/stream/rule

####   
App and Project requirements for v2 access

PowerTrack access is granted through a contracted annual subscription for data, and set up through console.gnip.com by your account manager at Twitter.  PowerTrack does not require a Twitter developer App to access.  In order to use the Twitter API v2 filter stream, you must have [signed up for a Twitter developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info), and a Twitter [developer App](https://developer.twitter.com/en/portal/projects-and-apps.html) associated with a Project. The developer App and Project setup for Twitter API v2 access is all done through the [developer portal](https://developer.twitter.com/en/portal/projects-and-apps).  

#### Authentication method

The PowerTrack API endpoints use Basic Authentication set up in console.gnip.com. The Twitter API v2 filtered stream endpoints require a Twitter developer App and an [OAuth 2.0 App Access Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0) (also referred to as Application-only or Bearer Authentication). To make requests to the Twitter API v2 version you must use your specific developer App's Access Token to authenticate your requests.

In the process of setting up your developer account, developer App and Project, an App Access Token is created and shared within the dev portal user interface, however, you can generate a new one by navigating to your app's “Keys and tokens” page on the [developer portal](https://developer.twitter.com/en/portal/projects-and-apps). If you’d like to generate/destroy the App Access Tokens programmatically, see this [OAuth 2.0 App-Only guide](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only.html).

#### Usage tracking

PowerTrack usage can be retrieved programatically using the Usage API, or can be seen in console.gnip.com on the [usage tab](https://developer.twitter.com/en/docs/twitter-api/enterprise/console/usage.html).  Tweet consumption across all PowerTrack streams is deduplicated each day and volume consumption is defined within the enterprise contract. 

Twitter API v2 filtered stream usage can be tracked within the developer portal at the Project level.  Tweet consumption is [set at the Project level](https://developer.twitter.com/en/docs/projects/overview.html) and is shared across several different Twitter API v2 endpoints, including filtered stream, recent search, user Tweet timeline and user mention timeline.  Currently with Basic Access, the monthly Tweet consumption limit is 500,000 Tweets per month total, and Tweets are not deduplicated across products or time.

#### Multiple streams, redundant conections, backfill and Replay API for recovery

There are several recovery and redunancy features available via PowerTrack, some of which are not yet available for Twitter API v2 filtered stream.  For PowerTrack, all [recovery and redundancy features](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/powertrack_recovery_and_redundancy_features.html) are configured within the enterprise contract. PowerTrack API currently has the flexibility to offer multiple PowerTrack streams (commonly "dev" and "production") with unique rulesets.  Currently, the Twitter API v2 filtered stream is only available with a single stream.

PowerTrack allows you to connect to have multiple connections to a single stream, generally used for redundant connections to different data centers or clients. If you have [Academic Research access](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level), you will have access redundant connections, enabling you to make up to two connections to a single stream.

If a PowerTrack stream is disconnected breifly, a reconnection can be made using the backfillMinutes parameter to reduce the chance of data loss within five minutes of the disconection. While we have added this functionality to the Twitter API v2 version, it is currently only available with Academic Research access, and has been renamed to backfill\_minutes.

If a PowerTrack stream is disconnected for longer than a 5 minute period, the separate [Replay API](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/api-reference/replay-stream.html) can be used to recover data for up to a 2 hour period in the recent 5 day past.  Currently, the Twitter API v2 filtered stream does not have a replay feature.

#### Request parameters and response format

One of the biggest differences between PowerTrack API and Twitter API v2 filtered stream is the parameter functionality.

Using the Twitter API v2 filtered stream, there are several parameters used on the connection request to identify which fields or expanded objects to return in the Tweet payload.  This is common for all v2 endpoints. By default, only the Tweet id and text are returned for matching Tweets but additional parameters, fields and expansions described below, can be added in order to recieve more detailed data per matching Tweet. 

fields: Twitter API v2 endpoints enable you to select which fields are provided in your payload. For example, Tweet, User, Media, Place, and Poll objects all have a list of fields that can be returned (or not). 

expansions: Used to expand the complementary objects referenced in Tweet JSON payloads. For example, all Retweets and Replies reference other Tweets. By setting expansions=referenced\_tweets.id, these other Tweet objects are expanded according to the \`tweet.fields\` setting.  Other objects such as users, polls, and media can be expanded.

https://api.twitter.com/2/tweets/search/stream?tweet.fields=created\_at,public\_metrics,author\_id,entities&expansions=attachments.poll\_ids

You can learn more about how to use fields and expansions by visiting our [guide](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/using-fields-and-expansions), and by reading through our broader [data dictionary](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction).

|     |     |
| --- | --- |
| **Connection to PowerTrack** | **Example request to Twitter API v2 filtered stream** |
| curl --compressed -v -uexample@customer.com "https://gnip-stream.twitter.com/stream/powertrack/accounts/:account\_name/publishers/twitter/:stream\_label.json" | curl "https://api.twitter.com/2/tweets/search/stream?tweet.fields=attachments,author\_id,context\_annotations,conversation\_id,created\_at,entities,geo,id,in\_reply\_to\_user\_id,lang,possibly\_sensitive,public\_metrics,referenced\_tweets,reply\_settings,source,text,withheld&user.fields=created\_at,description,entities,id,location,name,pinned\_tweet\_id,profile\_image\_url,protected,public\_metrics,url,username,verified,withheld&expansions=author\_id,referenced\_tweets.id,referenced\_tweets.id.author\_id,entities.mentions.username,attachments.poll\_ids,attachments.media\_keys,in\_reply\_to\_user\_id,geo.place\_id&place.fields=contained\_within,country,country\_code,full\_name,geo,id,name,place\_type&poll.fields=duration\_minutes,end\_datetime,id,options,voting\_status" -H "Authorization: Bearer $ACCESS\_TOKEN" |

The PowerTrack API data format is set within console.gnip.com at the stream settings level, which can be set to either the Twitter [native enriched format](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/tweet.html) or [Activity streams format](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/activity.html). 

PowerTrack API only uses one optional parameter on connection, to reconnect using backfill (backfillMinutes=5). This optional parameter is also available to filtered stream, but is called backfill\_minutes, and is only available via Academic Research access.  
 

https://gnip-stream.twitter.com/stream/powertrack/accounts/{account\_name}/publishers/twitter/{stream\_label}.json?backfillMinutes=5

#### Response structure and data format

As described above, the request parameters set at the connection request for Twitter API v2 filtered stream determine the response data returned.  There are several different response possibilites using different fields and expansions which can range from the most simple default response with only the Tweet id and text, to an extremely detailed and expanded data payload.

The data format for PowerTrack is set within console.gnip.com at the stream settings level, which can be set to either the Twitter Native Enriched format or Activity Streams format. 

The following table references Tweet response examples in each different format:

|     |     |     |
| --- | --- | --- |
| **Native enriched format** | **Activity streams format** | **Twitter API v2 filtered stream format** |
| [Payload examples](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/enriched-native-example-payloads) | [Payload examples](https://developer.twitter.com/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/example-payloads.html) | [Payload examples](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/example-payloads.html) |

If you would like to know more about how the enterprise data formats map to the Twitter API v2 format, please visit our following guides:

* [Native Enriched to Twitter API v2 format migration guide](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats/native-enriched-to-v2)
* [Activity Streams to Twitter API v2 format migration guide](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats/activity-streams-to-v2)