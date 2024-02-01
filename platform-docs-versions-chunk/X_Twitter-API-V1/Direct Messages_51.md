platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/welcome-messages/api-reference/new-welcome-message

## Example Request[¶](#example-request "Permalink to this headline")

    {
      "welcome_message" : {
        "name": "simple_welcome-message 01",
        "message_data": {
          "text": "Welcome!",
          "attachment": {
            "type": "media",
            "media": {
              "id": "48909183894931"
            }
          }
        }
      }
    }

### Example request using [Twurl](https://github.com/twitter/twurl)[¶](#example-request-using-twurl "Permalink to this headline")

    twurl -A 'Content-type: application/json' /1.1/direct_messages/welcome_messages/new.json -d '{"name": "simple_welcome-message 01", "welcome_message": {"message_data": {"text": "Welcome!", "attachment": {"type": "media", "media": {"id": "48909183894931"}}}}}'