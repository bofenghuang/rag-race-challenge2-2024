platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/typing-indicator-and-read-receipts/api-reference/new-read-receipt

## Example request using [Twurl](https://github.com/twitter/twurl)[¶](#example-request-using-twurl "Permalink to this headline")

    twurl -X POST /1.1/direct_messages/mark_read.json -d "last_read_event_id=8754578330382663743" -d "recipient_id=3805104374" 

## HTTP Response Codes[¶](#http-response-codes "Permalink to this headline")

Response contains no body.

| Code | Message |
| --- | --- |
| 204 | Read receipt successfully sent. |
| 400 | Missing or invalid parameter(s) included in request. |