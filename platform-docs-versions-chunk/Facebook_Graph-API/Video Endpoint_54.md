platform: Facebook
topic: Graph-API
subtopic: Video Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Video Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/video/video_insights/


### Reels Metrics

The following metrics are available for the `metric` [parameter](#parameters) when you read aggregated insights for a reel. For more information about Reels, see [Reels Developer Documentation](https://developers.facebook.com/docs/reels).

| Name | Description | Values for `period` |
| --- | --- | --- |
| `blue_reels_play_count` | The number of times your reel starts to play after an impression is already counted. This metric counts reels sessions with 1 millisecond or more of playback. This metric excludes replays. | lifetime |
| `fb_reels_replay_count` | The number of times your reel starts to play again after an initial play of your reel by the same account for at least 1ms in the same session. | lifetime |
| `fb_reels_total_plays` | The number of times your reel starts to play after an impression is already counted.This is defined as reel sessions with 1ms or more and includes replays. Replays are counted after the initial play of the reel in the same session. | lifetime |
| `post_impressions_unique` | The number of people who saw your reel at least once, whether or not the person played your reel. This metric is different from impressions, which includes multiple views of your reel by the same person. This metric is estimated. | lifetime |
| `post_video_avg_time_watched` | The average number of milliseconds your reel was played during a single instance of playing it, including time spent replaying your reel. Because this metric includes replays, the value can be greater than the total length of the reel. | lifetime |
| `post_video_followers` | The number of follows for your reel. | lifetime |
| `post_video_likes_by_reaction_type` | The number of likes on your reel. | lifetime |
| `post_video_retention_graph` | The percentage of times your reel was played at various timestamp segments out of the total number of plays. Most reels will start out at 100% retention and curve downward as plays begin to drop off. If someone skipped the beginning of the reel, your curve will start at the timestamp where the reel started playing. | lifetime |
| `post_video_social_actions` | The number of comments on your reel and the number of times your reel was shared. | lifetime |
| `post_video_view_time` | The total number of milliseconds your reel played, including time spent replaying your reel. | lifetime |