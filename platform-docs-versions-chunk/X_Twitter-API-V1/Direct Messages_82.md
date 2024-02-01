platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/typing-indicator-and-read-receipts/api-reference/new-typing-indicator

POST direct\_messages/indicate\_typing

new-typing-indicator

# POST direct\_messages/indicate\_typing

Displays a visual typing indicator in the recipient’s Direct Message conversation view with the sender. Each request triggers a typing indicator animation with a duration of ~3 seconds.

## Usage[¶](#usage "Permalink to this headline")

A rudimentary approach would be to invoke an API request on every keypress or input event, however the application may quickly hit rate limits. A more sophisticated approach is to capture input events, but limit API requests to a specified interval based on the behavior of your users and the rate limit specified below.

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/direct_messages/indicate_typing.json`