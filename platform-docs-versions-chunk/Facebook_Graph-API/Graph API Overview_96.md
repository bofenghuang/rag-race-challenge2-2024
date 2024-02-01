platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/guides/field-expansion

# Field Expansion

If you test the `GET /me/feed` query in the Graph API Explorer, you will noticed that the request returned many objects and paginated the results. This is common for most edges.

#### Example Response

{
  "data": \[
   {
      "created\_time": "2021-04-30T01:37:07+0000",
      "message": "I’ll never forget it has a head.",
      "id": "10211998223264288\_10222340566616408"
    },
    ...
    {
      "created\_time": "2021-04-25T22:29:26+0000",
      "message": "Things you hear at my house: \\"I accidentally made a cake.\\"",
      "id": "10211998223264288\_10222314489524497"
    }
  \],
  "paging": {
    "previous": "https://graph.facebook.com/v11.0/USER-ID/feed?access\_token=ACCESS-TOKEN&pretty=0&\_\_previous=1&since=1627322627&until&\_\_paging\_token=enc\_AdB2fX...",
    "next": "https://graph.intern.facebook.com/v11.0/USER-ID/feed?access\_token=ACCESS-TOKEN&pretty=0&until=1619389766&since&\_\_paging\_token=enc\_AdAamX...&\_\_previous"
  }
}

Field expansion allows you not only to limit the number of objects returned but also perform nested requests.