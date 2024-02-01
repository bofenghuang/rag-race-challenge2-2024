platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/overview

## Nodes

A node is an individual object with a unique ID. For example, there are many User node objects, each with a unique ID representing a person on Facebook. Pages, Groups, Posts, Photos, and Comments are just some of the nodes of the Facebook Social Graph.

The following cURL example represents a call to the User node.

curl -i -X GET \\
  "https://graph.facebook.com/USER-ID?access\_token=ACCESS-TOKEN"

This request would return the following data by default, formatted using JSON:

{
  "name": "Your Name",
  "id": "YOUR-USER-ID"
}