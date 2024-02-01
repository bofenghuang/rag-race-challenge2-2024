platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/custom-profiles/api-reference/attach-profile

Send a Direct Message with custom profile

attach-profile

# Send a Direct Message with custom profile

To attach a custom profile to a Direct Message add a `event.custom_profile_id` parameter to the [POST direct\_messages/events/new.json](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/new-event) request.

_Note:_ See [full documentation](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/new-event) for all properties. Custom profiles can also be used with [welcome messages](https://developer.twitter.com/en/docs/direct-messages/welcome-messages/overview).

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |
| --- | --- |
| **event.custom\_profile\_id** | The string ID of the custom profile to attach to the Direct Message. |