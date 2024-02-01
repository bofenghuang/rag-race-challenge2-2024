platform: X
topic: Twitter-API-V2
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/direct-messages/lookup/integrate


### Direct Message event fields and expansions

The Twitter API v2 allows users to select exactly which data they want to return from the API using a set of tools called fields and expansions. For example, Direct Message lookup endpoints support the following dm\_events fields: 

* id, event\_type, and text are the defaults for MessageCreate events. 
    
* id, event\_type, and participant\_ids are the defaults for ParticipantsJoin and ParticipantsLeave events.
    
* dm\_conversation\_id and created\_at are available for all events.
    
* attachments and referenced\_tweets are available for MessageCreate events. 
    
* sender\_id is available for MessageCreate and ParticipantsJoin events. 
    
* participant\_ids is available for ParticipantsJoin and ParticipantsLeave events. 
    

In addition, the Direct Message lookup endpoints support the following [expansions](https://developer.twitter.com/en/docs/twitter-api/expansions):  

* sender\_id - Expands the User object associated with who sent the message or who invited someone to the conversation. 
    
* referenced\_tweets.id - Expands the Tweet object if the Direct Message text includes a link to a Tweet. 
    
* attachments.media\_keys - Expands the Media object if the Direct Message includes a media attachment. 
    
* participant\_ids - Expands the User object associated with who joined or left a group conversation.
    

Since expansion include Tweets, Users, and Media objects, you can also use the tweet.fields, user.fields, and media.fields request query parameters. See our guide on how to [use fields and expansions](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/using-fields-and-expansions) for more information.