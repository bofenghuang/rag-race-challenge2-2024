platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/recovery-and-redundancy-features

Recovery and redundancy features

Note:These recovery and redundancy features are only available to those that have Enterprise access.

## Introduction

When consuming realtime data, maximizing your connection time and receiving all matched data is a fundamental goal. This means that it is important to take advantage of redundant connections, automatically detect disconnections, to reconnect quickly, and to have a plan for recovering lost data.

In this integration guide, we will discuss different recovery and redundancy features: redundant connections, backfill, and recovery.