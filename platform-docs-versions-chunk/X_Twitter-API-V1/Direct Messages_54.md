platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/welcome-messages/api-reference/new-welcome-message-rule

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Content-Type | application/json |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

## Welcome Message Rule Object[¶](#welcome-message-rule-object "Permalink to this headline")

|     |     |
| --- | --- |
| **welcome\_message\_id** (required) | The ID of the Welcome Message that will be sent when this Rule is triggered. |

## Example Request[¶](#example-request "Permalink to this headline")

    {
      "welcome_message_rule": {
        "welcome_message_id": "844385345234"
      }
    }

### Example request using [Twurl](https://github.com/twitter/twurl)[¶](#example-request-using-twurl "Permalink to this headline")

    twurl -A 'Content-type: application/json' -X POST /1.1/direct_messages/welcome_messages/rules/new.json -d '{"welcome_message_rule": {"welcome_message_id": "844385345234"}}'