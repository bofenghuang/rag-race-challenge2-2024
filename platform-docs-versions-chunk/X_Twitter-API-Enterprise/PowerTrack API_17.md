platform: X
topic: Twitter-API-Enterprise
subtopic: PowerTrack API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/PowerTrack API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/connecting

## Reconnecting

Once an **established** connection drops, attempt to reconnect immediately. If the reconnect fails, slow down your reconnect attempts according to the type of error experienced:

* Back off linearly for **TCP/IP level network errors**. These problems are generally temporary and tend to clear quickly. Increase the delay in reconnects by 250ms each attempt, up to 16 seconds.
* Back off exponentially for **HTTP errors** for which reconnecting would be appropriate. Start with a 5 second wait, doubling each attempt, up to 320 seconds.
* Back off exponentially for **HTTP 420 errors**. Start with a 1 minute wait and double each attempt. Note that every HTTP 420 received increases the time you must wait until rate limiting will no longer will be in effect for your account.