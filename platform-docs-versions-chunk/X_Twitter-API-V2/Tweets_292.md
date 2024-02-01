platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/volume-streams/integrate/handling-disconnections

Handling disconnections

## What is a disconnection?

Establishing a connection to the streaming APIs means making a very long lived HTTPS request, and parsing the response incrementally. When connecting to the sampled stream endpoint, you should form a HTTPS request and consume the resulting stream for as long as is practical. Our servers will hold the connection open indefinitely, barring server-side error, excessive client-side lag, network issues, routine server maintenance, or duplicate logins. With connections to streaming endpoints, it is likely, and should be expected, that disconnections will take place and reconnection logic built.