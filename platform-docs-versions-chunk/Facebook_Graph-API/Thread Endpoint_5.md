platform: Facebook
topic: Graph-API
subtopic: Thread Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Thread Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/thread

### Filtering Messages

The `messages` connection can be filtered to avoid pulling text that is part of thread warnings by the Messenger Apps. This is done via the `source` filter there only participants might be selected.

If this filter is not apply _admin text_ (gray text appears in the thread by Messenger) will be retrieved as well.

#### Example

This call will retrieve the last 3 messages made only by the participants.

curl -i -X GET \\
 "https://graph.facebook.com/v4.0/t\_10155839492600149?fields=id,messages.source(PARTICIPANTS).limit(3)&access\_token=<Access Token>"

## Publishing

You can't perform this operation on this endpoint.

## Deleting

You can't perform this operation on this endpoint.

## Updating

You can't perform this operation on this endpoint.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)