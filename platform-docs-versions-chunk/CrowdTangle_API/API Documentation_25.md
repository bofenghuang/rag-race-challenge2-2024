platform: CrowdTangle
topic: API
subtopic: API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/CrowdTangle_API/API Documentation.md
url: https://github.com/CrowdTangle/API/wiki/AccountStatistics


### [](#statisticset)StatisticSet

Aggregate data for the account in question. Includes basic metrics (likeCount, commentCount, shareCount) as well as some additional metrics. Some of these metrics are platform specific. See [Post/statistics](https://github.com/CrowdTangle/API/wiki/Post#statistics) for the by-platform breakdown.

| Property | Type | Description |
| --- | --- | --- |
| angryCount | int | Total number of angrys. |
| commentCount | int | Total number of comments. |
| favoriteCount | int | Total number of favorites. |
| hahaCount | int | Total number of hahas. |
| interactionRate | double | The interactionRate for the given aggregation. This is provided at a percentage. E.g., An `interactionRate` of 1.324 is 1.32%, not 132%. |
| likeCount | int | Total number of likes for given aggregation. |
| loveCount | int | Total number of loves. |
| postCount | int | Total number of posts posted for the given aggregation. |
| repostCount | int | Total number of reposts. |
| sadCount | int | Total number of sads. |
| shareCount | int | Total number of shares. |
| totalInteractionCount | int | The sum of the individual metric counts. E.g., likeCount + shareCount + commentCount. |
| upCount | int | Total number of upvotes. |
| wowCount | int | Total number of wows. |
| careCount | int | Total number of cares. |
| threePlusMinuteVideoCount | int | The count of the aggregation's videos of length 3 minutes or longer. |
| totalVideoTimeMS | int | Total video time in milliseconds. |