platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/custom-profiles/api-reference/new-profile

POST custom\_profiles/new.json

new-profile

# POST custom\_profiles/new.json

Creates a new custom profile. The returned ID should be used with when publishing a new message with [POST direct\_messages/events/new](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/new-event).

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/custom_profiles/new.json`

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 24 hour window (user auth) | Yes (1000 / 1 day) |