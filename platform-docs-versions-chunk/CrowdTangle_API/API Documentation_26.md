platform: CrowdTangle
topic: API
subtopic: API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/CrowdTangle_API/API Documentation.md
url: https://github.com/CrowdTangle/API/wiki/AccountStatistics

### [](#subscriberdata)SubscriberData

The subscriberData for the given date range.

| Property | Type | Description |
| --- | --- | --- |
| finalCount | int | The number of the subscribers the account had at the end of the date range. |
| initialCount | int | The number of subscribers the account had at the start of the date range. |
| notes | String | Human-readable notes. Counts may not be available for selected date ranges based on when we started tracking an account within CrowdTangle. If initialCount or finalCount is 0, we likely were not tracking the account at that time. This can be confirmed by referencing the notes section which could look like this: "No subscriberCount available for beginning of time range." If the note section is present at all, any calculations made with subscriberCount data will need to take into account potentially missing data. |