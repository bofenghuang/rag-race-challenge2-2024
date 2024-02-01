platform: X
topic: Twitter-API-V2
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/direct-messages/manage/api-reference/post-dm_conversations


### JSON body parameters

| Name | Type | Description |
| --- | --- | --- |
| `conversation_type`  <br> Required | string | The `conversation_type` attribute must be set to "Group" (case sensitive).  <br>  <br>Example: `{"conversation_type": "Group"}` |
| `message`  <br> Required | object | A JSON object that contains either or both the `text` and `attachments` parameters.  <br>  <br>Example: `{"message": {text": "Hello just you conversation participants!"}}` |
| `participant_ids`  <br> Required | array | An array of User IDs that the conversation is created with. Conversations can have up to 50 participants.  <br>  <br>Example: `{"participant_ids": ["944480690","906948460078698496"]}` |
| `message.attachments`  <br> Optional | array | A single Media ID being attached to the Direct Message. This field is required if `message.text` is not present. For this launch, only 1 attachment is supported.  <br>  <br>Example: `{"message": {"text": "Sending a DM with media!", "attachments": [{"media_id": "1455952740635586573"}]}` |
| `message.text`  <br> Optional | string | Text of the Direct Message being created. This field is required if `message.attachments` is not present. Text messages support up to 10,000 characters.  <br>  <br>Example: `{"message": {"text": "Hello just you conversation participants!"}}` |