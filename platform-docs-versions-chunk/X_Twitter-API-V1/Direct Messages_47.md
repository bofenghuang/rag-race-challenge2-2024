platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/welcome-messages/api-reference/list-welcome-messages


## Example Response[¶](#example-response "Permalink to this headline")

Welcome Messages are returned in the `welcome_messages` array. A `next_cursor` property will be returned if there are more welcome messages to be retrieved.

> **Note**
> 
> To determine if there are more welcome messages to retrieve, always look for the presence of a `next_cursor`. In rare cases the `welcome_messages` array may be empty.

    {
      "welcome_messages": [
        {
          "id": "844385345234",
          "created_timestamp": "1470182274821",
          "message_data": {
            "text": "Welcome!",
            "attachment": {
              "type": "media",
              "media": {
                ...
              }
            }
          }
        },
        {
          "id": "844385345238",
          "created_timestamp": "1470182275399",
          "message_data": {
            "text": "Welcome Again!",
            "attachment": {
              "type": "media",
              "media": {
                ...
              }
            }
          }
        }
      ],
      "next_cursor": "NDUzNDUzNDY3Nzc3"
    }