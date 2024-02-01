platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/quick-replies/api-reference/options

Options Quick Reply

options

# Options Quick Reply

List of up to 20 predefined options presented for a user to choose from. For use with [POST direct\_messages/events/new (message\_create)](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/new-event).

## Quick Reply Object[¶](#quick-reply-object "Permalink to this headline")

|     |     |
| --- | --- |
| **quick\_reply.type** (required) | Must be set to `options` |
| **quick\_reply.option** (required) | An array of `options` objects. |