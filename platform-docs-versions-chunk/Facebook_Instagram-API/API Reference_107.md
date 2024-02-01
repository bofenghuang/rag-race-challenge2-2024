platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/business_discovery

### Sample Request with Edge

GET graph.facebook.com
  /17841405309211844
    ?fields=business\_discovery.username(bluebottle){followers\_count,media\_count,media}

### Sample Response with Edge

{
  "business\_discovery": {
    "followers\_count": 267788,
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
        {
          "id": "17911489846004508"
        }
      \],
    },
    "id": "17841401441775531"
  },
  "id": "17841405309211844"
}