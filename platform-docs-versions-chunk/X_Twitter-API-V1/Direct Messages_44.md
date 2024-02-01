platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/welcome-messages/api-reference/list-welcome-message-rules

## Example Responses[¶](#example-responses "Permalink to this headline")

Welcome message rules are returned in the `welcome_message_rules` array. A `next_cursor` property will be returned if there are more welcome message rules to be retrieved.

> **Note**
> 
> To determine if there are more welcome message rules to retrieve, always look for the presence of a `next_cursor`. In rare cases the `welcome_message_rules` array may be empty.

    {
      "welcome_message_rules": [
        {
          "id": "9910934913490319",
          "created_timestamp": "1470182394258",
          "welcome_message_id": "844385345234"
        },
        {
          "id": "9910934913490431",
          "created_timestamp": "1470182394265",
          "welcome_message_id": "844385345238"
        }
      ],
      "next_cursor": "NDUzNDUzNDY3Nzc3"
    }