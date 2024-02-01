platform: X
topic: Twitter-API-Enterprise
subtopic: Compliance Firehose API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Compliance Firehose API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/compliance-firehose-api/api-reference/compliance-firehose

GET compliance/firehose

compliance-firehose

# GET compliance/firehose

Jump to on this page

[Methods](#Methods)

[Authentication](#Authentication)

[GET /compliance/:stream](#Connect)

[Response Codes](#ResponseCodes)

[Other Recommendations & Best Practices](#OtherRecommendations)

## Methods [¶](#methods- "Permalink to this headline")

| Method | Description |
| --- | --- |
| [GET /compliance/:stream](#Connect) | Connect to the Data Stream |

## Authentication [¶](#authentication- "Permalink to this headline")

All requests to the Compliance Firehose API must use HTTP Basic Authentication, constructed from a valid email address and password combination used to log into your account at console.gnip.com. Credentials must be passed as the Authorization header for each request.