platform: Facebook
topic: Graph-API
subtopic: Message Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Message Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/message

### Limitations

**For Instagram Messaging**

* Only Instagram Professional accounts with a linked Facebook Page can access this endpoint.
    
* When querying this endpoint, all messages for this conversation will be returned. However, you will only be able to query data for the 20 most recent messages in the conversation. If a message is not within the 20 most recent, an error will be returned stating that the message has been deleted.