platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-media/insights


### Metrics

Some of these metrics are deprecated for v18.0. They will be deprecated for all versions beginning Dec 11, 2023. Please use the alternative metrics listed.

`total_interactions`, which is listed as an alternative for some of the deprecated metrics, is currently only available using version 18.0 and does not work with older versions. When querying older versions before Dec 11, 2023, please use the `engagement` metric.

See the [Changelog](https://developers.facebook.com/docs/instagram-api/changelog) for more information.

#### Album Metrics

| Metric | Description |
| --- | --- |
| `carousel_album_engagement`  <br>_Deprecated for v18.0+_ | Total number of likes and [IG Comments](https://developers.facebook.com/docs/instagram-api/reference/ig-comment) on the album [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object.  <br>**Alternative metric:** `total_interactions` |
| `carousel_album_impressions`  <br>_Deprecated for v18.0+_ | Total number of times the album [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object has been seen.  <br>**Alternative metrics:** `impressions` |
| `carousel_album_reach`  <br>_Deprecated for v18.0+_ | Total number of unique Instagram accounts that have seen the album [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object.  <br>**Alternative metric:** `reach` |
| `carousel_album_saved`  <br>_Deprecated for v18.0+_ | Total number of unique Instagram accounts that have saved the album [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object.  <br>**Alternative metric:** `saved` |
| `carousel_album_video_views`  <br>_Deprecated for v18.0+_ | Total number of unique Instagram accounts that have viewed video [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) within the album.  <br>**Alternative metric:** `video_views` |

#### Photo and Video Metrics

Metrics on media within an album are not supported. Get metrics on the album instead.

| Metric | Description |
| --- | --- |
| `engagement`  <br>_Deprecated for v18.0+_ | Sum of [`likes_count`](https://developers.facebook.com/docs/instagram-api/reference/ig-media#fields), [`comment_count`](https://developers.facebook.com/docs/instagram-api/reference/ig-media#fields), and [`saved`](#metrics) counts on the [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media).  <br>**Alternative metric:** `total_interactions`  <br>**Note:** You may see different results. `engagement` includes likes, comments and saves count while `total_interactions` includes likes, comments, saved and shares count. |
| `impressions` | Total number of times the [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object has been seen. |
| `reach` | Total number of unique Instagram accounts that have seen the [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object. |
| `saved` | Total number of unique Instagram accounts that have saved the [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object. |
| `video_views` | Total number of times the video [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) has been seen. For album IG Media, the number of times all videos within the album have been seen. |

#### Reels Metrics

| Metric | Description |
| --- | --- |
| `clips_replays_count` | The number of times your reel starts to play again after an initial play of your reel. This is defined as replays of 1ms or more in the same reel session. |
| `comments` | Number of comments on the reel. Metric [in development](https://business.facebook.com/business/help/metrics-labeling). |
| `ig_reels_aggregated_all_plays_count` | The number of times your reel starts to play or replay after an impression is already counted. This is defined as plays of 1ms or more. Replays are counted after the initial play in the same reel session. |
| `ig_reels_avg_watch_time` | The average amount of time spent playing the reel. Metric [in development](https://business.facebook.com/business/help/metrics-labeling). |
| `ig_reels_video_view_total_time` | The total amount of time the reel was played, including any time spent replaying the reel. Metric [in development](https://business.facebook.com/business/help/metrics-labeling). |
| `likes` | Number of likes on the reel. Metric [in development](https://business.facebook.com/business/help/metrics-labeling). |
| `plays` | Number of times the reels starts to play after an impression is already counted. This is defined as video sessions with 1 ms or more of playback and excludes replays. Metric [in development](https://business.facebook.com/business/help/metrics-labeling). |
| `reach` | Number of unique accounts that have seen the reel at least once. Reach is different from impressions, which can include multiple views of a reel by the same account. Metric is [estimated](https://business.facebook.com/business/help/metrics-labeling) and [in development](https://business.facebook.com/business/help/metrics-labeling). |
| `saved` | Number of saves of the reel. Metric [in development](https://business.facebook.com/business/help/metrics-labeling). |
| `shares` | Number of shares of the reel. Metric [in development](https://business.facebook.com/business/help/metrics-labeling). |
| `total_interactions` | Number of likes, saves, comments, and shares on the reel, minus the number of unlikes, unsaves, and deleted comments. Metric [in development](https://business.facebook.com/business/help/metrics-labeling). |

#### Story Metrics

| Metric | Description |
| --- | --- |
| `exits`  <br>_Deprecated for v18.0+_ | Total number of times someone exited the story [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object.  <br>**Alternative metric:** `navigation`  <br>**Breakdown:** `story_navigation_action_type` |
| `impressions` | Total number of times the story [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object has been seen. |
| `reach` | Total number of unique Instagram accounts that have seen the story [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object. |
| `replies` | Total number of replies ([IG Comments](https://developers.facebook.com/docs/instagram-api/reference/ig-comment)) on the story [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object. Value does not include replies made by users in some regions. These regions include: Europe starting December 1, 2020 and Japan starting April 14, 2021. If the Story was created by a user in one of these regions, returns a value of `0`. |
| `taps_forward`  <br>_Deprecated for v18.0+_ | Total number of taps to see this story [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object's next photo or video.  <br>**Alternative metric:** `navigation`  <br>**Breakdown:** `story_navigation_action_type` |
| `taps_back`  <br>_Deprecated for v18.0+_ | Total number of taps to see this story [IG Media](https://developers.facebook.com/docs/instagram-api/reference/ig-media) object's previous photo or video.  <br>**Alternative metric:** `navigation`  <br>**Breakdown:** `story_navigation_action_type` |

#### Sample Request

curl -X GET \\
  'https://graph.facebook.com/`v19.0`/17895695668004550/insights?metric=impressions,reach&access\_token=IGQVJ...'

#### Sample Response

{
  "data": \[
    {
      "name": "impressions",
      "period": "lifetime",
      "values": \[
        {
          "value": 264
        }
      \],
      "title": "Impressions",
      "description": "Total number of times the media object has been seen",
      "id": "17855590849148465/insights/impressions/lifetime"
    },
    {
      "name": "reach",
      "period": "lifetime",
      "values": \[
        {
          "value": 103
        }
      \],
      "title": "Reach",
      "description": "Total number of unique accounts that have seen the media object",
      "id": "17855590849148465/insights/reach/lifetime"
    }
  \]
}