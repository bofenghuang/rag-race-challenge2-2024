platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/batch-requests


## Batch Request

A batch request takes a JSON object consisting of an array of your requests. It returns an array of logical HTTP responses represented as JSON arrays. Each response has a status code, an optional headers array, and an optional body (which is a JSON encoded string).

To make a batched request, send a `POST` request to an endpoint where the `batch` parameter is your JSON object.

POST /ENDPOINT?batch=\[JSON-OBJECT\]

**Sample Batch Request**

In this example, we are getting information about two Pages that our app manages.

_Formatted for readability._

curl -i -X POST 'https://graph.facebook.com/me?batch=  
  \[
    {
      "method":"GET",
      "relative\_url":"PAGE-A-ID"
    },  
    {
      "method":"GET",
      "relative\_url":"PAGE-B-ID"
    }
  \]
  &include\_headers=false             // Included to remove header information
  &access\_token=ACCESS-TOKEN'

Once all operations are complete, a response is sent with the result of each operation. Because the headers returned can sometimes be much larger than the actual API response, you might want to remove them for efficiency. To include header information, remove the `include_headers` parameter or set it to `true`.

**Sample Response**

The body field contains a string encoded JSON object:

\[
  {
    "code": 200,
    "body": "{
      \\"name\\": \\"Page A Name\\",
      \\"id\\": \\"PAGE-A-ID\\"
      }"
  },
  {
    "code": 200,
    "body": "{
      \\"name\\": \\"Page B Name\\",
      \\"id\\": \\"PAGE-B-ID\\"
      }"
  }
\]