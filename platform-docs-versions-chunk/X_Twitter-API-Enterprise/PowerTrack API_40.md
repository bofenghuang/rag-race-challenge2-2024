platform: X
topic: Twitter-API-Enterprise
subtopic: PowerTrack API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/PowerTrack API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/api-reference/powertrack-stream

PowerTrack API

powertrack-stream

# PowerTrack API

Jump to on this page

[Methods](#Methods)

[Authentication](#Authentication)

[GET /track/:stream](#Stream)

## Methods [¶](#methods- "Permalink to this headline")

| Method | Description |
| --- | --- |
| [GET /track/:stream](#Stream) | Connect to the data stream |

## Authentication [¶](#authentication- "Permalink to this headline")

All requests to the PowerTrack API must use HTTP Basic Authentication, constructed from a valid email address and password combination used to log into your account at console.gnip.com. Credentials must be passed as the Authorization header for each request. Make sure your client is adding the "Authentication: Basic" HTTP header (with encoded credentials over HTTPS) to all API requests.