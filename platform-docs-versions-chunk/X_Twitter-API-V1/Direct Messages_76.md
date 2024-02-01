platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/buttons/api-reference/buttons

## Example Request[¶](#example-request "Permalink to this headline")

    {
      "event": {
        "type": "message_create",
        "message_create": {
          "target": {
            "recipient_id": "844385345234"
          },
          "message_data": {
            "text": "Flight SF8020 from San Francisco to Montreal is ahead of schedule and will land in approximately 15 minutes. Can we help with anything else?",
            "ctas": [
              {
                "type": "web_url",
                "label": "See flight details",
                "url": "https://www.myairline.domain/see-flight-details"
              },
              {
                "type": "web_url",
                "label": "Map it",
                "url": "https://www.myairline.domain/map-it"
              },
              {
                "type": "web_url",
                "label": "Visit MyAirline.domain",
                "url": "https://www.myairline.domain/"
              }
            ]
          }
        }
      }
    }