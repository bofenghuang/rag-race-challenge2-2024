platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/insights


### Getting Media Metrics

To get metrics on a media object, query the [`GET /{ig-media-id}/insights`](https://developers.facebook.com/docs/instagram-api/reference/ig-media/insights) edge and specify the metrics you want returned.

#### Sample Request

GET graph.facebook.com/{media\-id}/insights
    ?metric\=engagement,impressions,reach

#### Sample Response

{
  "data": \[
    {
      "name": "engagement",
      "period": "lifetime",
      "values": \[
        {
          "value": 8
        }
      \],
      "title": "Engagement",
      "description": "Total number of likes and comments on the media object",
      "id": "media\_id/insights/engagement/lifetime"
    },
    {
      "name": "impressions",
      "period": "lifetime",
      "values": \[
        {
          "value": 13
        }
      \],
      "title": "Impressions",
      "description": "Total number of times the media object has been seen",
      "id": "media\_id/insights/impressions/lifetime"
    },
    {
      "name": "reach",
      "period": "lifetime",
      "values": \[
        {
          "value": 13
        }
      \],
      "title": "Reach",
      "description": "Total number of unique accounts that have seen the media object",
      "id": "media\_id/insights/reach/lifetime"
    }
  \]
}

[](#)

[](#)