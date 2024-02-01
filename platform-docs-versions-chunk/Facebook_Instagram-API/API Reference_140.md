platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/insights


### Sample Interaction Metric Response

{
  "data": \[
    {
      "name": "reach",
      "period": "day",
      "title": "Accounts reached",
      "description": "The number of unique accounts that have seen your content, at least once, including in ads. Content includes posts, stories, reels, videos and live videos. Reach is different from impressions, which may include multiple views of your content by the same accounts. This metric is estimated and in development.",
      "total\_value": {
        "value": 224,
        "breakdowns": \[
          {
            "dimension\_keys": \[
              "media\_product\_type"
            \],
            "results": \[
              {
                "dimension\_values": \[
                  "CAROUSEL\_CONTAINER"
                \],
                "value": 100
              },
              {
                "dimension\_values": \[
                  "POST"
                \],
                "value": 124
              }
            \]
          }
        \]
      },
      "id": "17841405309211844/insights/reach/day"
    }
  \],
  "paging": {
    "previous": "https://graph.face...",
    "next": "https://graph.face..."
  }