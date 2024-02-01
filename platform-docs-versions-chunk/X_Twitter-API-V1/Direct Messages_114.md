platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/customer-feedback/api-reference/events

## Example Result[¶](#example-result "Permalink to this headline")

    {
      "events":[
        {
          "event_type": "feedback.updated",
          "created_at": "SatDec1517:58:22+00002015",
          "feedback": {
            "created_at": "SatDec1517:58:20+00002015",
            "updated_at": "SatDec1517:59:22+00002015",
            "id": "123456789",
            ...
          }
        },
        {
          "event_type": "feedback.created",
          "created_at": "SatDec1517:59:22+00002015",
          "feedback":{
            "created_at": "SatDec1517:59:22+00002015",
            "updated_at": "SatDec1517:59:22+00002015",
            "id": "123456799",
            ...
          }
        }
      ],
      "next_cursor": "10011"
    }