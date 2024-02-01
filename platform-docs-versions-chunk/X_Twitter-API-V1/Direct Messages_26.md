platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/sending-and-receiving/api-reference/list-events

## Example request using [Twurl](https://github.com/twitter/twurl)[¶](#example-request-using-twurl "Permalink to this headline")

    twurl -X GET /1.1/direct_messages/events/list.json

## Example Response[¶](#example-response "Permalink to this headline")

Events are returned in the `events` array. A `next_cursor` property will be returned if there are more events to be retrieved.

> **Note**
> 
> To determine if there are more event to retrieve, always look for the presence of a `next_cursor`. In rare cases the `events` array may be empty.

    {
      "next_cursor": "AB345dkfC",
      "events": [
        { "id": "110", "created_timestamp": "5300", ... },
        { "id": "109", "created_timestamp": "5200", ... },
        { "id": "108", "created_timestamp": "5200", ... },
        { "id": "107", "created_timestamp": "5200", ... },
        { "id": "106", "created_timestamp": "5100", ... },
        { "id": "105", "created_timestamp": "5100", ... },
        ...
      ]
    }