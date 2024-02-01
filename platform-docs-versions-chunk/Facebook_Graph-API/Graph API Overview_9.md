platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/overview

## /me

The `/me` node is a special endpoint that translates to the object ID of the person or Page whose access token is currently being used to make the API calls. If you had a User access token, you could retrieve a User's name and ID by using:

curl -i -X GET \\
  "https://graph.facebook.com/me?access\_token=ACCESS-TOKEN"

## Edges

An edge is a connection between two nodes. For example, a User node can have photos connected to it, and a Photo node can have comments connected to it. The following cURL example will return a list of photos a person has published to Facebook.

curl -i -X GET \\
  "https://graph.facebook.com/USER-ID/photos?access\_token=ACCESS-TOKEN"

Each ID returned represents a Photo node and when it was uploaded to Facebook.

    {
  "data": \[
    {
      "created\_time": "2017-06-06T18:04:10+0000",
      "id": "1353272134728652"
    },
    {
      "created\_time": "2017-06-06T18:01:13+0000",
      "id": "1353269908062208"
    }
  \],
}