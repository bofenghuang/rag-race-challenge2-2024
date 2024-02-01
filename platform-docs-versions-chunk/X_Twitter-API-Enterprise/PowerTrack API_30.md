platform: X
topic: Twitter-API-Enterprise
subtopic: PowerTrack API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/PowerTrack API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/powertrack_recovery_and_redundancy_features

## Recovering from disconnect 

Restarting and recovering from a disconnect involves several steps:

* Determining length of disconnect time period.
    * 5 minutes or less?
        * If you have Backfill enabled for stream, prepare connection request with appropriate ‘backfillMinutes’ parameter.
    * More than 5 minutes?
        * Make a connection request using 'startTime' and 'endTime' request parameters in order to start a recovery stream. The streaming recovery feature allows you to have an extended backfill window of 24 hours. Recovery enables you to 'replay' the time period of missed data.
* Request a new connection.