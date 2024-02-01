platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/business_discovery

### Sample Request with Field Expansion

Getting data about the Instagram Business [IG User](https://developers.facebook.com/docs/instagram-api/reference/ig-user) "Blue Bottle Coffee" and using field expansion to request its followers and media counts.

GET graph.facebook.com
  /17841405309211844
    ?fields=business\_discovery.username(bluebottle){followers\_count,media\_count}

### Sample Response

{
  "business\_discovery": {
    "followers\_count": 267788,
    "media\_count": 1205,
    "id": "17841401441775531"
  },
  "id": "17841405309211844"
}