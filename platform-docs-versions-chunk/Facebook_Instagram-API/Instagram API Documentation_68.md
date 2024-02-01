platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/insights


### Getting Account Metrics

To get metrics on an Instagram Business or Creator Account, query the [`GET /{ig-user-id}/insights`](https://developers.facebook.com/docs/instagram-api/reference/ig-user/insights) edge and specify the metrics you want returned.

#### Sample Request

GET graph.facebook.com/17841405822304914/insights
    ?metric\=impressions,reach,profile\_views
    &period\=day

#### Sample Response

{
  "data": \[
    {
      "name": "impressions",
      "period": "day",
      "values": \[
        {
          "value": 32,
          "end\_time": "2018-01-11T08:00:00+0000"
        },
        {
          "value": 32,
          "end\_time": "2018-01-12T08:00:00+0000"
        }
      \],
      "title": "Impressions",
      "description": "Total number of times the Business Account's media objects have been viewed",
      "id": "instagram\_business\_account\_id/insights/impressions/day"
    },
    {
      "name": "reach",
      "period": "day",
      "values": \[
        {
          "value": 12,
          "end\_time": "2018-01-11T08:00:00+0000"
        },
        {
          "value": 12,
          "end\_time": "2018-01-12T08:00:00+0000"
        }
      \],
      "title": "Reach",
      "description": "Total number of times the Business Account's media objects have been uniquely viewed",
      "id": "instagram\_business\_account\_id/insights/reach/day"
    },
    {
      "name": "profile\_views",
      "period": "day",
      "values": \[
        {
          "value": 15,
          "end\_time": "2018-01-11T08:00:00+0000"
        },
        {
          "value": 15,
          "end\_time": "2018-01-12T08:00:00+0000"
        }
      \],
      "title": "Profile Views",
      "description": "Total number of users who have viewed the Business Account's profile within the specified period",
      "id": "instagram\_business\_account\_id/insights/profile\_views/day"
    }
  \]
}