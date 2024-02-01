platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise

Enterprise Account Activity API

aaa-enterprise

# Enterprise Account Activity API

## POST account\_activity/webhooks[¶](#post-account-activity-webhooks "Permalink to this headline")

Registers a new webhook URL for the given application context. The URL will be validated via CRC request before saving. In case the validation failed, returns comprehensive error message to the requester.

The number of allowed webhooks is determined by billing package.

### Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/account_activity/webhooks.json`