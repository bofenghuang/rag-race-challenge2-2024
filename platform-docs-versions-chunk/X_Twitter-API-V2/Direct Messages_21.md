platform: X
topic: Twitter-API-V2
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/direct-messages/lookup/migrate/standard-to-twitter-api-v2


## Comparing v1.1 and v2 Direct Message event lookup endpoints

Both v1.1 and v2 versions of the Direct Messages endpoints provide methods for looking up Direct Message events. This guide is intended to help understand the differences and provide information for migrating to v2. 

A major difference between the two versions is that v1.1 supports only one-to-one conversations, while v2 introduces support for group conversations. One artifact of this is that v1.1 supports only "message created" events, while v2 also supports events associated with participants joining and leaving conversations. In fact, a fundamental v2 update is establishing dm\_conversations as a core API object.     

With v1.1. there are two endpoints for retrieving Direct Messages (again, new messages are the only event type supported with v1.1):  

* [GET direct\_messages/events/show](https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/sending-and-receiving/api-reference/get-event) - Retrieves a single event by ID. 
    
* [GET direct\_messages/events/list](https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/sending-and-receiving/api-reference/list-events) - Retrieves up to 30 days of one-to-one Direct Messages sent and received by the authenticated user. Note that this method is not able to retrieve messages from group conversations. 
    

With this v2 release, there are three GET methods for retrieving Direct Message conversation events:   

* **GET /2/dm\_conversations/with/:participant\_id/dm\_events** - Retrieves Direct Message events associated with a one-to-one conversation. The :participant\_id path parameter is the User ID of the account having the conversation with the authenticated user making this request. 
    
* **GET /2/dm\_conversations/:dm\_conversation\_id/dm\_events** - Retrieves Direct Message events associated with a specific conversation ID, as indicated by the :dm\_conversation\_id path parameter. This method supports both one-to-one and group conversations. 
    
* **GET /2/dm\_events** - Retrieves Direct Message events associated with a user, including both one-to-one and group conversations. Events from up to 30 days ago are available.  
    

An important detail is that conversation and event IDs are shared across v1.1 and v2 versions of the Twitter Platform. This means both versions can be used together. For example, the Direct Messages v1.1 endpoints provide methods for returning a single event and for deleting events, methods not yet available with v2. Since IDs are common across v1.1 and v2, you can make v1.1 requests based on IDs provided by v2, or by referencing conversation IDs displayed in conversation URLs on the Twitter application.

The following table compares fundamental aspects of the v1.1 and v2 Direct Message event lookup endpoints. The Twitter API v2 characteristics shared here are common to all of the Direct Message lookup endpoints.

|     |     |     |
| --- | --- | --- |
| **Description** | **Standard v1.1** | **Twitter API v2** |
| Host domain | https://api.twitter.com | https://api.twitter.com |
| Endpoint root path | [/1.1/direct\_messages](https://api.twitter.com/1.1/direct_messages) | [/2/dm\_conversations](https://api.twitter.com/2/users/:id/dm_conversations)<br><br>Direct Messages conversations are introduced as a fundamental API object.   <br><br>These endpoints retrieve MessageCreate, ParticipantsJoin, and ParticipantLeave events. |
| HTTP methods supported | GET | GET |
| Supports Group Direct Messages |     | ✔   |
| Event types supported | message\_create | MessageCreate, ParticipantsJoin, ParticipantsLeave |
| [Authentication](https://developer.twitter.com/en/docs/authentication) | OAuth 1.0a User Context | OAuth 1.0a User Context<br><br>OAuth 2 User Context (scopes: dm.read, tweet.read, user.read) |
| Requires the use of credentials from a [developer App](https://developer.twitter.com/en/docs/authentication) associated with a Twitter API v2 [Project](https://developer.twitter.com/en/docs/projects) |     | ✔   |
| Default request [rate limits](https://developer.twitter.com/en/docs/twitter-api/rate-limits)\*  <br>\*All requests require user tokens |     | GET requests: 300 requests per 15 mins<br><br>Rate limit is applied across all three endpoints |

The following tables compare the v2 GET methods with version v1.1. Note that these v2 offerings expand the available capabilities by supporting group conversations. 

**Get all messages in a specific one-to-one conversation**