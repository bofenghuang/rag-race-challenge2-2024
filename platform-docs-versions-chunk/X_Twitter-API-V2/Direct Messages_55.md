platform: X
topic: Twitter-API-V2
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/direct-messages/manage/integrate


### Direct Message conversations

All Direct Messages are part of a Direct Message conversation. These conversations can be one-to-one conversations or group conversations. This launch provides the foundational endpoints needed to create Direct Messages and retrieve events associated with Direct Message conversations. All conversations have a unique dm\_conversation\_id, and the events that make up that conversation all have a unique dm\_event\_id.  

The Manage Direct Message endpoints provide three POST methods for creating new messages and adding them to conversations:

* **POST /2/dm\_conversations/with/:participant\_id/messages** - Creates a one-to-one Direct Message. This method either adds the message to an existing one-to-one conversation or creates a new one. The :participant\_id path parameter is the User ID of the account receiving the message.   
    Here is an example JSON request body for sending a one-to-one Direct Message:
    

      `{    "text": "Hello just you. This will appear as a new conversation if we have never messaged, or will be added to our existing thread. " }`
    

* **POST /2/dm\_conversations** - Creates a new group conversation and adds a Direct Message to it. These requests require a list of conversation participants. Note that you can create multiple conversations with the same participant list. These requests will always return a new conversation ID. Below is an example JSON request body for creating a new group conversation and adding a Direct Message. Note that this requires a "conversation\_type" field and that must be set to "Group" (case sensitive).

      `{    "message": {"text": "Hello to just you two, this is a new group conversation."},    "participant_ids": ["944480690","906948460078698496"],    "conversation_type": "Group"        }`
    

* **POST /2/dm\_conversations/:dm\_conversation\_id/messages** \- Creates a Direct Message and adds it to an existing conversation. The :dm\_conversation\_id path parameter is the ID of the conversation that the message will be added to. This method can be used to add a message to both one-to-one and group conversations.  
    Here is an example JSON request body for sending Direct Message to both one-to-one and group conversations:
    

      `{    "text": "Here is a new message." }`
    

These POST methods support attaching a single piece of media. POST request bodies must include either or both the "text" and "attachments" fields. The "text" attribute is required if the "attachments" field is not included, and the "attachments" field is required if the "text" field is not included. See the next section for more information.

For more information see the [Manage Direct Messages API References](https://developer.twitter.com/en/docs/twitter-api/direct-messages/manage/api-reference).