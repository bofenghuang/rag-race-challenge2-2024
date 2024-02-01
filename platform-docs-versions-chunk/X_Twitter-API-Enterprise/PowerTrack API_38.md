platform: X
topic: Twitter-API-Enterprise
subtopic: PowerTrack API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/PowerTrack API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/faq


### Realtime PowerTrack API

**I am interested in Twitter data and would like to find out approximate subscription costs.**

Please fill out [this form](https://developer.twitter.com/en/enterprise-application) to get in touch with our Sales team.  
 

**What are some of the features provided by realtime PowerTrack?**  

By connecting directly to our data services, you can take advantage of many enterprise-ready features that provide reliable connectivity and full-fidelity data. As an enterprise licensed-access offering, realtime PowerTrack includes tools for dynamic filtering, consistent connection, data recovery and data compliance management. This technology, paired with operational monitoring, guaranteed support and integration services allows businesses to start with a strong foundation to serve their own customers.

These features include:

* Dynamic rule updates while connected to the stream. There is no need to disconnect your stream while you update your stream’s ruleset.
* Support for multiple connections to each stream.
* Ability to automatically recover data that is missed during brief disconnects when you reconnect within 5 minutes with Backfill.
* Availability of Recovery feature to recover missed data within the last 24 hours if you are unable to reconnect with the 5 minute backfill window.
* Availability of additional streams for testing and development.
* Status dashboard to communicate with customers about any operational issues.  
     

**How do I consume streaming data?**

Realtime streams of data are initiated by sending a HTTP GET command to your custom `https://gnip-stream.twitter.com` URL. HTTP streaming connections are requested with HTTP headers that indicate a ‘keep-alive’ connection. More information on realtime streaming is available [here](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/overview).

Given the potential of high volumes of Twitter data delivered in a stream, it is highly recommended that incoming data is processed in an asynchronous fashion. What this means is that your code that ‘hosts’ the client side of the stream simply inserts incoming Tweets into a (FIFO) queue, or similar memory structure, and then you have a separate process/thread that consumes Tweets from that queue and does more of the ‘heavy lifting’ of parsing and preparing the data for storage. With this design, you can implement a process that will bend but not break in case incoming data volumes change dramatically.  
 

**How can multiple customers, projects, and campaigns be managed in a single stream?**

The vast majority of realtime PowerTrack users manage multiple customers, projects, and campaigns within a single realtime stream by using [PowerTrack rule ‘tags’](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/overview). Rule tags have no special meaning, they are simply treated as opaque strings carried along with the rule. They will be included in the “matching rules” metadata in activities returned.

Tags provide an easy way to create logical groupings of PowerTrack rules. For example, you may generate a unique ID for a specific rule as its tag and allow your application to reference that ID within activities it processes to associate a result with specific customers, campaigns, categories, or other related groups.  
 

**How many connections to a given PowerTrack stream can I have at one time?**

PowerTrack streams support multiple connections to a single endpoint. Having multiple connections enables customers to build redundant data consumer clients, ideally on different networks. While PowerTrack streams default to a single connection, many customers prefer to have two connections per PowerTrack stream to ensure continuous delivery. If multiple connections are made to a single endpoint, and/or multiple streams exist with common rules, a given Tweet will be received multiple times. Note that for accounting purposes, the Tweet will be counted once.

Please talk to your Account Manager for more information.  
 

**How 'realtime' are the results? Is there any delay/elaboration time between the publication of a Tweet on Twitter and their release on the PowerTrack stream?**

Tweets that match your ruleset will be delivered to your stream within seconds of being published on the platform. There are variables, such as network connectivity and how your consuming application reads data off the stream; but all things being equal, you should receive Tweets within seconds of them being published.

Please note that the URL enrichment does cause an increased latency, due to the unwinding of each URL in the Tweet. 

Generally speaking, you should expect Volume streams (e.g. Firehose and [Decahose](https://developer.twitter.com/en/docs/twitter-api/enterprise/decahose-api/overview)) to be faster than [PowerTrack](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/overview), and PowerTrack to be fast than [statuses/filter](https://developer.twitter.com/en/docs/tweets/filter-realtime/api-reference/post-statuses-filter).  
 

**Is it possible to update several rules in one go?**

Yes, you can add or delete several rules with one request.  
  
However, note that the add and delete steps are separate and you will need two requests: one request to add one or several rule(s) and another request to delete one or several rule(s).

The upper limit number of rules that can either be added or be deleted in one go is a JSON body that is 5MB or less in size. Depending on the length of your rule values and tags, the upper number will be in the lower thousands.  
 

**Why isn't my rule appearing on the stream right away?**

Most rule additions take effect almost immediately. However, depending on factors such as network connectivity and rule size/complexity, it may take up to 5 minutes before you start receiving matching Tweets.  
 

**What if some Tweets are missing: I was expecting them to be returned by the stream, but they weren't?**

You can follow the next few steps to understand why some Tweets might not have been delivered:

1. Check your [rule](https://developer.twitter.com/en/docs/twitter-api/enterprise/rules-and-filtering/enterprise-operators) and ensure that you are using the correct operators.
2. Were you connected to the stream when the Tweet was created? You can use the 'Connections' tab in the [console](https://console.gnip.com/) to check your connection history.
3. Was your rule already in place when the Tweet was created?
4. Note that if the account from which the Tweet was sent was private at the time the Tweet was created, the Tweet won't be returned - even if the account is public at the time of the request.
  

**If I lose the connection to the stream and then connect back, will I lose all Tweets from that duration?**

Yes, if you lose the connection to the stream, you may be missing data for the period of time that you were disconnected from the stream. Whenever a disconnection occurs, your client app must restart the process by establishing a new connection.

Additionally, to ensure that you do not miss any data, you may need to utilize a [Redundant Connection](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/powertrack_recovery_and_redundancy_features#redundant_connections), [Backfill](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/powertrack_recovery_and_redundancy_features#backfill), or a [Replay stream](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/api-reference/replay-stream) to mitigate or recover data from disconnections from the stream. Please see our answer to the next question for more information.  
 

**What if I get disconnected from the stream? How can I collect any data that was missed while disconnected?**

When streaming data, the goal is to stay connected for as long as possible, recognizing that disconnects will occur. PowerTrack streams provide a 15-second heartbeat (in the form of a new-line character) that enable client applications to detect disconnects. When fresh data and the heartbeat stop arriving, reconnection logic should be triggered. In most software languages this can be easily implemented by setting a data read timeout.

Any time you disconnect from the stream, you are potentially missing data that would have been sent if connected. However, there are multiple ways to mitigate these disconnects and recover data when they occur.

There is a range of tools available for retrieving historical tweets, including:

1. [Redundant Streams](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/powertrack_recovery_and_redundancy_features#redundant_connections) - With multiple connections, consume the stream from multiple servers to prevent missed data when one is disconnected.
2. [Recovery](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/api-reference/replay-stream) - Recover data within the last 24 hours.
3. [Backfill](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/powertrack_recovery_and_redundancy_features#backfill) - Reconnect within 5 minutes and start from where you left off.
4. [Full Archive Search](https://developer.twitter.com/en/docs/twitter-api/enterprise/search-api/quick-start/enterprise-full-archive) - Recover data from the entire Twitter archive.

  
Please also refer to [our documentation on disconnects](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/disconnections-explained).  
 

**How fast is the streaming speed of Recovery?**

Recovery will deliver up to 1000 posts per second. It is intended to deliver the posts for the period of time that a customer is disconnected.

**Do you have any realtime PowerTrack code examples I can use to get started with?**

Yes, we have several realtime code examples available, including:

* [Sample Python scripts](https://github.com/twitterdev/python-enterprise-scripts/blob/master/python_stream_sample.py)
* [Sample Ruby scripts](https://github.com/twitterdev/ruby-enterprise-scripts/tree/master/PowerTrack)

Note that these are only available to enterprise customers.

**How do Edit Tweets impact my usage and billing?**   

Only the original Tweet will count for billing purposes. Any subsequent edits will be ignored and not contribute to your overall activity count.