platform: X
topic: Twitter-API-V2
subtopic: Compliance
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Compliance.md
url: https://developer.twitter.com/en/docs/twitter-api/compliance/streams/integrate/integrating-compliance-streams

## Integrating the compliance streams

To integrate the compliance streams into your system, you will need to build an integration that can do the following:

1. Establish a streaming connection to each streaming endpoint partition of the compliance streams. The Tweet and User streams are both split into 4 partitions, and a connect must be established for each partition. 
2. Handle high data volumes – de-couple stream ingestion from additional processing using asynchronous processes
3. Reconnect to the stream partitions automatically when disconnected for any reason. After a disconnection, reconnect using the 'backfill\_minutes' request parameter to avoid missing any events. Your system needs to be tolerant of duplicate events. 
4. Process compliance events that are relevant to Tweet and User data you have stored in accordance with the guidance presented above