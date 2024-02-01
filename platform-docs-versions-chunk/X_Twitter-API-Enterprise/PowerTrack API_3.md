platform: X
topic: Twitter-API-Enterprise
subtopic: PowerTrack API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/PowerTrack API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/overview


### Core components

The PowerTrack API consists of two endpoints:

#### Rules endpoint

A separate endpoint managed independently by your application, the rules endpoint supports GET, POST, POST \_method=delete and rule validation methods with basic authentication for managing your ruleset. It can support thousands of rules that allow you to filter the realtime stream of data for the topics and conversations that you care about. The rules endpoint can be accessed, managed, and will persist regardless of your connection status to the stream - you can also update (add/remove) rules while connected to the stream and the changes will take effect almost immediately.

#### Stream endpoint

Connecting to the streaming endpoint consists of a simple [GET](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/api-reference/powertrack-stream) request using basic authentication. Once a connection is established, data is delivered in JSON format (see sample payload below) through a persistent HTTP Streaming connection. You will only receive data matching your rules while connected to the stream.

#### Rule tags

A single PowerTrack stream can support thousands of rules, so being able to discern which rule(s) matched a given Tweet becomes important. This is easily solved by using rule tags. Upon rule creation, you can assign a tag value which will be returned in the matching\_rules object ([see here](https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/matching-rules.html)) of the response payload.

Rule tags can represent an end customer use case, a topic or conversation, or another helpful identifier that you can use to route incoming Tweets accordingly.

If, in addition to realtime data, your product also requires instant access to recent data, we recommend using our [Search API](https://developer.twitter.com/en/docs/twitter-api/search-overview).