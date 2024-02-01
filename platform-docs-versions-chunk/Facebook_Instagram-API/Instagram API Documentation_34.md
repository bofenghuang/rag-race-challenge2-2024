platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/business-discovery

### Getting Media

Since you can make nested requests by specifying an edge via the `fields` parameter, you can request the targeted Business or Creator Account's `media` edge to get all of its published media objects:

#### Sample Request

curl \-i \-X GET \\
 "https://graph.facebook.com/v3.2/17841405309211844?fields=business\_discovery.username(bluebottle){followers\_count,media\_count,media}&access\_token={access-token}"

#### Sample Response

{
  "business\_discovery": {
    "followers\_count": 267793,
    "media\_count": 1205,
    "media": {
      "data": \[
        {
          "id": "17858843269216389"
        },
        {
          "id": "17894036119131554"
        },
        {
          "id": "17894449363137701"
        },
        {
          "id": "17844278716241265"
        },
        ... // results truncated for brevity
      \],
    "id": "17841401441775531"
  },
  },
  "id": "17841405309211844"
}