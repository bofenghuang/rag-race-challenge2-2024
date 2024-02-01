platform: X
topic: Twitter-API-Enterprise
subtopic: PowerTrack API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/PowerTrack API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/disconnections-explained


### Forced disconnects  

At the highest level, forced disconnects happen when Twitter actively closes your connection to the stream. These can happen for a variety of reasons, and when you are force disconnected from your stream then Twitter will send a zero byte chunk in accordance with [HTTP chunked encoding practice](http://www.httpwatch.com/httpgallery/chunked/). In all cases of forced disconnects, you should be able to reconnect to the stream immediately and you should be sure to have [reconnect logic](https://developer.twitter.com/en/docs/tutorials/consuming-streaming-data#reconnecting) written into your code to prevent further data loss.

There are three types of forced disconnects that your app will need to be prepared for.  
 

#### **Twitter maintenance**

Twitter deploys for ongoing maintenance several times a week. During these updates, sometimes customer streams will experience one or more disconnects. This will be accompanied by a “Twitter is closing for operational reasons” message. These should be expected disconnections, and your application should be able to reconnect immediately, so make sure that you have [reconnect logic](https://developer.twitter.com/en/docs/tutorials/consuming-streaming-data#reconnecting) written into your application.  
 

#### **Full buffer disconnect**

A full buffer disconnect generally indicates that your application’s code isn’t keeping up with the amount of data that we’re streaming to you and there is a backup of cached data on the Twitter server side for your connection which needs to be flushed. This can happen after a major rule change, a [big event](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/high-volume-social-data-events), or simply because your application is having trouble [consuming the stream](https://developer.twitter.com/en/docs/tutorials/consuming-streaming-data). Full buffer disconnects are triggered when your stream connection buffer hits a certain threshold of Tweets. If you are disconnected for a full buffer, reconnecting with [backfill](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/powertrack_recovery_and_redundancy_features.html#backfill) is not available and data will begin streaming from the time you reconnect. It's likely that you will need to run a [Recovery](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/powertrack_recovery_and_redundancy_features#replay) to recover Tweets lost in the disconnection. If you find that full buffer disconnects are happening frequently, reach out to the support team to assist you in making sure that your application is properly configured. 

Here are some suggestions to prevent these kinds of disconnects from occurring in the future:

1. Ensure nothing is slowing down the process reading from the stream. Do not do any processing in the process/thread that is reading from the stream. Instead, have this process read the message then pass off any processing (such as parsing, date calculations, etc) of the message to a separate process or thread.
2. Verify there are no network issues between your application and Twitter preventing messages from being sent.
3. Make sure you have sufficient bandwidth for the volume of activities on your stream.  Some streams can have high volumes requiring significant bandwidth (~10 Mbps is not unheard of). Keep in mind these streams require this bandwidth to be sustained 24 hours a day, including spikes that may cause 2-3 times the volume during significant world events. These spikes are often absorbed by Twitter's buffer, and are one of the reasons it is in place.  
     

#### **Too many connections**

Each stream is configured to allow for a specified number of connections. This number is determined between you and your account manager, and is available in your account agreement. If you connect to your stream with more connections than are allowed, you will be force disconnected. Any extra connections are allowed for approximately one minute. If after one minute an extra connection exists, the most recent connection is forced disconnected. Allowing an extra connection for a minute enables the customer to, for example, spin up a new server and connect with it, then teardown a server that is being ‘retired.’