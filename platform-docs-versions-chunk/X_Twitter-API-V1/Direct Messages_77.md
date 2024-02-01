platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/buttons/api-reference/buttons


## Example Read Response[¶](#example-read-response "Permalink to this headline")

The following JSON payload is an example of what will be received using an [Account Activity webhook](https://developer.twitter.com/en/docs/accounts-and-users/subscribe-account-activity/overview.html) or GET request like [GET direct\_messages/events/list](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/list-events). Notice the addition of the t.co short URL representation of the full URLs.

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
                "tco_url": "https://t.co/foo1",
                "url": "https://www.myairline.domain/see-flight-details"
              },
              {
                "type": "web_url",
                "label": "Map it",
                "tco_url": "https://t.co/foo2",
                "url": "https://www.myairline.domain/map-it"
              },
              {
                "type": "web_url",
                "label": "Visit MyAirline.domain",
                "tco_url": "https://t.co/foo3",
                "url": "https://www.myairline.domain/"
              }
            ]
          }
        }
      }
    }