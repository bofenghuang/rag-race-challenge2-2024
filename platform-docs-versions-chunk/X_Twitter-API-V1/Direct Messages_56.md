platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/welcome-messages/api-reference/update-welcome-message

PUT direct\_messages/welcome\_messages/update

update-welcome-message

# PUT direct\_messages/welcome\_messages/update

Updates a Welcome Message by the given ID. Updates to the `welcome_message` object are atomic. For example, if the Welcome Message currently has `quick_reply` defined and you only provde `text`, the `quick_reply` object will be removed from the Welcome Message.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/direct_messages/welcome_messages/update.json`

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |
| --- | --- |
| **id** (required) | The id of the Welcome Message that should be updated. |