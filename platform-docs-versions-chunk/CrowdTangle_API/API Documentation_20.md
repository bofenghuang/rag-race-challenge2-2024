platform: CrowdTangle
topic: API
subtopic: API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/CrowdTangle_API/API Documentation.md
url: https://github.com/CrowdTangle/API/wiki/Post


### [](#statistics)Statistics

Two sets of metrics for a post: `actual` and `expected`. `actual` represents the actual metrics of the post, e.g., likeCount or commentCount. `expected` represents what that post's metrics were expected to be given that post's properties, as calculated by CrowdTangle. These metrics differ by `platform`. For instance, Facebook will include, "likeCount," "commentCount," and "shareCount" while Instagram includes "favoriteCount" and "commentCount." The full list is below.

#### [](#properties-1)Properties

| Property | Type | Description |
| --- | --- | --- |
| actual | Map<String, Long> | A set of key-value pairs representing the actual metrics of the post. |
| expected | Map<String, Long> | A set of key-values pairs representing the metrics CrowdTangle expected a post like this to accrue. |

##### [](#possible-metrics)Possible Metrics

| Property | platforms |
| --- | --- |
| angryCount | Facebook |
| commentCount | Facebook, Instagram, Reddit |
| favoriteCount | Instagram |
| hahaCount | Facebook |
| likeCount | Facebook |
| loveCount | Facebook |
| sadCount | Facebook |
| shareCount | Facebook |
| upCount | Reddit |
| wowCount | Facebook |
| thankfulCount\* | Facebook |
| careCount | Facebook |

\*The purple flower "Thankful" reaction was a temporary reaction available in 2016 and 2017. (See more [HERE](https://about.fb.com/news/2017/05/join-facebook-in-celebrating-moms-around-the-world/)). This metric surfaces thankfulCount for legacy posts that accrued Thankful reactions prior to the reaction's removal from Facebook.