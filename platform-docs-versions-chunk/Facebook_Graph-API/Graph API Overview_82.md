platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/batch-requests


## Complex Batch Requests

It is possible to combine operations that would normally use different HTTP methods into a single batch request. While `GET` and `DELETE` operations can only have a `relative_url` and a `method` field, `POST` and `PUT` operations may contain an optional `body` field. The body should be formatted as a raw HTTP POST string, similar to a URL query string.

**Sample Request**

The following example publishes a post to a Page we manage and have publish permissions and then the Page's feed in a single operation:

curl "https://graph.facebook.com/PAGE-ID?batch=
  \[
    { 
      "method":"POST",
      "relative\_url":"PAGE-ID/feed",
      "body":"message=Test status update"
    },
    { 
      "method":"GET",
      "relative\_url":"PAGE-ID/feed"
    }
  \]
  &access\_token=ACCESS-TOKEN"

The output of this call would be:

\[
    { "code": 200,
      "headers": \[
          { "name":"Content-Type", 
            "value":"text/javascript; charset=UTF-8"}
       \],
      "body":"{\\"id\\":\\"…\\"}"
    },
    { "code": 200,
      "headers": \[
          { "name":"Content-Type", 
            "value":"text/javascript; charset=UTF-8"
          },
          { "name":"ETag", 
            "value": "…"
          }
      \],
      "body": "{\\"data\\": \[{…}\]}
    }
\]

The following example creates a new ad for a campaign, and then gets the details of the newly created object. Note the **URLEncoding** for the body param:

curl \\
-F 'access\_token=...' \\
-F 'batch=\[
  {
    "method":"POST",
    "name":"create-ad",
    "relative\_url":"11077200629332/ads",
    "body":"ads=%5B%7B%22name%22%3A%22test\_ad%22%2C%22billing\_entity\_id%22%3A111200774273%7D%5D"
  }, 
  {
    "method":"GET",
    "relative\_url":"?ids={result=create-ad:$.data.\*.id}"
  }
\]' \\
https://graph.facebook.com

The following example adds multiple pages to a Business Manager:

curl \\
-F 'access\_token=<ACCESS\_TOKEN>' \\
-F 'batch=\[
  {
    "method":"POST",
    "name":"test1",
    "relative\_url":"<BUSINESS\_ID>/owned\_pages",
    "body":"page\_id=<PAGE\_ID\_1>"
  }, 
  {
    "method":"POST",
    "name":"test2",
    "relative\_url":"<BUSINESS\_ID>/owned\_pages",
    "body":"page\_id=<PAGE\_ID\_2>"
  }, 
  {
    "method":"POST",
    "name":"test3",
    "relative\_url":"<BUSINESS\_ID>/owned\_pages",
    "body":"page\_id=<PAGE\_ID\_3>"
  }, 
\]' \\
"https://graph.facebook.com/v12.0"

Where:

* `<ACCESS_TOKEN>` is an access token with the `business_management` permission.
* `<BUSINESS_ID>` is the ID of the Business Manager to which the pages should be claimed.
* `<PAGE_ID_n>` are the Page IDs to be claimed.