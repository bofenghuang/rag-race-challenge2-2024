platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/custom-profiles/api-reference/get-profile

GET custom\_profiles/:id

get-profile

# GET custom\_profiles/:id

Returns a custom profile that was created with [POST custom\_profiles/new.json](https://developer.twitter.com/en/docs/direct-messages/custom-profiles/api-reference/new-profile).

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/custom_profiles/:id.json`

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 24 hour window (user auth) | Yes (180 / 15 min) |

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |
| --- | --- |
| **id** (required) | The string ID of the custom profile that should be returned. Provided in resource URL. |

## Example request using [Twurl](https://github.com/twitter/twurl)[¶](#example-request-using-twurl "Permalink to this headline")

    twurl -X GET /1.1/custom_profiles/100001