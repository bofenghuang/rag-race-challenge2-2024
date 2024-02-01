platform: X
topic: Twitter-API-V2
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/direct-messages/lookup/integrate


### Direct Message conversations

All Direct Messages are part of a Direct Message conversation. These conversations can be one-to-one conversations or group conversations. This launch provides the foundational endpoints needed to create Direct Messages and retrieve events associated with Direct Message conversations. All conversations have a unique dm\_conversation\_id, and the events that make up that conversation all have a unique dm\_event\_id.  

The Direct Message lookup endpoints provide methods for retrieving events associated with conversations. These GET endpoints are used to retrieve the messages that make up a conversation, and for group conversations, can be used to understand who has joined and left group conversations.  

This initial release of Direct Messages lookup includes three GET methods:

* **GET /2/dm\_conversations/with/:participant\_id/dm\_events** - Retrieves Direct Message events associated with a one-to-one conversation. The :participant\_id path parameter is the numeric User ID of the account having the conversation with the authenticated user making this request.  
    
* **GET /2/dm\_conversations/:dm\_conversation\_id/dm\_events** - Retrieves Direct Message events associated with a specific conversation ID, as indicated by the :dm\_conversation\_id path parameter. Both one-to-one and group conversations IDs are supported.  
    
* **GET /2/dm\_events** - Retrieves Direct Message events associated with the authenticating user, including both one-to-one and group conversations. Events from up to 30 days ago are available.  
    

These GET endpoints all support retrieving dm\_events by event type with an event\_types request query parameters. Currently, there are three conversation event types supported:  

* **MessageCreate** - Created when a new Direct Message is created. This event object can include the time and text of the message, along with the account ID of who sent the message, and the conversation and event IDs. 
    
* **ParticipantsJoin** - Created when a new participant joins a group conversation. This dm\_event object includes the ID of the participant joining, along with the created\_at time and the sender\_id of the 'invite' event. 
    
* **ParticipantsLeave** - Created when a participant leaves a conversation.This event object includes the ID of the participant leaving, along with the time of the event. 
    

For more information see the [Direct Messages lookup API References](https://developer.twitter.com/en/docs/twitter-api/direct-messages/lookup/api-reference).