platform: X
topic: Twitter-API-Enterprise
subtopic: Decahose API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Decahose API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/decahose-api/guides/recovery-and-redundancy


## Recovering from Disconnect 

Restarting and recovering from a disconnect involves several steps:

* Determining length of disconnect time period.
    * 5 minutes or less?
        * If you have Backfill enabled for stream, prepare connection request with appropriate ‘backfillMinutes’ parameter.
    * More than 5 minutes?
        * If you have a Recovery stream, make a Recovery request for the disconnected time period (ideally with your current realtime rule set, using the Rules API if necessary).
* Request a new connection.

When you experience disconnects or downtime, here are strategies to mitigate and recover in this scenario:

1. **Implement backfill**  
    Backfill lets you reconnect from a point prior to disconnecting from a stream connection, and covers disconnects of up to 5 minutes. It is implemented by including a parameter in the connection request.
    
2. **Consume a redundant stream from another location**  
    If the redundant stream can be streamed into the same live environment, deduplicating data, you will eliminate the need for recovery unless BOTH the normal stream and redundant stream experience simultaneous downtime or disconnects. If the redundant stream cannot be streamed live into the production environment, it can be written into a separate “emergency” data store. Then, in the event of disconnects or downtime on the primary stream connection, your system will have data on hand to fill in your primary database for the period of time where data is missing
    
3. **Implement Recovery**  
    Where disconnects or downtime affect both the primary stream and redundant stream, use the Decahose Recovery to recover any data missed. The API provides a rolling window covering 5 days of the archive, and would be best utilized by requesting no more than an hour of that window at a time, and streaming it in. This is done in parallel to the realtime stream. Note that we do not have solutions for recovering Decahose data from beyond the 5 day window provided by Recovery, so it is important for you to utilize a redundant stream to ensure you have a complete copy of data on your side in the case of significant downtime on your side.
    

When you detect abnormal stored data volumes-   
Potential ways you can detect missing data where no disconnects or downtime occurred…

1. Count inbound Tweets  
    Your system should count the raw number of Tweets you receive at the very beginning of your ingestion app, and then provide a way to compare those numbers to the number of Tweets that reaches your final data store. Any differences can be monitored, and alert your team to issues causing data to be dropped after it is received.
    
2. Analyze for abnormal stored volumes  
    You may also want to analyze the volumes of stored data in your final database to look for abnormal drops. This can indicate issues as well, although there will likely be circumstances in which drops in volume are normal (e.g. if the Twitter platform is unavailable and people are not able to create Tweets for some period of time).