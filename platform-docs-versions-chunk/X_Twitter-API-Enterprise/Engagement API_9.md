platform: X
topic: Twitter-API-Enterprise
subtopic: Engagement API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Engagement API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/engagement-api/guides/dev-getting-started-engagement-api


### Integrating the Engagement API

#### Introduction to API

The Engagement API is a simple RESTful API that receives requests encoded in JSON and responds with engagement metrics encoded in JSON. Requests consist three main parts (follow links for more documentation):

* Array of **_Tweet IDs_**.
* Array specifying the [metric types](https://developer.twitter.com/en/docs/metrics/get-tweet-engagement/overview.html#EngagementTypes) of interest. Types include things such as ‘impressions’, ‘retweets’, ‘hashtag\_clicks’, and ‘user\_follows’.
* [Engagement groupings](https://developer.twitter.com/content/developer-twitter/en/docs/metrics/get-tweet-engagement/guides/grouping-results), which is a JSON structure indicating how you want the engagement data arranged in the API response.

  
In many situations, the Engagement Types and Groupings will remains relatively constant from request to request, with only the Tweet IDs being updated.

The Engagement API provides [three endpoints](https://developer.twitter.com/en/docs/metrics/get-tweet-engagement/overview.html#RequestEndpoints):

* **Totals** - Provides grand totals of engagements for Tweets. Some metrics are available for all Tweets, while others are only available for the past 90 days.
* **28 hour** - Provides time-series engagement metrics from the last 28 hours.
* **Historical** - Provides time-series engagement metrics for up to four consecutive weeks for Tweets posted since September 1, 2014.

  
The **/totals** endpoint supports requesting metrics for up to **250 Tweets per request**. The **/28hour** and **/historical** endpoints support **25 per request**.

After discussing getting access to the Engagement API, we’ll walk through making an API request, provide an OAuth overview, and provide links to other technical resources.

#### Getting API access

If you are reading this document, you have most likely already obtained access to the Engagement API. If not, please reach out to your Enterprise account manager, or apply for Enterprise access [here](https://developer.twitter.com/content/developer-twitter/en/enterprise-application).

The first step is creating a [Twitter app](https://developer.twitter.com/content/developer-twitter/en/docs/basics/developer-portal/guides/apps) using an approved developer account via the [developer portal](https://developer.twitter.com/content/developer-twitter/en/docs/basics/developer-portal/overview).  Your account manager will need the numeric App ID associated with this application to provide access. If you need to apply for a developer account, you can do so [here](https://developer.twitter.com/content/developer-twitter/en/apply).

#### Making a request

The good news is that making requests to the Engagement API is simple. For our request, we’ll ask it for total Retweets, Quote Tweets, Favorites, and replies, for the following two [@TwitterDev](https://twitter.com/TwitterDev) Tweets:

> 1/ Today we’re sharing our vision for the future of the Twitter API platform![https://t.co/XweGngmxlP](https://t.co/XweGngmxlP)
> 
> — Twitter Dev (@TwitterDev) [April 6, 2017](https://twitter.com/TwitterDev/status/850006245121695744)

> Don’t miss the Tweets about your Tweet.  
>   
> Now on iOS, you can see Retweets with comments all in one place. [pic.twitter.com/oanjZfzC6y](https://t.co/oanjZfzC6y)
> 
> — Twitter (@Twitter) [May 12, 2020](https://twitter.com/Twitter/status/1260294888811347969?ref_src=twsrc%5Etfw)

The first step is constructing the API request in JSON, consisting of these two Tweet IDs placed in an array, an array of engagement types of interest, and a custom-named “groupings” JSON object that indicates how we want the metrics arranged in the response. Here is what our request looks like:  

      `{   "tweet_ids": [     1260294888811347969, 850006245121695744   ],   "engagement_types": [     "retweets", "quote_tweets", "favorites", "replies"   ],   "groupings": {     "engagement-types-by-id": {       "group_by": [         "Tweet.id", "engagement.type"       ]     }   } }`
    

To retrieve these total metrics, we POST this JSON request to the https://data-api.twitter.com/insights/engagement/totals endpoint.

We’ll include the following headers to indicate that our request is encoded in JSON, and that it is Gzipped (request bodies can get big):

* Content-Type: application/json
* Accept-Encoding: gzip  
     

When making requests we authenticate using OAuth, which we’ll discuss more in the next section.

The API returns the following payload:

      `{   "grouping name": {     "1260294888811347969": {       "favorites": "17111",       "quote_tweets": "3254",       "replies": "1828",       "retweets": "5218"     },     "850006245121695744": {       "favorites": "492",       "quote_tweets": "66",       "replies": "42",       "retweets": "324"     }   } }`
    

  
Note that the response has our requested metrics in the structure described by the “groupings” definitions, with metrics listed by Tweet ID first, then by engagement type on the next level.

That was pretty simple. If you are new to authenticating with OAuth, check out the next section.