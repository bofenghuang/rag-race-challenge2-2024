platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/quick-replies/overview

Overview

Messages published with [POST direct\_messages/events/new (message\_create)](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/new-event) can have an attached Quick Reply to request stuctured input from a user.

[Quick Reply Options API reference](https://developer.twitter.com/en/docs/direct-messages/quick-replies/api-reference/options)List of up to 20 predefined options presented for a user to choose from.

Quick Reply attachment metadata will not be accessible via legacy REST and Streaming endpoints. Only text values will be delivered in the legacy Direct Message JSON format.