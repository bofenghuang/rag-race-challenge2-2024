platform: CrowdTangle
topic: API
subtopic: API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/CrowdTangle_API/API Documentation.md
url: https://github.com/CrowdTangle/API/wiki/AccountStatistics


### [](#accountstatistics)AccountStatistics

An AccountStatistics object represents the aggregate statistics of an [account](https://github.com/CrowdTangle/API/wiki/Account) over the specified time. A list of these objects makes up a leaderboard, see examples in [/leaderboard](https://github.com/CrowdTangle/API/wiki/Leaderboard).

#### [](#properties)Properties

| Property | Type | Description |
| --- | --- | --- |
| account | [account](https://github.com/CrowdTangle/API/wiki/Account) | Details about the account not related to statistics. |
| breakdown | Map<String, [StatisticSet](https://github.com/CrowdTangle/API/wiki/AccountStatistics#StatisticSet)\> | A StatisticSet for each type of [post](https://github.com/CrowdTangle/API/wiki/Post) the account posted. E.g. photo, video, etc. |
| subscriberData | [SubscriberData](https://github.com/CrowdTangle/API/wiki/AccountStatistics#SubscriberData) | The subscriberCounts relevant to the date range requested. |
| summary | [StatisticSet](https://github.com/CrowdTangle/API/wiki/AccountStatistics#StatisticSet) | An aggregate StatisticSet of the `breakdown`. |