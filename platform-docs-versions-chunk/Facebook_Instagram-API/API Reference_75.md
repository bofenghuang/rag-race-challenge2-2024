platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-media/insights


### Sample Story Metric Response

{
  "data": \[
    {
      "name": "navigation",
      "period": "lifetime",
      "values": \[
        {
          "value": 25
        }
      \],
      "title": "Navigation",
      "description": "This is the total number of actions taken from your story. These are made up of metrics like exited, forward, back and next story.",
      "total\_value": {
        "value": 25,
        "breakdowns": \[
          {
            "dimension\_keys": \[
              "story\_navigation\_action\_type"
            \],
            "results": \[
              {
                "dimension\_values": \[
                  "tap\_forward"
                \],
                "value": 19
              },
              {
                "dimension\_values": \[
                  "tap\_back"
                \],
                "value": 4
              },
              {
                "dimension\_values": \[
                  "tap\_exit"
                \],
                "value": 1
              },
              {
                "dimension\_values": \[
                  "swipe\_forward"
                \],
                "value": 1
              }
            \]
          }
        \]
      },
      "id": "17969782069736348/insights/navigation/lifetime"
    }
  \]
}