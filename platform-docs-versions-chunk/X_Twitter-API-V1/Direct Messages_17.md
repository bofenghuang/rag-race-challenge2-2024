platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/sending-and-receiving/api-reference/new-event

POST direct\_messages/events/new (message\_create)

new-event

# POST direct\_messages/events/new (message\_create)

Publishes a new `message_create` event resulting in a Direct Message sent to a specified user from the authenticating user. Returns an event if successful. Supports publishing Direct Messages with optional Quick Reply and media attachment. Replaces behavior currently provided by [POST direct\_messages/new](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/new-message).

Requires a JSON POST body and `Content-Type` header to be set to `application/json`. Setting `Content-Length` may also be required if it is not automatically.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/direct_messages/events/new.json`