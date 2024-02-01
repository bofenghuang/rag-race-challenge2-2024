platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/welcome-messages/api-reference/update-welcome-message

## Example request using [Twurl](https://github.com/twitter/twurl)[¶](#example-request-using-twurl "Permalink to this headline")

    twurl -A 'Content-type: application/json' -X PUT '/1.1/direct_messages/welcome_messages/update.json?id=4893198399134' -d ‘
    {
      "message_data":{
        "text": "Welcome!"
      }
    }

## Example Response[¶](#example-response "Permalink to this headline")

    {
      "name": "Generic Welcome 01"
      "welcome_message": {
        "id": "4893198399134",
        "created_timestamp": "154903045",
        "message_data": {
          "text": "Welcome!"
        }
      },
      "apps": {
        "8829219": {
          "id": "8829219",
          "name": "Furni",
          "url": "https://developer.twitter.com"
        }
      }
    }