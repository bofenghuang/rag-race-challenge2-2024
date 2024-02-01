platform: X
topic: Twitter-API-Enterprise
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/enrichments/overview/poll-metadata


# 

Poll metadata is a free enrichment available across all products (Realtime & Historical APIs) in enriched native format payloads. The metadata notes the presence of the poll in a Tweet, includes the list of poll choices, and includes both the poll duration and expiration time. This enrichment makes it easy to acknowledge the presence of a poll and enables proper rendering of a poll Tweet for display.

##### Important Details:

* Available across all enterprise APIs (PowerTrack, Replay, Search, Historical PowerTrack)
    * _Note:_ For Replay and Historical PowerTrack, this metadata was first made available on 02/22/17 - see documented [enrichment availability](https://developer.twitter.com/content/developer-twitter/en/docs/tweets/batch-historical/guides/hpt-timeline).
* Does not include vote information or poll results
* Does not currently have filter/operator support
* Available in **enriched native format** only
    * Enriched native format is a user-controlled setting that can be changed at any time through the Console: _Select a Product (PowerTrack, Replay, Search) > Settings tab > Output Format (Leave data in its original format)_