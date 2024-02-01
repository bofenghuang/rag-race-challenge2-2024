platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/webhooks

### Capture Story Insights

If you subscribe to the `story_insights` field, we send your endpoint a webhook notification containing user interaction metrics on a story, after the story has expired.

#### Sample Story Insights Payload

\[
  {
    "entry": \[
      {
        "changes": \[
          {
            "field": "story\_insights",
            "value": {
              "media\_id": "18023345989012587",
              "exits": 1,
              "replies": 0,
              "reach": 17,
              "taps\_forward": 12,
              "taps\_back": 0,
              "impressions": 28
            }
          }
        \],
        "id": "17841405309211844",  // Instagram Business or Creator Account ID
        "time": 1547687043
      }
    \],
    "object": "instagram"
  }
\]