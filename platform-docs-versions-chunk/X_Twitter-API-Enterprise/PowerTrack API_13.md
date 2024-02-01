platform: X
topic: Twitter-API-Enterprise
subtopic: PowerTrack API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/PowerTrack API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/connecting

Connecting to a streaming endpoint

# Connecting to a streaming endpoint

Establishing a connection to the streaming APIs means making a very long lived HTTP request, and parsing the response incrementally. Conceptually, you can think of it as downloading an infinitely long file over HTTP.

## Authentication

The following authentication methods are supported by the Streaming APIs:

|     |     |     |
| --- | --- | --- |
| Auth Type | Supported APIs | Description |
| [OAuth](https://developer.twitter.com/en/docs/basics/authentication/overview) | * Track API Stream | Requests must be authorized [according to the OAuth specification](https://developer.twitter.com/content/developer-twitter/en/docs/authentication) . |
| [Basic auth](https://developer.twitter.com/en/docs/basics/authentication/overview/basic-auth.html) | * PowerTrack API<br>* Decahose stream | Requests must use of HTTP Basic Authentication, constructed from a valid email address and password combination. |