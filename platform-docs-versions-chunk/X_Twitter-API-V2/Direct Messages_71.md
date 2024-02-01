platform: X
topic: Twitter-API-V2
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/direct-messages/manage/api-reference/post-dm_conversations-dm_conversation_id-messages

### JSON body parameters

| Name | Type | Description |
| --- | --- | --- |
| `attachments`  <br> Optional | array | A single Media ID being attached to the Direct Message. This field is required if `text` is not present. For this launch, only 1 attachment is supported.  <br>  <br>Example: `{"text": "Sending a DM with media!", "attachments": [{"media_id": "1455952740635586573"}]` |
| `text`  <br> Optional | string | Text of the Direct Message being created. This field is required if `attachments` is not present. Text messages support up to 10,000 characters.  <br>  <br>Example: `{"text": "Hello just you conversation participants!""}` |