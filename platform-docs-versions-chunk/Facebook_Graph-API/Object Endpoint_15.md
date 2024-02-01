platform: Facebook
topic: Graph-API
subtopic: Object Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Object Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/object/likes

### Example Usage

**Sample Request**

curl -i -X GET "https://graph.facebook.com/{object-id}
  ?fields=likes.summary(true)
  &access\_token={access-token}"

#### Sample Response

  {
  "likes": {
    "data": \[
      {
        "name": "Bill the Cat",
        "id": "155111347875779",
        "created\_time": "2017-06-18T18:21:04+0000"
      },
      {
        "name": "Calvin and Hobbes",
        "id": "257573197608192",
        "created\_time": "2017-06-18T18:21:02+0000"
      },
      {
        "name": "Berkeley Breathed's Bloom County",
        "id": "108793262484769",
        "created\_time": "2017-06-18T18:20:58+0000"
      }
    \],
    "paging": {
      "cursors": {
        "before": "Nzc0Njg0MTQ3OAZDZD",
        "after": "NTcxODc1ODk2NgZDZD"
      },
      "next": "https://graph.facebook.com/vX.X/me/likes?access\_token=user-access-token&pretty=0&summary=true&limit=25&after=NTcxODc1ODk2NgZDZD"
    },
    "summary": {
      "total\_count": 136
    }
  },
  "id": "user-id"
}

## Publish

Like an object.