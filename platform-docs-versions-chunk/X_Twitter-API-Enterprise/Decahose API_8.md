platform: X
topic: Twitter-API-Enterprise
subtopic: Decahose API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Decahose API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/decahose-api/overview/streaming-likes


## Compliance guidance

* Compliance only possible via Gnip Compliance Firehose
* If a tweet is deleted, all likes associated with that Tweet should be deleted (just like its Retweets)
    * We will not deliver individual delete events for each Like in this scenario
* If a user protects/deletes his/her account, all likes performed by that user should be scrubbed (just like their Retweets)
    * We will not deliver individual delete events for each like in this scenario
* If a user protects/deletes his/her account, all likes of that user’s Tweets should be scrubbed (just like their Tweets and Retweets)
    * We will not deliver individual delete events for each like in this scenario
* If a user scrubs their geo, all likes associated with their Tweets should have its geo scrubbed (because the payload contains their original Tweet)
* If a user removes a like they performed (aka unliked), this is equivalent to a delete of that like and that like should be deleted.
    * We will deliver an event in the Compliance Firehose to reflect these like deletions
    * These like delete events will not include an ID for the original like event and will instead include the TweetID that was liked and the User that performed that like (a user can only like a Tweet once at a time)