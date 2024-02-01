platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/insights


### Sample Response

{
  "data": \[
    {
      "name": "impressions",
      "period": "day",
      "values": \[
        {
          "value": 4,
          "end\_time": "2017-05-04T07:00:00+0000"
        },
        {
          "value": 66,
          "end\_time": "2017-05-05T07:00:00+0000"
        }
      \],
      "title": "Impressions",
      "description": "Total number of times this profile has been seen",
      "id": "17841400008460056/insights/impressions/day"
    },
    {
      "name": "reach",
      "period": "day",
      "values": \[
        {
          "value": 3,
          "end\_time": "2017-05-04T07:00:00+0000"
        },
        {
          "value": 36,
          "end\_time": "2017-05-05T07:00:00+0000"
        }
      \],
      "title": "Reach",
      "description": "Total number of unique accounts that have seen this profile",
      "id": "17841400008460056/insights/reach/day"
    },
    {
      "name": "profile\_views",
      "period": "day",
      "values": \[
        {
          "value": 0,
          "end\_time": "2017-05-04T07:00:00+0000"
        },
        {
          "value": 2,
          "end\_time": "2017-05-05T07:00:00+0000"
        }
      \],
      "title": "Profile Views",
      "description": "Total number of unique accounts that have viewed this profile within the specified period",
      "id": "17841400008460056/insights/profile\_views/day"
    }
  \]
}

Notice that the [sample request](#sample-request) above did not include the `since` and `until` parameters, so the API returned data for a default range of 2 days. Each day is identified by an ISO 8601 formatted UTC timestamp with zero offset, which has been assigned to an `end_time` property.

The `end_time` property indicates a data set's lookback cutoff date; data older than this value is not included in the data set's calculation.