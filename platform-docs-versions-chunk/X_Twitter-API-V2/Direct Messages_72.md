platform: X
topic: Twitter-API-V2
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/direct-messages/manage/api-reference/post-dm_conversations-dm_conversation_id-messages

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [cURL](#tab0)

cURL

      `curl -X POST "https://api.twitter.com/2/dm_conversations/:dm_conversation_id/messages" -d '{"text": "Adding a Direct Message to a conversation by referencing the conversation ID. This method supports both one-to-one and group conversations."}' -H "Authorization: Bearer $ACCESS_TOKEN"`
    

### Example responses

* [Successful response](#tab0)

Successful response

      `{   "dm_conversation_id": "1346889436626259968",   "dm_event_id": "128341038123" }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `dm_conversation_id` | string | Contains the `id` of the Direct Message conversation the Direct Message was added to. |
| `dm_event_id` | string | Contains the `id` of the event created by this request. |