platform: X
topic: Twitter-API-V1
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/direct-messages/sending-and-receiving/guides/direct-message-migration

### Deleting Direct Messages

Direct Messages can now be deleted with DELETE direct\_messages/events/destroy. The interface is largely the same requiring the ID of the message to delete. The key differences is the endpoint now requires a DELETE request instead of a POST request.  
  
How deleted Direct Messages are reflected in official Twitter clients remains the same. Direct Messages are only removed from the interface of the user context provided. Other members of the conversation can still access the Direct Message.

#### Summary

* Deleting a Direct Message requires the ID.
* New endpoint requires a DELETE request.
* How deleted Direct Messages are reflected in official Twitter clients remains unchanged.

**Questions about migrating to the new Direct Message endpoints?  
**Post your question to the developer community forum on [twittercommunity.com](https://twittercommunity.com/tags/c/rest-api/rest-api-v1-1/directmessages).