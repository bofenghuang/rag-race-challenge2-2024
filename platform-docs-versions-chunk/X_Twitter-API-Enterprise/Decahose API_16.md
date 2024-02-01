platform: X
topic: Twitter-API-Enterprise
subtopic: Decahose API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Decahose API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/decahose-api/api-reference/decahose

Decahose stream

decahose

# Decahose stream

Jump to on this page

[Methods](#Methods)

[Authentication](#Authentication)

[GET /{stream-type}/:stream](#Stream)

[Replay API](#replay_api)

## Methods [¶](#methods- "Permalink to this headline")

| Method | Description |
| --- | --- |
| [GET /{stream-type}/:stream](#Stream) | Connect to the data stream |

## Authentication [¶](#authentication- "Permalink to this headline")

All requests to the Volume Stream APIs must use HTTP Basic Authentication, constructed from a valid email address and password combination used to log into your account at console.gnip.com. Credentials must be passed as the Authorization header for each request. So confirm that your client is adding the "Authentication: Basic" HTTP header (with encoded credentials over HTTPS) to all API requests.