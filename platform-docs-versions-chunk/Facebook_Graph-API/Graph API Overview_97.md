platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/guides/field-expansion


## Limiting Results

Limiting allows you to control the number of objects returned in each set of paginated results. To limit results, add a `.limit()` argument to any field or edge.

For example, performing a GET request on your `/feed` edge may return hundreds of Posts. You can limit the number of Posts returned for each page of results by doing this:

curl -i -X GET "https://graph.facebook.com/USER-ID?fields=feed.limit(3)&access\_token=ACCESS-TOKEN"

This returns all of the Posts on your User node, but limits the number of objects in each page of results to three. Notice that instead of specifying the Feed edge in the path URL (`/user/feed`), you specify it in the `fields` parameter (`?fields=feed`), which allows you to append the `.limit(3)` argument.

Here are the query results:

{
  "feed": {
    "data": \[
      {
        "created\_time": "2021-12-12T01:24:21+0000",
        "message": "This picture of my grandson with Santa",
        "id": "POST-ID"
      },
      {
        "created\_time": "2021-12-11T23:40:17+0000",
        "message": ":)",
        "id": "POST-ID"      
      },
      {
        "created\_time": "2021-12-11T23:31:38+0000",
        "message": "Thought you might enjoy this.",
        "id": "POST-ID"      
      }
    \],
    "paging": {
      "previous": "https://graph.facebook.com/v8.0/USER-ID/feed?format=json&limit=3&since=1542820440&access\_token=ACCESS-TOKEN&\_\_paging\_token=enc\_AdC...&\_\_previous=1",
      "next": "https://graph.facebook.com/v8.0/USER-ID/feed?format=json&limit=3&access\_token=ACCESS-TOKEN&until=1542583212&\_\_paging\_token=enc\_AdD..."
    }
  },
  "id": "USER-ID"
}

As you can see, only three objects appear in this page of paginated results. However, the response included a `next` field and URL which you can use to fetch the next page.