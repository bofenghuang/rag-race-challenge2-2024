platform: X
topic: Twitter-API-Enterprise
subtopic: Decahose API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Decahose API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/decahose-api/guides/recovery-and-redundancy


## Introduction 

With streaming high volumes of realtime Tweets comes a set of best practices that promote both data reliability and data full-fidelity. When consuming realtime data, maximizing your connection time is a fundamental goal. When disconnects occur, it is important to automatically detect that and reconnect. After reconnecting it’s important to assess if there are any periods to backfill data for. The component that manages these details and consumes realtime Tweets is only one part of a system with network, datastore, server, and storage concerns. Given the complexity of these systems, another best practice is to have different streaming environments, with at least separate streams for development/testing and production.

Decahose comes with a set of features that help with these efforts.

1. To support multiple environments, we can deploy [Additional Streams](#AdditionalStreams) for your account. These streams are independent of each other and have a different stream\_label  to help differentiate them.
2. To help support maintaining a connection, each Decahose stream supports [Redundant Connections](https://developer.twitter.com/en/docs/twitter-api/enterprise/decahose-api/guides/recovery-and-redundancy.html#RedundantConnections). The most common architecture is for a stream to have two connections, and on the client-side there are two independent consumers –ideally on different networks. With this design, there can be redundancy across the client-side networks, servers, and datastore pathways. Note that a full-copy of the data is served on each connection and the client-side must be tolerant of and manage duplicate data.
3. A '**heartbeat**' will be provided every 10 seconds; however, with the Decahose stream, the volume of data is high enough that even a small duration (e.g., a few seconds) of no Tweets can indicate a connection issue. Therfore, both a 'data silence' and lack of a heartbeat can be used to detect a disconnect.

Since disconnects will happen, the Decahose stream has a dedicated [Recovery](https://developer.twitter.com/en/docs/tweets/sample-realtime/guides/recovery-and-redundancy#Replay) and a [Backfill](https://developer.twitter.com/en/docs/tweets/sample-realtime/guides/recovery-and-redundancy#Backfill) feature to help recover data that was missed due to disconnections and other operational issues.