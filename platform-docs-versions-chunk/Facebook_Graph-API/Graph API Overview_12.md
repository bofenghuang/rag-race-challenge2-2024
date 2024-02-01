platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/overview


### Read-After-Write

For create and update endpoints, the Graph API can immediately read a successfully published or updated object and return any fields supported by the corresponding read endpoint.

By default, an ID of the object created or updated will be returned. To include more information in the response, include the `fields` parameter in your request and list the fields you want returned. For example, to publish the message “Hello” to a Page's feed, you could make the following request:

curl -i - X POST "https://graph.facebook.com/PAGE-ID/feed?message=Hello&
  fields=created\_time,from,id,message&access\_token=ACCESS-TOKEN"

_The above code example is formatted for readability._

This would return the specified fields as a JSON-formatted response, like this:

{
  "created\_time": "2017-04-06T22:04:21+0000",
  "from": {
    "name": "My Facebook Page",
    "id": "PAGE-ID"
  },
  "id": "POST\_ID",
  "message": "Hello",
}

Refer to each endpoint's [reference documentation](https://developers.facebook.com/docs/graph-api/reference) to see if it supports **read-after-write** and what fields are available.

#### Errors

If the read fails for any reason (for example, requesting a non-existent field), the Graph API will respond with a standard error response. Visit our [Handling Errors guide](https://developers.facebook.com/docs/graph-api/guides/error-handling) for more information.

You can usually delete a node, such as a Post or Photo node, by performing a DELETE operation on the object ID:

curl -i -X DELETE \\
  "https://graph.facebook.com/PHOTO-ID?access\_token=ACCESSS-TOKEN"

Usually you can only delete nodes that you created, but check each node's reference guide to see requirements for delete operations.