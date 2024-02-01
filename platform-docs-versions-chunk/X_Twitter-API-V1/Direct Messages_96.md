platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/custom-profiles/api-reference/delete-profile

DELETE custom\_profiles/destroy.json

delete-profile

# DELETE custom\_profiles/destroy.json

Deletes a custom profile that was created with [POST custom\_profiles/new.json](https://developer.twitter.com/en/docs/direct-messages/custom-profiles/api-reference/new-profile).

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/custom_profiles/destroy.json`

## Resource information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 24 hour window (user auth) | Yes (1000 / 1 day) |

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |
| --- | --- |
| **id** (required) | The string ID of the custom profile to destroy. |