platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/volume-streams/integrate/recovery-and-redundancy-features


### Recovering missed data after a disconnection: Backfill

After you've detected a disconnection, your system should be smart enough to reconnect to the stream. If possible, your system should take note of how long the disconnection lasted so that you can use the proper recovery feature to backfill the data. 

If you are using a Project with Academic Research access and identified that the disconnection lasted five minutes or less, you can use the backfill parameter, backfill\_minutes. If you pass this parameter with your [GET /tweets/sample/stream](https://developer.twitter.com/en/docs/twitter-api/tweets/sampled-stream/api-reference/get-tweets-sample-stream) request, you will receive the Tweets that match your rules within the past one to five minutes. We generally deliver these older Tweets first before any newer sampled Tweets, and also do not deduplicate Tweets. This means that if you were disconnected for 90 seconds, but request two minutes worth of backfill data, you will receive 30 seconds worth of duplicate Tweets, which your system should be tolerant of. Here is an example of what a request might look like with the backfill parameter:

      `curl 'https://api.twitter.com/2/tweets/sample/stream?backfill_minutes=5' -H "Authorization: Bearer $BEARER_TOKEN"`
    

  
If you don't have access to the Enterprise access, or identified that the disconnection time lasted for longer than five minutes, you can try to utilize the [recent search endpoint](https://developer.twitter.com/en/docs/twitter-api/tweets/search/introduction) to request missed data. However, note that the search Tweets endpoints do not include the sample: operator, so requesting a random sample of data is not possible.