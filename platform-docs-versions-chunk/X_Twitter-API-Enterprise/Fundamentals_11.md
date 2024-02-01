platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/console/usage

Usage tab

## Usage tab

The Usage Tab provides insight into your use of your streams over various time periods. For programmatic access to usage information, see the [Usage API](https://developer.twitter.com/en/docs/twitter-api/enterprise/usage-api/overview.html).

### Monthly

The Monthly Usage page displays your stream usage broken down by product. For example, coverage products (for example, PowerTrack, Historical PowerTrack, and PowerTrack Replay) for a given data source will be grouped together to provide separate data, as well as a combined roll-up count. The counts include a current month-to-date, estimated end-of-month (based on this month’s usage so far, and remaining time in the month), and the previous two months’ counts.

Notably, these counts are deduplicated for each product and stream. If you received the same Tweet through multiple connections to the same PowerTrack stream, that Tweet will be counted once for these purposes. Counts will be updated every 24 hours at 00:00 UTC.