platform: Facebook
topic: Graph-API
subtopic: Video Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Video Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/video/video_insights/


### Video Metrics

The following metrics are available for the `metric` [parameter](#parameters) when you read aggregated insights for a video.

| Name | Description | Values for `period` |
| --- | --- | --- |
| `total_video_views` | The number of times your videos played for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_views_unique` | The number of people who viewed your videos for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_views_autoplayed` | The number of times your videos automatically played for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_views_clicked_to_play` | The number of times your videos played for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds, after people clicked play. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_views_organic` | The number of times your videos played for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds, by organic reach. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_views_organic_unique` | The number of people who viewed your videos for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds, by organic reach. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_views_paid` | The number of times your promoted videos played for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds. For each [impression](https://www.facebook.com/business/help/675615482516035) of a video, we'll count video views separately and exclude any time spent replaying the video. | lifetime |
| `total_video_views_paid_unique` | The number of people who viewed your promoted videos for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds. For each [impression](https://www.facebook.com/business/help/675615482516035) of a video, we'll count video views separately and exclude any time spent replaying the video. | lifetime |
| `total_video_views_sound_on` | The number of times your videos played with sound on for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_complete_views` | The number of times your videos played for 97%, or more, or its length. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_complete_views_unique` | The number of people who viewed your videos for 97%, or more, of its length. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_complete_views_auto_played` | The number of times your videos automatically played for 97%, or more, of its length. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_complete_views_clicked_to_play` | The number of times your videos played for 97%, or more, of its length, after people clicked play. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_complete_views_organic` | The number of times your videos played for 97%, or more, of its length, by organic reach. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_complete_views_organic_unique` | The number of people who viewed your videos for 97%, or more, of its length, by organic reach. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_complete_views_paid` | The number of times your promoted videos played for 97%, or more, of its length. For each [impression](https://www.facebook.com/business/help/675615482516035) of a video, we'll count video views separately and exclude any time spent replaying the video. | lifetime |
| `total_video_complete_views_paid_unique` | The number of people who viewed your promoted videos for 97%, or more, of its length. For each [impression](https://www.facebook.com/business/help/675615482516035) of a video, we'll count video views separately and exclude any time spent replaying the video. | lifetime |
| `total_video_10s_views` | The number of times your videos played for 10 seconds. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_10s_views_unique` | The number of people who viewed your videos for 10 seconds or more. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_10s_views_auto_played` | The number of times your videos automatically played for 10 seconds or more. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_10s_views_clicked_to_play` | The number of times your videos played for 10 seconds or more, after people clicked play. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_10s_views_organic` | The number of times your videos played for 10 seconds or more, by organic reach. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_10s_views_paid` | The number of times your promoted videos played for 10 seconds or more. For each [impression](https://www.facebook.com/business/help/675615482516035) of a video, we'll count video views separately and exclude any time spent replaying the video. | lifetime |
| `total_video_10s_views_sound_on` | The number of times your videos played with sound on for 10 seconds or more. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_15s_views` | The number of times your videos played for 15 seconds or more. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_60s_excludes_shorter_views` | The number of times your videos played for 60 seconds or more. During a single instance of a video playing, we'll exclude any time spent replaying the video. | lifetime |
| `total_video_retention_graph` | The number of times your videos played at each interval as a percentage of all views. Videos are divided into 40 equal intervals. Retention graphs may show more [impressions](https://www.facebook.com/business/help/675615482516035) later in the video than at the beginning. People might start the video in the middle, skip ahead, save, and rewatch it from that point, or other similar behaviors | lifetime |
| `total_video_retention_graph_autoplayed` | The number of times your videos automatically played at each interval as a percentage of all views. Videos are divided into 40 equal intervals. Retention graphs may show more [impressions](https://www.facebook.com/business/help/675615482516035) later in the video than at the beginning. People might start the video in the middle, skip ahead, save, and rewatch it from that point, or other similar behaviors. | lifetime |
| `total_video_retention_graph_clicked_to_play` | The number of times your videos played at each interval as a percentage of all views, after people clicked play. Videos are divided into 40 equal intervals. Retention graphs may show more [impressions](https://www.facebook.com/business/help/675615482516035) later in the video than at the beginning. People might start the video in the middle, skip ahead, save, and rewatch it from that point, or other similar behaviors. | lifetime |
| `total_video_avg_time_watched` | The average time, in milliseconds, people viewed your videos. | lifetime |
| `total_video_view_total_time` | The total time, in milliseconds, people viewed your videos. | lifetime |
| `total_video_view_total_time_organic` | The total time, in milliseconds, people viewed your videos, by organic reach. | lifetime |
| `total_video_view_total_time_paid` | The total time, in milliseconds, people viewed your promoted videos. | lifetime |
| `total_video_impressions` | The total number of [impressions](https://www.facebook.com/business/help/675615482516035) of your videos. | lifetime |
| `total_video_impressions_unique` | The total number of unique [impressions](https://www.facebook.com/business/help/675615482516035) of your videos. | lifetime |
| `total_video_impressions_paid_unique` | The total number of unique [impressions](https://www.facebook.com/business/help/675615482516035) or your promoted videos. | lifetime |
| `total_video_impressions_paid` | The total number of [impressions](https://www.facebook.com/business/help/675615482516035) of your promoted videos. | lifetime |
| `total_video_impressions_organic_unique` | The total number of unique [impressions](https://www.facebook.com/business/help/675615482516035) of your videos, by organic reach. | lifetime |
| `total_video_impressions_organic` | The total number of [impressions](https://www.facebook.com/business/help/675615482516035) of your videos, by organic reach. | lifetime |
| `total_video_impressions_viral_unique` | The total number of unique [impressions](https://www.facebook.com/business/help/675615482516035) of your videos in a friend's story. | lifetime |
| `total_video_impressions_viral` | The total number of [impressions](https://www.facebook.com/business/help/675615482516035) of your videos in a story generated by a friend. | lifetime |
| `total_video_impressions_fan_unique` | The total number of unique [impressions](https://www.facebook.com/business/help/675615482516035) of your videos for people who liked your Page. | lifetime |
| `total_video_impressions_fan` | The total number of [impressions](https://www.facebook.com/business/help/675615482516035) of your videos for people who liked your Page. | lifetime |
| `total_video_impressions_fan_paid_unique` | The total number of unique [impressions](https://www.facebook.com/business/help/675615482516035) of your promoted videos for people who liked your Page. | lifetime |
| `total_video_impressions_fan_paid` | The total number of [impressions](https://www.facebook.com/business/help/675615482516035) of your promoted video for people who liked your Page. | lifetime |
| `total_video_stories_by_action_type` | The total number of stories created about your Page's video, by action type; liking, commenting, sharing, etc. | lifetime |
| `total_video_reactions_by_type_total` | The total number of reactions to your Page's video, by type. | lifetime |
| `total_video_view_time_by_age_bucket_and_gender` | The total time, in milliseconds, your video has been viewed by Top Audiences; age and gender. | lifetime |
| `total_video_view_time_by_region_id` | The total time, in milliseconds, your Page's videos played for your Top 45 Locations; Region - Country. | lifetime |
| `total_video_views_by_distribution_type` | The number of times your videos played by distribution type; page\_owned and shared. | lifetime |
| `total_video_view_time_by_distribution_type` | The total time, in milliseconds, your Page's videos played by distribution type; page\_owned and shared. | lifetime |
| `total_video_view_total_time_live` | Total time (in ms) video has been viewed when it was broadcasted live. (Total Count). | lifetime |
| `total_video_views_by_country_id` | Lifetime video views by country. | lifetime |
| `total_video_views_live` | Number of people who viewed your video for 3 seconds or viewed to the end, when it was streamed live. | lifetime |
| `total_video_views_by_age_bucket_and_gender` | Lifetime video views by age bucket and gender. | lifetime |
| `total_video_views_gender_male` | Lifetime total number of times your videos played for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds by male viewers. | lifetime |
| `total_video_views_gender_female` | Lifetime total number of times your videos played for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds by female viewers. | lifetime |
| `total_video_views_live_clicked_to_play` | Lifetime total number of times people clicked to play your video and viewed it more than 3 seconds - while it was being streamed live. | lifetime |
| `total_video_views_gender_male_live` | Lifetime total number of times males viewed your video for more than 3 seconds while it was being streamed live. | lifetime |
| `total_video_views_live_autoplayed` | Lifetime total number of times your video started automatically playing and people viewed it for more than 3 seconds - while it was being streamed live. | lifetime |
| `total_video_views_gender_female_live` | Lifetime total number of times females viewed your video for more than 3 seconds while it was being streamed live. | lifetime |
| `has_total_video_views_by_publisher_platform_type` | Whether the video played for at least 3 seconds, or for nearly their total length if they're shorter than 3 seconds broken down by publisher platform type. | lifetime |
| `total_video_30s_views` | Total number of times your video was viewed for 30 seconds or 97% of the video if video is less than 30 seconds. (Total Count) | lifetime |

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)