platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/guides/direct-message-migration.html


### Retrieving Direct Messages

Retrieving past Direct Message is now accomplished with a single API endpoint: [GET direct\_messages/events/list](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/list-events). The significant difference with this new endpoint is that it now returns both sent and received messages in reverse chronological order. This may make it easier to rebuild a conversation. However, if you are only looking for sent or received messages you will need to post-process the response by referring to the sender\_id property.

Pagination is now based on a cursor value rather an ID of a Direct Message. A cursor property is returned with each response. [GET direct\_messages/events/list](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/list-events) will return up to 30 days of past messages, regardless of how many messages exist within the past 30 days. When a cursor is not returned, there are no more messages to be returned. The method for accessing individual Direct Messages with [GET direct\_messages/events/show](https://developer.twitter.com/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/api-reference/get-event) remains the same, although the Direct Message object returned has a different structure as described previously.

Finally, real-time access to Direct Messages will now be accomplished via webhook with the [Account Activity API](https://developer.twitter.com/content/developer-twitter/en/docs/accounts-and-users/subscribe-account-activity/overview). For guidance in migrating from User Streams or Site Streams, see the migration guide to Account Activity API for more information.

#### Summary

* Sent and Received messages are now returned on the same endpoint.
* Up to 30 days of messages returned.
* Cursor based pagination.
* Real-time access to Direct Message via webhook.