platform: X
topic: Twitter-API-Enterprise
subtopic: Usage API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Usage API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/usage-api/api-reference/get-usage

get-usage

get-usage

## Methods [¶](#methods- "Permalink to this headline")

| Method | Description |
| --- | --- |
| [GET /metrics/usage/accounts/{ACCOUNT\_NAME}.json](#GETData) | Retrieve usage data |

Where:

* :account\_name is the (case-sensitive) name associated with your account, as displayed at console.gnip.com

## Authentication and Rate Limit [¶](#authentication-and-rate-limit- "Permalink to this headline")

#### Authentication

All requests to the Usage API require HTTP Basic Authentication, using any of the email/password credentials enabled on your account to log into your account at console.gnip.com or connect to any Gnip stream.

#### Rate Limit

The Usage API enforces a rate limit of two requests per minute.