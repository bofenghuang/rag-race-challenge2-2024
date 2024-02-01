platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/business-discovery


### Getting Basic Metrics on Media

You can use both nested requests and field expansion to get public fields for a Business or Creator Account's media objects. Note that this does not grant you permission to access media objects directly — performing a `GET` on any returned [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) will fail due to insufficient permissions.

For example, here's how to get the number of comments and likes for each of the media objects published by Blue Bottle Coffee:

#### Sample Request

curl \-i \-X GET \\
 "https://graph.facebook.com/v3.2/17841405309211844?fields=business\_discovery.username(bluebottle){followers\_count,media\_count,media{comments\_count,like\_count}}&access\_token={access-token}"

#### Sample Response

{
  "business\_discovery": {
    "followers\_count": 267793,
    "media\_count": 1205,
    "media": {
      "data": \[
        {
          "comments\_count": 50,
          "like\_count": 5841,
          "id": "17858843269216389"
        },
        {
          "comments\_count": 11,
          "like\_count": 2998,
          "id": "17894036119131554"
        },
        {
          "comments\_count": 28,
          "like\_count": 3644,
          "id": "17894449363137701"
        },
        {
          "comments\_count": 43,
          "like\_count": 4943,
          "id": "17844278716241265"
        },
        {
          "comments\_count": 60,
          "like\_count": 9347,
          "id": "17899363132086521"
        },
        {
          "comments\_count": 63,
          "like\_count": 6913,
          "id": "17893114378137541"
        },
        {
          "comments\_count": 16,
          "like\_count": 2791,
          "id": "17886057709171561"
        },
        {
          "comments\_count": 15,
          "like\_count": 3895,
          "id": "17856337633208377"
        },
      \],
    },
    "id": "17841401441775531"
  },
  "id": "17841405976406927"
}

[](#)

[](#)