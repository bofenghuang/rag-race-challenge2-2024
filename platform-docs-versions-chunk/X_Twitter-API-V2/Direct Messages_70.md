platform: X
topic: Twitter-API-V2
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/direct-messages/manage/api-reference/post-dm_conversations-dm_conversation_id-messages

### OAuth 2.0 scopes required by this endpoint

|     |
| --- |
| `dm.write`<br><br>`dm.read`<br><br>`tweet.read`<br><br>`users.read` |
| [Learn more about OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/twitter-api/oauth2) |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `dm_conversation_id`  <br> Required | string | The `dm_conversation_id` of the conversation to add the Direct Message to. Supports both 1-1 and group conversations. |