platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/welcome-messages/api-reference/delete-welcome-message-rule

DELETE direct\_messages/welcome\_messages/rules/destroy

delete-welcome-message-rule

# DELETE direct\_messages/welcome\_messages/rules/destroy

Deletes a Welcome Message Rule by the given id.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/direct_messages/welcome_messages/rules/destroy.json`

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | 204 - No Content |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |
| --- | --- |
| **id** (required) | The id of the Welcome Message Rule that should be deleted. |

## Example request using [Twurl](https://github.com/twitter/twurl)[¶](#example-request-using-twurl "Permalink to this headline")

    twurl -X DELETE /1.1/direct_messages/welcome_messages/rules/destroy.json?id=9910934913490319