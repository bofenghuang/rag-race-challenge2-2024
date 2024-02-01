platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-media/insights


### Sample Post Metric Response

{
  "data": \[
    {
      "name": "profile\_activity",
      "period": "lifetime",
      "values": \[
        {
          "value": 4
        }
      \],
      "title": "Profile activity",
      "description": "\[IG Insights\] This header is the name of a metric that appears on an educational info sheet for a particular post, story, video or promotion. This metric is the sum of all profile actions people take when they engage with this content.",
      "total\_value": {
        "value": 4,
        "breakdowns": \[
          {
            "dimension\_keys": \[
              "action\_type"
            \],
            "results": \[
              {
                "dimension\_values": \[
                  "email"
                \],
                "value": 1
              },
              {
                "dimension\_values": \[
                  "text"
                \],
                "value": 1
              },
              {
                "dimension\_values": \[
                  "direction"
                \],
                "value": 1
              },
              {
                "dimension\_values": \[
                  "bio\_link\_clicked"
                \],
                "value": 1
              }
            \]
          }
        \]
      },
      "id": "17932174733377207/insights/profile\_activity/lifetime"
    }
  \]
}