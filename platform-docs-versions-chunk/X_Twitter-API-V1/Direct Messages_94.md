platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/custom-profiles/api-reference/attach-profile

## Example Request[¶](#example-request "Permalink to this headline")

    {
      "event": {
        "type": "message_create",
        "message_create": {
          "target": {
            "recipient_id": "844385345234"
          },
          "message_data": {
            "text": "Hi, my name is Jon. How can I help?",
          },
          "custom_profile_id": "100001"
        }
      }
    }

### Example request using [Twurl](https://github.com/twitter/twurl)[¶](#example-request-using-twurl "Permalink to this headline")

    twurl -A 'Content-type: application/json' -X POST /1.1/direct_messages/events/new.json -d ' { "event": { "type": "message_create", "message_create": { "target": { "recipient_id": "844385345234" }, "message_data": { "text": "Hi, my name is Jon. How can I help?", }, "custom_profile_id": "100001" } } }'