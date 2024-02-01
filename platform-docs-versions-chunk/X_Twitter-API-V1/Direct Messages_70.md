platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/quick-replies/api-reference/options


## Example Request[¶](#example-request "Permalink to this headline")

Although not required, if one option defines the `description`, then all `options` must contain the `description`.

    {
      "event": {
        "type": "message_create",
        "message_create": {
          "target": {
            "recipient_id": "844385345234"
          },
          "message_data": {
            "text": "What's your favorite type of bird?",
            "quick_reply": {
              "type": "options",
              "options": [
                {
                  "label": "Red Bird",
                  "description": "A description about the red bird.",
                  "metadata": "external_id_1"
                },
                {
                  "label": "Blue Bird",
                  "description": "A description about the blue bird.",
                  "metadata": "external_id_2"
                },
                {
                  "label": "Black Bird",
                  "description": "A description about the black bird.",
                  "metadata": "external_id_3"
                },
                {
                  "label": "White Bird",
                  "description": "A description about the white bird.",
                  "metadata": "external_id_4"
                }
              ]
            }
          }
        }
      }
    }