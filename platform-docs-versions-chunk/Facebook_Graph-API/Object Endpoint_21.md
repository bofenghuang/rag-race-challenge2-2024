platform: Facebook
topic: Graph-API
subtopic: Object Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Object Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/object/private_replies

# `/{object-id}/private_replies`

#### Legacy Private Replies are deprecated for v5.0+

On October 29, 2019 we announced that this endpoint is now deprecated. Please use the new [Private Replies](https://developers.facebook.com/docs/messenger-platform/discovery/private-replies)

As part of the V3.3 changes the `read_page_mailboxes` permission was deprecated. Use `pages_messaging` permission to access this endpoint. The `read_page_mailboxes` permission will stop working after June 30 2020

This edge is the **Legacy Private Replies** allows Pages to reply to Post Comments and Visitor Posts with a plain text only message. It can be used with the following nodes:

* [`Comment`](https://developers.facebook.com/docs/graph-api/reference/comment)
    
* [`Post`](https://developers.facebook.com/docs/graph-api/reference/post)
    

Please note that a comment or post may only be replied to once.

## Reading

You can't read using this edge.