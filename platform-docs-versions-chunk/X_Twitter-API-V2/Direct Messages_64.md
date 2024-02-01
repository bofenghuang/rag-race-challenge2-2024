platform: X
topic: Twitter-API-V2
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/direct-messages/manage/migrate/manage-dms-standard-to-twitter-api-v2


## Comparing v1.1 and v2 Manage Direct Message endpoints

Both v1.1 and v2 versions of the Direct Messages endpoints provide methods for creating Direct Message messages. This guide is intended to help understand the differences and provide information for migrating to v2. 

A major difference between the two versions is that v1.1 supports only one-to-one conversations, while v2 introduces support for group conversations. One artifact of this is that v1.1 supports only "message created" events, while v2 also supports events associated with participants joining and leaving conversations. In fact, a fundamental v2 update is establishing dm\_conversations as a core API object.     

With v1.1. there are two endpoints for managing Direct Messages:  

* [POST direct\_messages/events/new](https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/sending-and-receiving/api-reference/new-event) \- Creates a one-to-one Direct Message. This v1.1 endpoint can only create one-to-one messages, and does not support group messages.  
    
* [DELETE direct\_messages/events/destroy](https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/sending-and-receiving/api-reference/delete-message-event) - Deletes a one-to-one message from the view of the authenticating user. 
    

With this v2 release, there are three POST methods for creating Direct Messages:   

* **POST /2/dm\_conversations/with/:participant\_id/messages** - Creates a one-to-one Direct Message. This method either adds the message to an existing one-to-one conversation or creates a new one. The :participant\_id path parameter is the User ID of the account receiving the message. 
    
* **POST /2/dm\_conversations** - Creates a new group conversation and adds a Direct Message to it. These requests require a list of conversation participants. Note that you can create multiple conversations with the same participant list. These requests will always return a new conversation ID. 
    
* **POST /2/dm\_conversations/:dm\_conversation\_id/messages** - Creates a Direct Message and adds it to an existing conversation. The :dm\_conversation\_id path parameter is the ID of the conversation that the message will be added to. 
    

An important detail is that conversation and event IDs are shared across v1.1 and v2 versions of the Twitter Platform. This means both versions can be used together. For example, the Direct Messages v1.1 endpoints provide methods for returning a single event and for deleting events, methods not yet available with v2. Since IDs are common across v1.1 and v2, you can make v1.1 requests based on IDs provided by v2, or by referencing conversation IDs displayed in conversation URLs on the Twitter application.  

The following table compares fundamental aspects of the v1.1 and v2 manage Direct Messages endpoints. The Twitter API v2 characteristics shared here are common to all of the Direct Message lookup endpoints.  

|     |     |     |
| --- | --- | --- |
| **Description** | **Standard v1.1** | **Twitter API v2** |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint root path | [/1.1/direct\_messages](https://api.twitter.com/1.1/direct_messages) | [/2/dm\_conversations](https://api.twitter.com/2/users/:id/dm_conversations)<br><br>Direct Messages conversations are introduced as a fundamental API object.   <br><br>These endpoints retrieve MessageCreate, ParticipantsJoin, and ParticipantLeave events. |
| HTTP methods supported | POST | POST |
| Supports Group Direct Messages |     | ✔   |
| Event types supported | message\_create | MessageCreate, ParticipantsJoin, ParticipantsLeave |
| [Authentication](https://developer.twitter.com/en/docs/authentication) | OAuth 1.0a User Context | OAuth 1.0a User Context<br><br>OAuth 2 User Context (scopes: dm.read, dm.write) |
| Requires the use of credentials from a [developer App](https://developer.twitter.com/en/docs/authentication) associated with a Twitter API v2 [Project](https://developer.twitter.com/en/docs/projects) |     | ✔   |
| Default request [rate limits](https://developer.twitter.com/en/docs/twitter-api/rate-limits)\*  <br>\*All requests require user tokens | 1000 requests per user per 24 hours  <br>15000 requests per app per 24 hours | 200 requests per 15 minutes per user<br><br>1000 requests per user per 24 hours<br><br>15000 requests per app per 24 hours<br><br>These rate limits are shared across all dm\_conversations POST endpoints. |

The following tables compare the v2 POST methods with version v1.1. Note that these v2 offerings expand the available capabilities by supporting group conversations. 

**Create a new one-to-one Direct Message**