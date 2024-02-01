platform: X
topic: Twitter-API-Enterprise
subtopic: PowerTrack API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/PowerTrack API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/api-reference/replay-stream

Replay API

replay-stream

# Replay API

Jump to on this page

[Methods](#Methods)

[Authentication](#Authentication)

[GET /replay](#Stream)

## Methods [¶](#methods- "Permalink to this headline")

| Method | Description |
| --- | --- |
| [GET /replay/:stream\_type](#Stream) | Connect to the replay stream. For realtime PowerTrack, the Stream Type is 'powertrack'. For Volume Streams, Stream Types include 'sample10' (i.e. decahose), 'firehose', 'mentions', and 'compliance'. |

* * *

## Authentication [¶](#authentication- "Permalink to this headline")

All requests to the Replay API must use HTTP Basic Authentication, constructed from a valid email address and password combination used to log into your account at console.gnip.com. Credentials must be passed as the Authorization header for each request.

* * *